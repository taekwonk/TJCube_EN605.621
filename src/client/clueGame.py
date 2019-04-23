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

import pygame as pg
import logging
import sys
from os import path

from settings import *
from sprites import *
from settings import *
from characters import *
from weapons import *
from rooms import *
from buttons import *

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
        self.screen = WINDOW_SET
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        logging.warning("Setting up basic configurations.")

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)        
        logging.warning("Loading the board map.")

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '0':
                    Wall(self, col, row)
                if tile == '1':
                    self.player = Player(self, col, row, RED)
        logging.warning("Set up for a new game.")

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
        # Title in right side of window
        self.screen.blit(GAME_HEADER, GAME_HEADER_RECT)
        # Add Top Buttons
        self.screen.blit(CREATE_GAME_BTN, CREATE_GAME_RECT)
        self.screen.blit(JOIN_GAME_BTN, JOIN_GAME_RECT)
        self.screen.blit(START_GAME_BTN, START_GAME_RECT)
        self.screen.blit(QUIT_GAME_BTN, QUIT_GAME_RECT)
        # Add Bottom Buttons
        self.screen.blit(END_TURN_BTN, END_TURN_RECT)
        self.screen.blit(MAKE_SUGGESTION_BTN, MAKE_SUGGESTION_RECT)
        self.screen.blit(MAKE_ACCUSATION_BTN, MAKE_ACCUSATION_RECT)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
           
    def events(self):
        # catch all events here
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
                    self.quit()
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
                    # Call desired function
                    createGame()
                    # Log to file / command line
                    logging.warning('Clicked on Create Game Button')
                elif JOIN_GAME_RECT.collidepoint(pos) and mouseclick:
                    # Call desired function
                    joinGame()
                    logging.warning('Clicked on Join Game Button')
                elif START_GAME_RECT.collidepoint(pos) and mouseclick:
                    # Call desired function
                    startGame()
                    logging.warning('Clicked on Start Game Button')
                elif QUIT_GAME_RECT.collidepoint(pos) and mouseclick:
                    # Call desired function
                    quitGame()
                    logging.warning('Clicked on Quit Game Button')
                elif END_TURN_RECT.collidepoint(pos) and mouseclick:
                    # Call desired function
                    endTurn()
                    logging.warning('Clicked on Finished With Turn / End Turn Button')
                elif MAKE_SUGGESTION_RECT.collidepoint(pos) and mouseclick:
                    # Call desired function
                    makeSuggestion()
                    logging.warning('Clicked on Make A Suggestion Button')
                elif MAKE_ACCUSATION_RECT.collidepoint(pos) and mouseclick:
                    # Call desired function
                    makeAccusation()
                    logging.warning('Clicked on Make An Accusation Button')


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
        g.new()
        g.run()
        g.show_go_screen()

if __name__ == '__main__':
    main()
