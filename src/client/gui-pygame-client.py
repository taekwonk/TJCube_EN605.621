# Johns Hopkins University - Whiting School of Engineering
# Engineering for Professionals
# Spring 2019 - Foundations of Software Engineering
# TJ^3 Project Group
#
# References:
# https://youtu.be/ajR4BZBKTr4
# https://inventwithpython.com/makinggames.pdf
# https://www.raywenderlich.com/2614-multiplayer-game-programming-for-teens-with-python-part-1
#
# PyGame Client GUI
# Reference: https://youtu.be/ajR4BZBKTr4
#
#
# TO-DO:
# Spawn character token sprite with each client ..?! Connected with each player
# Display player hand
# Display player character
# Display who's turn it is
# Display Player Location
# Functionality behind passage way buttons
# Save popDialog selected option in function
# Checkbox / Button change text color of known information (last priority)
# Room conditional states
# Deny suggestion if in a hallway
#
# https://github.com/miguelgrinberg/Flask-SocketIO/issues/822
#

import pygame as pg
import logging
import sys
import socketio
import tkinter as tk # lowercase for Python-3

from pygame.locals import *
from os import path
from settings import *
from sprites import *
from settings import *
from characters import *
from weapons import *
from rooms import *
from gameOptions import *

# Set up the Server-Client Connection ******************************************

sio = socketio.Client()
sio.connect('http://localhost:5000')

hand = None

@sio.on('connect')
def on_connect():
    print('Successfully Connected')

@sio.on('disconnect')
def on_disconnect():
    print('Successfully Disconnected')

# Triggered when current player on this client joins a game.
# Data contains room id and player name
# Only triggered for current player on this client.
# data.room_id
# data.player_name
@sio.on('joined_game')
def on_joined_game(data):
    print(data)

# Triggered when the game is started.
# Data contains player that has the starting turn.
# data.name - player name
# data.id - player id
@sio.on('game_started')
def on_game_started(data):
    sio.emit('my_hand')
    # Display player name
    #PLAYER_ID, PLAYER_ID_RECT = settings.displayServerData(data.name, 12, WHITE, 10, 10)
    #print(data)

# Triggered when player moves.
# Data contains information about the player who moved
# data.name - player name (ex. Mrs. White)
# data.location - name of the player's new location (ex. 'Hall', h_sh, ...)
@sio.on('moved')
def on_moved(data):
    pass
    #print(data)

@sio.on('start_turn')
def on_start_turn(data):
    print(data)

# Returns data that is the hand of the current player
# Data is array of cards dictionary({'name':'Knife', 'type':'CardType.WEAPON'})
@sio.on('my_hand')
def on_my_hand(data):
    global hand
    hand = data
    print('My Hand:', data)

# Called as part of suggestion process.
# Player who receives this message must choose one of the cards suggested
# If player has no matching cards, it should return None
# If there are multiple cards, the client should let the user choose which one he/she wants to show
# This client just selects one for you for simplicity sake
# Data is the case object the other player suggested
# data.suspect - suspect name
# data.location - room name
# data.weapon - weapon name
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

# Triggered when current player makes suggestion.
# Data contains information of the card shown by other player
# This is only triggered if current player on this client makes suggestion and other players do not get this info.
# data.player_name - name of player who showed card to you
# data.name - name of the card shown
# data.type - type of the card shown
@sio.on('suggest_result') #only received by player who suggested
def on_suggest_result(data):
    print('suggest_result', data)
    print('{} showed {}'.format(data['player_name'], data['name']))

# Triggered when someone makes accuation.
# Data contains result of accusation whether it was correct or not
# data.is_correct - true/false whether accuse was correct.
@sio.on('accuse_result')
def on_accuse_result(data):
    pass
    #print(data)

# Need???? --------------
def join(l, sep):
    out = ''
    for i, el in enumerate(l):
        el = "".join(e[0] for e in el.split())
        out += '{}{}'.format(el,sep)

    return out[:-len(sep)]

