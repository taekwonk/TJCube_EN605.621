#Communication logic

#import engineio
import eventlet
import socketio
import uuid

from game import Game
import player

host = ''
port = 5000

sio = socketio.Server(logger=True)
app = socketio.WSGIApp(sio)

rooms = {}
player_list = {}

@sio.on('connect')
def connect(sid, environ):
    sio.save_session(sid, {"test" : "test string"})
    print('connect', sid)

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

    session = sio.session as session
    session['room'] = id
    sio.save_session(sid, session)

    sio.enter_room(sid, id)
    sio.emit('message', 'Room ' + id +'  created')

@sio.on('join_room')
def join_room(sid, data): #data = room_id

    session = sio.session as session
    if(session['room'] is None):    
        if(data is None):  #join first joinable room
            for key, value in rooms.items():
                if(value.joinable()):
                    name = value.add_player(sid)
                    if(name):
                        sio.enter_room(sid, key)
                        session = sio.session as session
                        session['room'] = key
                        session['name'] = name
                        sio.save_session(sid, session)
                                
                        player_list[sid] = key

                        sio.emit({key, name})
                    else:
                        sio.emit(None)
    
    else : #rejoining from connection drop, for example. Maybe don't need this?
        sio.enter_room(sid, key) 
        sio.emit(session['room'])
                
    # else:
    #     sio.enter_room(sid, data)
    #     session = sio.session as session
    #     session['room'] = data
    #     sio.save_session(sid, session)

    #     sio.emit(data)
    
    return sio.emit(None)

@sio.on('start_game')
def start_game(sid, room_id):
    room = rooms[room_id]
    if(room is not None):
        room.start_game()





if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen((host,port)), app)