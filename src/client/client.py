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

# Triggered when room is created. Data contains room id and player name
# Only triggered for current player on this client.
# data.room_id
# data.player_name
@sio.on('room_created')
def on_room_created(data): 
    print(data)

# Triggered when current player on this client joins a game. Data contains room id and player name
# Only triggered for current player on this client.
# data.room_id
# data.player_name
@sio.on('joined_game')
def on_joined_game(data): 
    print(data)

# Triggered when the game is started. Data contains player that has the starting turn.
# data.name - player name
# data.id - player id
@sio.on('game_started')
def on_game_started(data): 
    print(data)

# Triggered when player moves. Data contains information about the player who moved
# data.name - player name (ex. Mrs. White)
# data.location - name of the player's new location (ex. 'Hall', h_sh, ...)
@sio.on('moved')
def on_moved(data): 
    print(data)

@sio.on('start_turn')
def on_start_turn(data):
    print(data)

# Triggered when current player makes suggestion. Data contains information of the card shown by other player
# This is only triggered if current player on this client makes suggestion and other players do not get this info.
# data.name - name of the card shown
# data.type - type of the card shown
@sio.on('suggest_result') #only received by player who suggested
def on_suggest_result(data): 
    print(data)

# Triggered when someone makes accuation. Data contains result of accusation whether it was correct or not
# data.is_correct - true/false whether accuse was correct.
@sio.on('accuse_result') 
def on_accuse_result(data): 
    print(data)



sio.connect('http://localhost:5000')

while 1:
    selection = input('type selection (0:join, 1: send message, 2: create game, 3: disconnect, 4: debug, 5: start, 6: move, 7: suggest, 8:accuse, 9: end): ')
    print(selection)
    if selection == "1":
        msg = input('enter message:')
        sio.emit('message', {'msg': msg})    
    elif selection =="0":
        sio.emit('join_room')    
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
        sio.emit('move', tile)              #tile - name of the tile (ex. Hall, h_sh, ...)
    elif selection == "7":
        suspect = input('enter suspect:')
        location = input('enter location:')
        weapon = input('enter weapon:')
        sio.emit('suggest', {"suspect":suspect, "location":location, "weapon":weapon}) #ex. 'Mrs. White', 'Study', 'Knife'
    elif selection == "8":
        suspect = input('enter suspect:')
        location = input('enter location:')
        weapon = input('enter weapon:')
        sio.emit('accuse', {"suspect":suspect, "location":location, "weapon":weapon}) #ex. 'Mrs. White', 'Study', 'Knife'
    elif selection == "9":
        sio.emit('end_turn')
    


print('program ended')