# Don't believe needed with GUI --------------
@sio.on('all_locations')
def on_print_board(data): #player list info
    pass

suspects = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Mrs. White", "Colonel Mustard"]
weapons = ["Rope", "Lead Pipe", "Knife", "Wrench", "Candlestick", "Revolver"]
rooms = ["Study", "Hall", "Lounge", "Library", "Billiard Room", "Dining Room", "Conservatory", "Ballroom", "Kitchen"]

# Text based move selection -- not sure needed but added in case
def join_selection(l, abbreviate):
    out = ''
    for i, el in enumerate(l):
        if(abbreviate):
            el = "".join(e[0] for e in el.split())

            out += '{}:{}-{}{}'.format(i, el, l[i], ', ')
        else:
            out += '{}:{}{}'.format(i, l[i], ', ')

    return out[:-len(', ')]


# Game Clue ********************************************************************

class Game:

    # Create a real-time log
    log = logging.getLogger()
    # Make log print to the console
    console = logging.StreamHandler()
    log.addHandler(console)
    # Emit a warning to the humans
    # Not sure if there is a better one than warning as info doesn't print log
    log.warning('Winter is Here')

    def quit_callback():
        global Done
        Done = True

    def __init__(self):
        # initialize pygame
        pg.init()
        self.players = []
        self.screen = WINDOW_SET
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat() # 1 move per key press
        self.load_data()
        logging.warning("Setting up basic configurations.")
        # initialize tkinter
        #popDialog = tk.Tk()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
        logging.warning("Loading the board map.")

    def new_board(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.rooms = pg.sprite.Group()
        self.halls = pg.sprite.Group()
        self.player = pg.sprite.Group()

        # INSTEAD: Have sprite create upon client connection up to 6 / start game
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                # Set Board Tiles
                if tile == 'H':
                    Hall(self, col, row, "Hall")
                if tile == '0':
                    Wall(self, col, row)
                # Rooms assigned to numbers
                if tile == '1':
                    Room(self, col, row, "Study")
                if tile == '2':
                    Room(self, col, row, "Hall")
                if tile == '3':
                    Room(self, col, row, "Lounge")
                if tile == '4':
                    Room(self, col, row, "Library")
                if tile == '5':
                    Room(self, col, row, "Billiard Room")
                if tile == '6':
                    Room(self, col, row, "Dining Room")
                if tile == '7':
                    Room(self, col, row, "Conservatory")
                if tile == '8':
                    Room(self, col, row, "Ballroom")
                if tile == '9':
                    Room(self, col, row, "Kitchen")

                # Need to spawn player with each client
                # Starting Player Token / Tiles
                # --- Player1 = Scarlet
                #if tile == 'S':
                #    self.player = Player(self, col, row, RED, player1)
                # --- Player2 = Mustard
                #if tile == 'M':
                #    self.player = Player(self, col, row, YELLOW, player2)
                # --- Player3 = White
                #if tile == 'W':
                #    self.player = Player(self, col, row, WHITE, player3)
                # --- Player4 = Green
                #if tile == 'G':
                #    self.player = Player(self, col, row, GREEN, player4)
                # --- Player5 = Peacock
                #if tile == 'B':
                #    self.player = Player(self, col, row, BLUE, player5)
                # --- Player6 = Plum
                #if tile == 'P':
                #    self.player = Player(self, col, row, PURPLE, player6)
        logging.warning("Set up board for a new game.")

    # Weird being here and a separate class. Worry about duplication later.
    # Note there is a dependency with the function call from gameOptions to the
    # class popDialog. However, while that class ran fine solo, it wouldn't run
    # properly until I added the function here in clueGame. To revisit if there
    # is time later.
    def popDialog(suspects, weapons, rooms):

        popupDialog = tk.Tk()
        popupDialog.geometry("300x200")
        popupDialog.title("What's Your Thoughts?")

        tk.Label(popupDialog, text="Murder Mystery:").grid(row=0)

        varSuspect = tk.StringVar()
        varWeapon = tk.StringVar()
        varRoom = tk.StringVar()

        tk.Label(popupDialog, text="Suspects: ").grid(row=1, column=0)
        # Suspect Options
        selectSuspect = tk.OptionMenu(popupDialog, varSuspect, *suspects)
        selectSuspect.configure(font=("Arial", 15))
        selectSuspect.grid(row=1, column=1)

        tk.Label(popupDialog, text="Weapons: ").grid(row=2, column=0)
        # Weapon Options
        selectWeapon = tk.OptionMenu(popupDialog, varWeapon, *weapons)
        selectWeapon.configure(font=("Arial", 15))
        selectWeapon.grid(row=2, column=1)

        tk.Label(popupDialog, text="Rooms: ").grid(row=3, column=0)
        # Room Options
        selectRoom = tk.OptionMenu(popupDialog, varRoom, *rooms)
        selectRoom.configure(font=("Arial", 15))
        selectRoom.grid(row=3, column=1)

        # Select Button
        selectBtn = tk.Button(popupDialog, text="Select") #, command=makeSelection)
        selectBtn.grid(row=4, column=1)

        tk.mainloop()

    def displayPlayerName():
        pass

    def displayPlayerLocation():
        pass

    def displayPlayerTurn():
        pass

    def displayPlayerHand():
        pass

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
        logging.warning("Ran Game Loop")

    def quit(self):
        pg.quit()
        sys.exit()
        logging.warning("Quit the game and shut the system down.")

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BGCOLOR)
        # Titles of window
        self.screen.blit(GAME_HEADER, GAME_HEADER_RECT)
        self.screen.blit(PLAYER_ID_HEADER, PLAYER_ID_HEADER_RECT)
        self.screen.blit(YOUR_CARDS_HEADER, YOUR_CARDS_HEADER_RECT)
        self.screen.blit(KNOWN_INFO_HEADER, KNOWN_INFO_HEADER_RECT)
        self.screen.blit(PLAYER_TURN_HEADER, PLAYER_TURN_HEADER_RECT)
        self.screen.blit(PLAYER_POSITION_HEADER, PLAYER_POSITION_HEADER_RECT)
        # Add Top Buttons
        self.screen.blit(CREATE_GAME_BTN, CREATE_GAME_RECT)
        self.screen.blit(JOIN_GAME_BTN, JOIN_GAME_RECT)
        self.screen.blit(START_GAME_BTN, START_GAME_RECT)
        self.screen.blit(QUIT_GAME_BTN, QUIT_GAME_RECT)
        # Add Secret Passage Way Buttons
        self.screen.blit(TO_KITCHEN_BTN, TO_KITCHEN_BTN_RECT)
        self.screen.blit(TO_STUDY_BTN, TO_STUDY_BTN_RECT)
        self.screen.blit(TO_CONSERVATORY_BTN, TO_CONSERVATORY_BTN_RECT)
        self.screen.blit(TO_LOUNGE_BTN, TO_LOUNGE_BTN_RECT)
        # Probably going to make one long box take in string array to display
        # Cards Display Boxes (Y at 200)
        pg.draw.rect(WINDOW_SET, RED, (725,200, 675, 75))
        #pg.draw.line(WINDOW_SET, BLACK, (800,200), (800,275), 5)
        #pg.draw.line(WINDOW_SET, BLACK, (875,200), (875,275), 5)
        #pg.draw.line(WINDOW_SET, BLACK, (950,200), (950,275), 5)
        #pg.draw.line(WINDOW_SET, BLACK, (1025,200), (1025,275), 5)
        #pg.draw.line(WINDOW_SET, BLACK, (1100,200), (1100,275), 5)
        #pg.draw.line(WINDOW_SET, BLACK, (1175,200), (1175,275), 5)
        #pg.draw.line(WINDOW_SET, BLACK, (1250,200), (1250,275), 5)
        #pg.draw.line(WINDOW_SET, BLACK, (1325,200), (1325,275), 5)
        #pg.draw.line(WINDOW_SET, BLACK, (1400,200), (1400,275), 5)
        # Cards Display Titles
        #self.screen.blit(CARD_1, CARD_1_RECT)
        #self.screen.blit(CARD_2, CARD_2_RECT)
        #self.screen.blit(CARD_3, CARD_3_RECT)
        #self.screen.blit(CARD_4, CARD_4_RECT)
        #self.screen.blit(CARD_5, CARD_5_RECT)
        #self.screen.blit(CARD_6, CARD_6_RECT)
        #self.screen.blit(CARD_7, CARD_7_RECT)
        #self.screen.blit(CARD_8, CARD_8_RECT)
        #self.screen.blit(CARD_9, CARD_9_RECT)
        # So&So's Turn
        # Known Information Section Boxes (Y at 350)
        pg.draw.rect(WINDOW_SET, RED, (725, 350, 675, 275))
        pg.draw.line(WINDOW_SET, BLACK, (950,350), (950,625), 5)
        pg.draw.line(WINDOW_SET, BLACK, (1175,350), (1175,625), 5)
        # Known Information Section Titles
        self.screen.blit(CHARACTERS_SECTION, CHARACTERS_SECTION_RECT)
        self.screen.blit(WEAPONS_SECTION, WEAPONS_SECTION_RECT)
        self.screen.blit(ROOMS_SECTION, ROOMS_SECTION_RECT)
        # Known Information Character Check Titles
        self.screen.blit(CHECK_CHAR_GREEN, CHECK_CHAR_GREEN_RECT)
        self.screen.blit(CHECK_CHAR_MUSTARD, CHECK_CHAR_MUSTARD_RECT)
        self.screen.blit(CHECK_CHAR_PEACOCK, CHECK_CHAR_PEACOCK_RECT)
        self.screen.blit(CHECK_CHAR_PLUM, CHECK_CHAR_PLUM_RECT)
        self.screen.blit(CHECK_CHAR_SCARLET, CHECK_CHAR_SCARLET_RECT)
        self.screen.blit(CHECK_CHAR_WHITE, CHECK_CHAR_WHITE_RECT)
        # Known Information Weapon Check Titles
        self.screen.blit(CHECK_WEAPON_CANDLESTICK, CHECK_WEAPON_CANDLESTICK_RECT)
        self.screen.blit(CHECK_WEAPON_KNIFE, CHECK_WEAPON_KNIFE_RECT)
        self.screen.blit(CHECK_WEAPON_LEAD_PIPE, CHECK_WEAPON_LEAD_PIPE_RECT)
        self.screen.blit(CHECK_WEAPON_REVOLVER, CHECK_WEAPON_REVOLVER_RECT)
        self.screen.blit(CHECK_WEAPON_ROPE, CHECK_WEAPON_ROPE_RECT)
        self.screen.blit(CHECK_WEAPON_WRENCH, CHECK_WEAPON_WRENCH_RECT)
        # Known Information Room Check Titles
        self.screen.blit(CHECK_ROOM_BALLROOM, CHECK_ROOM_BALLROOM_RECT)
        self.screen.blit(CHECK_ROOM_BILLIARD, CHECK_ROOM_BILLIARD_RECT)
        self.screen.blit(CHECK_ROOM_CONSERVATORY, CHECK_ROOM_CONSERVATORY_RECT)
        self.screen.blit(CHECK_ROOM_DINING_ROOM, CHECK_ROOM_DINING_ROOM_RECT)
        self.screen.blit(CHECK_ROOM_HALL, CHECK_ROOM_HALL_RECT)
        self.screen.blit(CHECK_ROOM_KITCHEN, CHECK_ROOM_KITCHEN_RECT)
        self.screen.blit(CHECK_ROOM_LIBRARY, CHECK_ROOM_LIBRARY_RECT)
        self.screen.blit(CHECK_ROOM_LOUNGE, CHECK_ROOM_LOUNGE_RECT)
        self.screen.blit(CHECK_ROOM_STUDY, CHECK_ROOM_STUDY_RECT)
        # Add Bottom Buttons
        self.screen.blit(END_TURN_BTN, END_TURN_RECT)
        self.screen.blit(MAKE_SUGGESTION_BTN, MAKE_SUGGESTION_RECT)
        self.screen.blit(MAKE_ACCUSATION_BTN, MAKE_ACCUSATION_RECT)
        self.all_sprites.draw(self.screen)
        pg.display.flip()



    def events(self):
        # All events caught here
        for event in pg.event.get():
            # Check for quit
            if event.type == pg.QUIT:
                logging.warning("Event type = QUIT (Terminal Ctrl + C // Window X Button)")
                self.quit()
            # Arrow Keys
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    print("Event key = ESCAPE")
                    logging.warning("Event key = ESCAPE pressed")
                    quitGame()
                if event.key == pg.K_LEFT:
                    logging.warning("Event key (player move) = LEFT pressed")
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    logging.warning("Event key (player move) = RIGHT pressed")
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    logging.warning("Event key (player move) = UP pressed")
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    logging.warning("Event key (player move) = DOWN pressed")
                    self.player.move(dy=1)
            # Button Clicks
            if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                mouseclick = pg.mouse.get_pressed()
                # Check if the user clicked on an option button
                if CREATE_GAME_RECT.collidepoint(pos) and mouseclick:
                    logging.warning('Clicked on Create Game Button')
                    sio.emit('create_room')
                    #self.screen.blit(PLAYER_ID, PLAYER_ID_RECT)
                elif JOIN_GAME_RECT.collidepoint(pos) and mouseclick:
                    logging.warning('Clicked on Join Game Button')
                    sio.emit('join_room')
                elif START_GAME_RECT.collidepoint(pos) and mouseclick:
                    logging.warning('Clicked on Start Game Button')
                    sio.emit('start_game')
                elif QUIT_GAME_RECT.collidepoint(pos) and mouseclick:
                    logging.warning('Clicked on Quit Game Button')
                    sio.disconnect()
                    logging.warning('Disconnected from the Server')
                    self.quit()
                    sys.exit()
                elif END_TURN_RECT.collidepoint(pos) and mouseclick:
                    logging.warning('Clicked on Finished With Turn / End Turn Button')
                    sio.emit('end_turn')
                elif MAKE_SUGGESTION_RECT.collidepoint(pos) and mouseclick:
                    logging.warning('Clicked on Make A Suggestion Button')
                    makeSuggestion(suspects, weapons, rooms)
                elif MAKE_ACCUSATION_RECT.collidepoint(pos) and mouseclick:
                    logging.warning('Clicked on Make An Accusation Button')
                    makeAccusation(suspects, weapons, rooms)
                # Buttons for Secret Passage Ways
                elif TO_KITCHEN_BTN_RECT.collidepoint(pos) and mouseclick:
                    logging.warning('Taking the passage way to the Kitchen')
                    passageToKitchen()
                elif TO_STUDY_BTN_RECT.collidepoint(pos) and mouseclick:
                    logging.warning('Taking the passage way to the Study')
                    passageToStudy()
                elif TO_CONSERVATORY_BTN_RECT.collidepoint(pos) and mouseclick:
                    logging.warning('Taking the passage way to the Conservatory')
                    passageToConservatory()
                elif TO_LOUNGE_BTN_RECT.collidepoint(pos) and mouseclick:
                    logging.warning('Taking the passage way to the Lounge')
                    passageToLounge()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# Main Method
def main():
    # Create the game object
    g = Game()
    g.show_start_screen()
    while True:
        g.new_board()
        g.run()
        g.show_go_screen()

if __name__ == '__main__':
    main()
