import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('connected')

@sio.on('message')
def on_message(data):
    print('message received ', data)

@sio.on('disconnect')
def on_disconnect():
    print('disconnected')

@sio.on('debug')
def on_debug(data):
    print(data)


sio.connect('http://localhost:5000')

while 1:
    selection = input('type selection (1: send message, 2: create game, 3: disconnect, 4: debug): ')
    print(selection)
    if selection == "1":
        msg = input('enter message:')
        sio.emit('message', {'msg': msg})        
    elif selection == "2":
        sio.emit('create_room')
    elif selection == "3":
        sio.disconnect()
    elif selection == "4":
        sio.emit('debug')
    


print('program ended')