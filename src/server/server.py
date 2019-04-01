#Communication logic

#import engineio
import eventlet
import socketio

from game import Game

host = ''
port = 5000

sio = socketio.Server(logger=True)
app = socketio.WSGIApp(sio)

roomNames = []

@sio.on('connect')
def connect(sid, environ):
    sio.save_session(sid, {"test" : "test string"})
    print('connect', sid)

@sio.on('message')
def message(sid, data):
    print('message', data)
    sio.emit('message', data)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect', sid)

@sio.on('create_room')
def create_room(sid):
    roomNames.append(Game())
    sio.enter_room(sid, len(roomNames) - 1)
    sio.emit('message', 'Room ' + str(len(roomNames) - 1)+'  created')

@sio.on('join_room')
def join_room(sid, data):
    sio.enter_room(sid, data)



if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen((host,port)), app)