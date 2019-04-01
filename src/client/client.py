import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('connected')

@sio.on('message')
def on_message(data):
    print('message received', data)

@sio.on('disconnect')
def on_disconnect():
    print('disconnected')

sio.connect('http://localhost:5000')

while 1:
    selection = input('type selection (1: send message, 2: create game, 3: disconnect): ')
    print(selection)
    if selection == "1":
        msg = input('enter message:')
        sio.emit('message', {'msg': msg})
    elif selection == "2":
        sio.emit('create_room')
    elif selection == "3":
        sio.disconnect()
        break


print('program ended')