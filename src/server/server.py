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
    sio.emit('message', 'connected to server', sid)

@sio.on('message')
def message(sid, data):
    #data.message, data.room_id
    print('message', data)

    room_id = player_list[sid]
    if(room_id is not None):
        room = rooms[room_id]

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

    sio.enter_room(sid, id)
    name = rooms[id].add_player(sid)   
    session['name'] = name
    sio.save_session(sid, session)

    player_list[sid] = id 
    sio.emit('message', 'Room {} created. Joining game as {}'.format(id, name), room=id)
    sio.emit('room_created', {'room_id': str(id), 'player_name': name}, sid)    

@sio.on('join_room')
def join_room(sid): #data = room_id

    session = sio.get_session(sid)
    if('room' not in session or session['room'] is None):
#        if(data is None):  #join first joinable room
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

                    sio.emit('message', 'Player joined as {}'.format(name), key)
                    sio.emit('joined_game', {'room_id':str(key), 'player_name':name}, sid)
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
        start_player_info = room.start_game() #name, id
        sio.emit('message', 'Game started!', room_id)
        sio.emit('game_started', start_player_info, room_id)

@sio.on('move')
def move(sid, tileName): #tileName: ex. Library, h_sh, etc.        
    room_id = player_list[sid]
    game = rooms[room_id]

    if(game.is_player_turn(sid)):
        if(game is not None):
            player = game.get_player(sid)
            if(player.moved):
                sio.emit('message', 'You already moved.', sid)
                return

            valid = game.player_moved(sid, tileName)
            if(valid):
                        
                player.moved = True
                
                sio.emit('message', '{} moved to {}'.format(player.name, player.location.name), room_id)
                sio.emit('moved', {'name': player.name, 'location': player.location.name}, room_id)

        

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

            if(player.suggested):
                sio.emit('message', 'You already made a suggestion', sid)
                return

            player = game.get_player(sid)
            if(player.location.name != case['location']):
                sio.emit('message', 'Player must be in the room that he is suggesting.', room_id)
                return
            if(player.location.type == TileType.HALLWAY):
                sio.emit('message', 'Player must be in a room to suggest.', room_id)
                return

            sio.emit('message', 'Suggestion is made: Crime was committed in the {} by {} with the {}'.format(case['location'], case['suspect'], case['weapon']), room_id)
            result = game.suggestion_made(sid, case)
            player.suggested = True

            if(result is False):
                pass #invalid
            if(result['card'] is None):
                #no one had matching card
                sio.emit('message', 'No one had matching card', room_id)
            else:
                sio.emit('message', 'Player {} showed 1 card'.format(result['player_name']) ,room_id)
                sio.emit('suggest_result', {'name': result['card'].name, 'type': str(result['card'].type)}, sid )



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
            sio.emit('message', '{} made a wrong accuation. Player cannot make a move from this point.'.format(player.name), room_id)
            nextPlayer = game.end_turn(sid)
            sio.emit('message', 'It is now {}''s turn'.format(nextPlayer), room_id)


        sio.emit('accuse_result', {"is_correct": result}, room_id)
        
        #TODO: end game


@sio.on('end_turn')
def end_turn(sid):
    room_id = player_list[sid]
    game = rooms[room_id]

    if(game.is_player_turn(sid)):
        player = game.get_player(sid)
        nextPlayer = game.end_turn(sid)

        sio.emit('message', '{} ended his/her turn'.format(player.name), room_id)
        sio.emit('message', 'It is now {}''s turn'.format(nextPlayer.name), room_id)
        sio.emit('start_turn', 'It is your turn' ,nextPlayer.id)



if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen((host,port)), app)