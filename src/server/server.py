#Communication logic

#import engineio
import eventlet
import socketio
import uuid

from game import Game
import player
from model.tile_type import TileType

host = ''
port = 5000

sio = socketio.Server(logger=True)
app = socketio.WSGIApp(sio)

rooms = {} #key= guid, value= game
player_list = {} #key=sid, value=room_id

@sio.on('debug')
def debug(sid):
    print('rooms', rooms)
    print('players', player_list)
    sio.emit('debug', {'sid': sid, 'test': 'test'})
#    sio.emit('message', rooms)
 #   sio.emit('message', player_list)

@sio.on('connect')
def connect(sid, environ):
    sio.save_session(sid, {"test" : "test string"})
    print('connect', sid)
    sio.emit('message', sid)

@sio.on('message')
def message(sid, data):
    #data.message, data.room_id
    print('message', data)
    sio.emit('message', data.message, data.room_id)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect', sid)
    player_list[sid] = None
    #handle game player leave?

@sio.on('create_room')
def create_room(sid):
    id = uuid.uuid4()
    rooms[id] = Game()

    session = sio.get_session(sid)
    session['room'] = id
    sio.save_session(sid, session)

    sio.enter_room(sid, id)
    name = rooms[id].add_player(sid)   
    player_list[sid] = id 
    sio.emit('message', 'Room {} created. Joining game as {}'.format(id, name), room=id)

@sio.on('join_room')
def join_room(sid, data): #data = room_id

    session = sio.get_session(sid)
    if(session['room'] is None):
        if(data is None):  #join first joinable room
            for key, value in rooms.items():
                if(value.joinable()):
                    name = value.add_player(sid)
                    if(name):
                        sio.enter_room(sid, key)
                        session = sio.get_session(sid)
                        session['room'] = key
                        session['name'] = name
                        sio.save_session(sid, session)
                                
                        player_list[sid] = key

                        sio.emit('joined_game', {key, name}, room=key)
                    else:
                        sio.emit('message', None, room=key)
    
    else : #rejoining from connection drop, for example. Maybe don't need this?
        #TODO: finish this
        sio.enter_room(sid, key) 
        sio.emit('message', 'Rejoined room', room=session['room'])
                
    # else:
    #     sio.enter_room(sid, data)
    #     session = sio.session as session
    #     session['room'] = data
    #     sio.save_session(sid, session)

    #     sio.emit(data)
    

@sio.on('start_game')
def start_game(sid):
    #TODO: add precondition

    room_id = player_list[sid]
    room = rooms[room_id]
    if(room is not None):
        start_player_info = room.start_game()
        sio.emit('game_started', start_player_info, room_id)

@sio.on('move')
def move(sid, tileName): #tileName: ex. Library, h_sh, etc.        
    room_id = player_list[sid]
    game = rooms[room_id]

    if(game.is_player_turn(sid)):
        if(game is not None):
            valid = game.player_moved(sid, tileName)
            if(valid):
                sio.emit('message', 'player moved', room_id)
        

@sio.on('suggest')
def suggest(sid, case):
    #case.suspect - suspect name
    #case.location - room name
    #case.weapon - weapon name
    room_id = player_list[sid]
    game = rooms[room_id]

    if(game.is_player_turn(sid)):
        if(game is not None):
            player = game.get_player(sid)
            if(player.location.name != case['location']):
                sio.emit('message', 'Player must be in the room that he is suggesting.', room_id)
                return
            if(player.location.type == TileType.HALLWAY):
                sio.emit('message', 'Player must be in a room to suggest.', room_id)
                return

            sio.emit('message', 'Suggestion is made: Crime was committed in the {} by {} with the {}'.format(case['location'], case['suspect'], case['weapon']), room_id)
            result = game.suggestion_made(sid, case)
            if(result is False):
                pass #invalid
            if(result['card'] is None):
                #no one had matching card
                sio.emit('message', 'No one had matching card', room_id)
            else:
                sio.emit('message', 'Player {} showed 1 card'.format(result['player_name']) ,room_id)
                sio.emit('suggest_result', {'name': result['card'].name, 'type': result['card'].type}, sid )



@sio.on('accuse')
def accuse(sid, case):
    #case.suspect - suspect name
    #case.location - room name
    #case.weapon - weapon name

    room_id = player_list[sid]
    game = rooms[room_id]

    if(game.is_player_turn(sid)):
        result = game.accusation_made(sid, case)
        player = game.get_player(sid)
        if(result): #win!
            sio.emit('message', '{} found the answer, {} wins the game!'.format(player.name, player.name), room_id)
        else: #
            sio.emit('message', '{} made a wrong accuation. '.format(player.name), room_id)

        sio.emit('accuse_result', {"is_correct": result})
        
        #TODO: end game


@sio.on('end_turn')
def end_turn(sid):
    room_id = player_list[sid]
    game = rooms[room_id]

    if(game.is_player_turn(sid)):
        game.end_turn(sid)



if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen((host,port)), app)