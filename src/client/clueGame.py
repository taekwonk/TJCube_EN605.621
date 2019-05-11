# Johns Hopkins University - Whiting School of Engineering
# Engineering for Professionals
# Spring 2019 - Foundations of Software Engineering
# TJ^3 Project Group
#
# This page was last modified (4.23.2019) by Jenna S. Nuth
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
# CHECKLIST:
# on_room_created
# on_joined_game
# on_game_started
# on_moved
# on_start_turn
#
# Block tile when token leaves it
# Multi-client connected to different players
#
# http://www.mechanicalcat.net/richard/log/Python/PyGame_sample__drawing_a_map__and_moving_around_it
#

import pygame as pg
import logging
import sys
import socketio

from os import path
from settings import *
from sprites import *
from settings import *
from characters import *
from weapons import *
from rooms import *
from buttons import *
from logic import *

# Set up the Server-Client Connection
sio = socketio.Client()
sio.connect('http://localhost:5000')

clientNumber = 0
hand = 0

suspects = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Mrs. White", "Colonel Mustard"]
weapons = ["Rope", "Lead Pipe", "Knife", "Wrench", "Candlestick", "Revolver"]
rooms = ["Study", "Hall", "Lounge", "Library", "Billiard Room", "Dining Room", "Conservatory", "Ballroom", "Kitchen"]

player1 = suspects[0]
player2 = suspects[1]
player3 = suspects[2]
player4 = suspects[3]
player5 = suspects[4]
player6 = suspects[5]

class Game:

    # Create a real-time log
    log = logging.getLogger()
    # Make log print to the console
    console = logging.StreamHandler()
    log.addHandler(console)
    # Emit a warning to the humans
    # Not sure if there is a better one than warning as info doesn't print log
    log.warning('Winter is Here')

    def __init__(self):
        pg.init()
        self.players = []
        self.screen = WINDOW_SET
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat() # 1 move per key press
        self.load_data()
        logging.warning("Setting up basic configurations.")
        self.all_sprites = pg.sprite.Group()

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
        logging.warning("Loading the board map.")

    def new_board(self):
        # initialize all variables and do all the setup for a new game
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
                if tile == 'S':
                    self.player = Player(self, col, row, RED, player1)
                # --- Player2 = Mustard
                if tile == 'M':
                    self.player = Player(self, col, row, YELLOW, player2)
                # --- Player3 = White
                if tile == 'W':
                    self.player = Player(self, col, row, WHITE, player3)
                # --- Player4 = Green
                if tile == 'G':
                    self.player = Player(self, col, row, GREEN, player4)
                # --- Player5 = Peacock
                if tile == 'B':
                    self.player = Player(self, col, row, BLUE, player5)
                # --- Player6 = Plum
                if tile == 'P':
                    self.player = Player(self, col, row, PURPLE, player6)

        logging.warning("Set up board for a new game.")


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
        # Cards Display Boxes (Y at 200)
        pg.draw.rect(WINDOW_SET, RED, (725,200, 675, 75))
        pg.draw.line(WINDOW_SET, BLACK, (800,200), (800,275), 5)
        pg.draw.line(WINDOW_SET, BLACK, (875,200), (875,275), 5)
        pg.draw.line(WINDOW_SET, BLACK, (950,200), (950,275), 5)
        pg.draw.line(WINDOW_SET, BLACK, (1025,200), (1025,275), 5)
        pg.draw.line(WINDOW_SET, BLACK, (1100,200), (1100,275), 5)
        pg.draw.line(WINDOW_SET, BLACK, (1175,200), (1175,275), 5)
        pg.draw.line(WINDOW_SET, BLACK, (1250,200), (1250,275), 5)
        pg.draw.line(WINDOW_SET, BLACK, (1325,200), (1325,275), 5)
        pg.draw.line(WINDOW_SET, BLACK, (1400,200), (1400,275), 5)
        # Cards Display Titles
        self.screen.blit(CARD_1, CARD_1_RECT)
        self.screen.blit(CARD_2, CARD_2_RECT)
        self.screen.blit(CARD_3, CARD_3_RECT)
        self.screen.blit(CARD_4, CARD_4_RECT)
        self.screen.blit(CARD_5, CARD_5_RECT)
        self.screen.blit(CARD_6, CARD_6_RECT)
        self.screen.blit(CARD_7, CARD_7_RECT)
        self.screen.blit(CARD_8, CARD_8_RECT)
        self.screen.blit(CARD_9, CARD_9_RECT)
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
        # Checks
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
                    sio.emit('create_game')
                    logging.warning('Clicked on Create Game Button')
                elif JOIN_GAME_RECT.collidepoint(pos) and mouseclick:
                    sio.emit('join_room')
                    logging.warning('Clicked on Join Game Button')
                elif START_GAME_RECT.collidepoint(pos) and mouseclick:
                    sio.emit('start_game')
                    logging.warning('Clicked on Start Game Button')
                elif QUIT_GAME_RECT.collidepoint(pos) and mouseclick:
                    sio.disconnect()
                    logging.warning('Disconnected from the Server')
                    logging.warning('Clicking on Quit Game Button')
                    self.quit()
                    sys.exit()
                elif END_TURN_RECT.collidepoint(pos) and mouseclick:
                    sio.emit('end_turn')
                    logging.warning('Clicked on Finished With Turn / End Turn Button')
                elif MAKE_SUGGESTION_RECT.collidepoint(pos) and mouseclick:
                    makeSuggestion()
                    logging.warning('Clicked on Make A Suggestion Button')
                elif MAKE_ACCUSATION_RECT.collidepoint(pos) and mouseclick:
                    makeAccusation()
                    logging.warning('Clicked on Make An Accusation Button')
                # Buttons for Secret Passage Ways
                elif TO_KITCHEN_BTN_RECT.collidepoint(pos) and mouseclick:
                    passageToKitchen()
                    logging.warning('Taking the passage way to the Kitchen')
                elif TO_STUDY_BTN_RECT.collidepoint(pos) and mouseclick:
                    passageToStudy()
                    logging.warning('Taking the passage way to the Study')
                elif TO_CONSERVATORY_BTN_RECT.collidepoint(pos) and mouseclick:
                    passageToConservatory()
                    logging.warning('Taking the passage way to the Conservatory')
                elif TO_LOUNGE_BTN_RECT.collidepoint(pos) and mouseclick:
                    passageToLounge()
                    logging.warning('Taking the passage way to the Lounge')

                # Checkboxes - currently being overwritten so need to save state...
                elif CHECKBOX_GREEN_RECT.collidepoint(pos) and mouseclick:
                    GREEN_BOX=(CHECKBOX_GREEN_CHECKED, CHECKBOX_GREEN_CHECKED_RECT)
                    logging.warning('Checked GREEN')
                elif CHECKBOX_GREEN_CHECKED_RECT.collidepoint(pos) and mouseclick:
                    self.screen.blit(CHECKBOX_GREEN, CHECKBOX_GREEN_RECT)
                    logging.warning('Unchecked GREEN')

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
