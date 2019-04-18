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

@sio.on('suggest_result')
def on_suggest_result(data);
    print(data)

@sio.on('accuse_result')
def on_accuse_result(data);
    print(data)



sio.connect('http://localhost:5000')

while 1:
    selection = input('type selection (1: send message, 2: create game, 3: disconnect, 4: debug, 5: start, 6: move, 7: suggest, 8:accuse, 9: end): ')
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
    elif selection == "5":
        sio.emit('start_game')
    elif selection == "6":
        tile = input('enter destination:')
        sio.emit('move', tile)
    elif selection == "7":
        suspect = input('enter suspect')
        location = input('enter location')
        weapon = input('enter weapon')
        sio.emit('suggest', {"suspect":suspect, "location":location, "weapon":weapon})
    elif selection == "8":
        suspect = input('enter suspect')
        location = input('enter location')
        weapon = input('enter weapon')
        sio.emit('accuse', {"suspect":suspect, "location":location, "weapon":weapon})
    elif selection == "9":
        sio.emit('end_turn')
    


print('program ended')