import socketio

#this is the text based client

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('connected')

@sio.on('message')
def on_message(data):
    print(data)

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
    pass
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

# Triggered when current player makes suggestion. Data contains information of the card shown by other player
# This is only triggered if current player on this client makes suggestion and other players do not get this info.
# data.player_name - name of player who showed card to you
# data.name - name of the card shown
# data.type - type of the card shown
@sio.on('suggest_result') #only received by player who suggested
def on_suggest_result(data): 
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

@sio.on('all_locations')
def on_print_board(data): #player list info 
    size = 10
    print('')
    print('----------', end="")
    print('    ', end="")
    print('----------', end="")
    print('    ', end="")
    print('----------')

    print('|', end="")    
    if('Study' in data):
        print('{0: ^8}'.format(join(data['Study'],',')), end="")
    else:
        print('        ', end="")
    print('|', end="")    
    if('h_sh' in data):
        print('{0:-^4}'.format(join(data['h_sh'],',')), end="") #hallway
    else:
        print('----', end="")
    print('|', end="")    
    if('Hall' in data):
        print('{0: ^8}'.format(join(data['Hall'],',')), end="")
    else:
        print('        ', end="")
    print('|', end="")    
    if('h_hl' in data):
        print('{0:-^4}'.format(join(data['h_hl'],',')), end="") #hallway
    else:
        print('----', end="")
    print('|', end="")    
    if('Lounge' in data):
        print('{0: ^8}'.format(join(data['Lounge'],',')), end="")
    else:
        print('        ', end="")
    print('|')    

    print('----------', end="")
    print('    ', end="")
    print('----------', end="")
    print('    ', end="")
    print('----------')



    print('  |', end="")    
    if('h_sl' in data):
        print('{0: ^4}'.format(join(data['h_sl'],',')), end="") #hallway
    else:
        print('    ', end="")
    print('|  ', end="")  
    print('    ', end="")    
    print('  |', end="")    
    if('h_hb' in data):
        print('{0: ^4}'.format(join(data['h_hb'],',')), end="") #hallway
    else:
        print('    ', end="")
    print('|  ', end="")  
    print('    ', end="")  
    print('  |', end="")    
    if('h_ld' in data):
        print('{0: ^4}'.format(join(data['h_ld'],',')), end="") #hallway
    else:
        print('    ', end="")
    print('|')



    print('----------', end="")
    print('    ', end="")
    print('----------', end="")
    print('    ', end="")
    print('----------')

    print('|', end="")    
    if('Library' in data):
        print('{0: ^8}'.format(join(data['Library'],',')), end="")
    else:
        print('        ', end="")
    print('|', end="")    
    if('h_lb' in data):
        print('{0:-^4}'.format(join(data['h_lb'],',')), end="") #hallway
    else:
        print('----', end="")
    print('|', end="")    
    if('Billiard Room' in data):
        print('{0: ^8}'.format(join(data['Billiard Room'],',')), end="")
    else:
        print('        ', end="")
    print('|', end="")    
    if('h_bd' in data):
        print('{0:-^4}'.format(join(data['h_bd'],',')), end="") #hallway
    else:
        print('----', end="")
    print('|', end="")    
    if('Dining Room' in data):
        print('{0: ^8}'.format(join(data['Dining Room'],',')), end="")
    else:
        print('        ', end="")
    print('|')    

    print('----------', end="")
    print('    ', end="")
    print('----------', end="")
    print('    ', end="")
    print('----------')



    print('  |', end="")    
    if('h_lc' in data):
        print('{0: <4}'.format(join(data['h_lc'],',')), end="") #hallway
    else:
        print('    ', end="")
    print('|  ', end="")  
    print('    ', end="")    
    print('  |', end="")    
    if('h_bb' in data):
        print('{0: <4}'.format(join(data['h_bb'],',')), end="") #hallway
    else:
        print('    ', end="")
    print('|  ', end="")  
    print('    ', end="")  
    print('  |', end="")    
    if('h_dk' in data):
        print('{0: <4}'.format(join(data['h_dk'],',')), end="") #hallway
    else:
        print('    ', end="")
    print('|')



    print('----------', end="")
    print('    ', end="")
    print('----------', end="")
    print('    ', end="")
    print('----------')

    print('|', end="")    
    if('Conservatory' in data):
        print('{0: ^8}'.format(join(data['Conservatory'],',')), end="")
    else:
        print('        ', end="")
    print('|', end="")    
    if('h_cb' in data):
        print('{0:-^4}'.format(join(data['h_cb'],',')), end="") #hallway
    else:
        print('----', end="")
    print('|', end="")    
    if('Ballroom' in data):
        print('{0: ^8}'.format(join(data['Ballroom'],',')), end="")
    else:
        print('        ', end="")
    print('|', end="")    
    if('h_bk' in data):
        print('{0:-^4}'.format(join(data['h_bk'],',')), end="") #hallway
    else:
        print('----', end="")
    print('|', end="")    
    if('Kitchen' in data):
        print('{0: ^8}'.format(join(data['Kitchen'],',')), end="")
    else:
        print('        ', end="")
    print('|')    

    print('----------', end="")
    print('    ', end="")
    print('----------', end="")
    print('    ', end="")
    print('----------')


sio.connect('http://localhost:5000')

suspects = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Mrs. White", "Colonel Mustard"]
weapons = ["Rope", "Lead Pipe", "Knife", "Wrench", "Candlestick", "Revolver"]
rooms = ["Study", "Hall", "Lounge", "Library", "Billiard Room", "Dining Room", "Conservatory", "Ballroom", "Kitchen"]


def join_selection(l, abbreviate):
    out = ''
    for i, el in enumerate(l):
        if(abbreviate):  
            el = "".join(e[0] for e in el.split())

            out += '{}:{}-{}{}'.format(i, el, l[i], ', ')
        else:
            out += '{}:{}{}'.format(i, l[i], ', ')

    return out[:-len(', ')]

while 1:
    selection = input('Type selection (0:join, 1: send message, 2: create game, 3: disconnect, 4: debug, 5: start, 6: move, 7: suggest, 8:accuse, 9: end, 10: print board): ')
    print(selection)
    if selection == "1":
        msg = input('Enter message:')
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
        print(join_selection(rooms, False))
        loc = input('Enter location number. If it is hallway, enter the name of hallway instead. (ex. h_sh):')
        try:
            locInt = int(loc)
            location = rooms[locInt]
        except ValueError:
            location = loc
        
        tile = location
        sio.emit('move', tile)              #tile - name of the tile (ex. Hall, h_sh, ...)
    elif selection == "7":
        print(join_selection(suspects, True))
        suspect = suspects[int(input('Enter suspect number:'))]
        print(join_selection(rooms, False))
        location = rooms[int(input('Enter location number :'))] 
        print(join_selection(weapons, False))
        weapon = weapons[int(input('Enter weapon number:'))]
        sio.emit('suggest', {"suspect":suspect, "location":location, "weapon":weapon}) #ex. 'Mrs. White', 'Study', 'Knife'
    elif selection == "8":
        print(join_selection(suspects, True))
        suspect = suspects[int(input('Enter suspect number:'))]
        print(join_selection(rooms, False))
        location = rooms[int(input('Enter location number :'))] 
        print(join_selection(weapons, False))
        weapon = weapons[int(input('Enter weapon number:'))]
        sio.emit('accuse', {"suspect":suspect, "location":location, "weapon":weapon}) #ex. 'Mrs. White', 'Study', 'Knife'
    elif selection == "9":
        sio.emit('end_turn')
    elif selection == "10":
        sio.emit('get_all_location')
    


print('program ended')
