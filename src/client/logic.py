# Johns Hopkins University - Whiting School of Engineering
# Engineering for Professionals
# Spring 2019 - Foundations of Software Engineering
# TJ^3 Project Group


import socketio

sio = socketio.Client()

hand = None

@sio.on('connect')
def on_connect():
    print('Successfully connected to the server.')

@sio.on('disconnect')
def on_disconnect():
    print('Successfully disconnected from the server.')

@sio.on('message')
def on_message(data):
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
    sio.emit('my_hand')
    #print(data)

# Triggered when player moves. Data contains information about the player who moved
# data.name - player name (ex. Mrs. White)
# data.location - name of the player's new location (ex. 'Hall', h_sh, ...)
@sio.on('moved')
def on_moved(data):
    pass
    #print(data)

@sio.on('start_turn')
def on_start_turn(data):
    print(data)

#returns data that is the hand of the current player
#data is array of cards dictionary({'name':'Knife', 'type':'CardType.WEAPON'})
@sio.on('my_hand')
def on_my_hand(data):
    global hand
    hand = data
    print('My Hand:', data)

#called as part of suggestion process. Player who receives this message must choose one of the cards suggested
#if player has no matching cards, it should return None
#if there are multiple cards, the client should let the user choose which one he/she wants to show
#this text client just selects one for you for simplicity sake
#data is the case object the other player suggested
#data.suspect - suspect name
#data.location - room name
#data.weapon - weapon name
@sio.on('suggest_react')
def on_suggest_react(data):
    print(hand)
    print('Your turn to react to suggestion, ')

    card = None
    for item in hand:
        if(item['name'] == data['suspect'] or item['name'] == data['location'] or item['name'] == data['weapon']):
            card = item
            break

    print('reacting with:', card)
    sio.emit('suggest_reacted', card)

# Triggered when current player makes suggestion. Data contains information of the card shown by other player
# This is only triggered if current player on this client makes suggestion and other players do not get this info.
# data.player_name - name of player who showed card to you
# data.name - name of the card shown
# data.type - type of the card shown
@sio.on('suggest_result') #only received by player who suggested
def on_suggest_result(data):
    print('suggest_result', data)
    print('{} showed {}'.format(data['player_name'], data['name']))

# Triggered when someone makes accuation. Data contains result of accusation whether it was correct or not
# data.is_correct - true/false whether accuse was correct.
@sio.on('accuse_result')
def on_accuse_result(data):
    pass
    #print(data)

def join(l, sep):
    out = ''
    for i, el in enumerate(l):
        el = "".join(e[0] for e in el.split())
        out += '{}{}'.format(el,sep)

    return out[:-len(sep)]

suspects = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Mrs. White", "Colonel Mustard"]
weapons = ["Rope", "Lead Pipe", "Knife", "Wrench", "Candlestick", "Revolver"]
rooms = ["Study", "Hall", "Lounge", "Library", "Billiard Room", "Dining Room", "Conservatory", "Ballroom", "Kitchen"]
