# Johns Hopkins University - Whiting School of Engineering
# Engineering for Professionals
# Spring 2019 - Foundations of Software Engineering
# TJ^3 Project Group
#
# This page was last modified (4.23.2019) by Jenna S. Nuth
# Coding with Atom (=
#
# References:
# https://youtu.be/ajR4BZBKTr4
# https://inventwithpython.com/makinggames.pdf
# https://www.raywenderlich.com/2614-multiplayer-game-programming-for-teens-with-python-part-1
#
# SETTINGS

import pygame as pg

# Init Font
pg.font.init()

# RGB Colors             R      G       B
WHITE        =   (   255,    255,    255  )
BLACK        =   (   0,      0,      0    )
OFF_BLACK    =   (   5,      5,      5    )
RED          =   (   128,    0,      0    )
GREEN        =   (   0,      155,    0    )
BLUE         =   (   0,      0,      128  )
BROWN        =   (   174,    94,     0    )
YELLOW       =   (   255,    255,    0    )
GREEN        =   (   0,      128,    0    )
GRAY         =   (   128,    128,    128  )
PURPLE       =   (   128,    0,      128  )
LIGHT_BLUE   =   (   100,    130,    200  )
LIGHT_GRAY   =   (   100,    100,    100  )
DARK_GRAY    =   (   30,     30,     30   )
ROOMS_GRAY   =   (   50,     50,     50   )
HALLS_GRAY   =   (   75,     75,     75   )
DARK_RED     =   (   76,     15,     15   )


# Game Settings
WINDOW_WIDTH = 1450   # 16 * 64 or 32 * 32 or 64 * 16
WINDOW_HEIGHT = 750  # 16 * 48 or 32 * 24 or 64 * 12
WINDOW_SET = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60
TITLE = "TJ^3 Clueless"
BGCOLOR = BLACK

# Board Settings
BOARD_WIDTH = 400
BOARD_HEIGHT = 400
TILE_SIZE = 60
GRID_WIDTH = BOARD_WIDTH / TILE_SIZE
GRID_HEIGHT = BOARD_HEIGHT / TILE_SIZE

# Amount of space on the left & right side (X_MARGIN) or above and below
# (Y_MARGIN) the game board, in pixels
X_MARGIN = int((WINDOW_WIDTH - (BOARD_WIDTH * TILE_SIZE)) / 2)
Y_MARGIN = int(WINDOW_HEIGHT - (BOARD_HEIGHT * TILE_SIZE) / 2)

# GUI Feature Color Key
BG_COLOR_WINDOW = OFF_BLACK
BG_COLOR_INFO_PANE = LIGHT_BLUE
BOARD_GRID_LINE_COLOR = WHITE
BTN_BG_COLOR = RED

# HEADERS -----------------------------

# Game Header
# Font Style Key (object.render('TEXT', True, color))
GAME_HEADER_FONT = pg.font.Font('freesansbold.ttf', 50)
GAME_HEADER = GAME_HEADER_FONT.render('CLUE', True, RED)
GAME_HEADER_RECT = GAME_HEADER.get_rect()
GAME_HEADER_RECT.midright = (1125, 50)

# Player Identification Section Header
PLAYER_ID_HEADER_FONT = pg.font.Font('freesansbold.ttf', 35)
PLAYER_ID_HEADER = PLAYER_ID_HEADER_FONT.render('PLAYER :', True, RED)
PLAYER_ID_HEADER_RECT = PLAYER_ID_HEADER.get_rect()
PLAYER_ID_HEADER_RECT.midleft = (125, 50)

# Your Cards Section Header
YOUR_CARDS_HEADER_FONT = pg.font.Font('freesansbold.ttf', 25)
YOUR_CARDS_HEADER = YOUR_CARDS_HEADER_FONT.render('Your Cards', True, RED)
YOUR_CARDS_HEADER_RECT = YOUR_CARDS_HEADER.get_rect()
YOUR_CARDS_HEADER_RECT.midright = (1130, 160)

# Player Turn Section Header
PLAYER_TURN_HEADER_FONT = pg.font.Font('freesansbold.ttf', 50)
PLAYER_TURN_HEADER = PLAYER_TURN_HEADER_FONT.render('TURN :', True, RED)
PLAYER_TURN_HEADER_RECT = PLAYER_TURN_HEADER.get_rect()
PLAYER_TURN_HEADER_RECT.midleft = (100, 625)

# Known Information Section Header
KNOWN_INFO_HEADER_FONT = pg.font.Font('freesansbold.ttf', 25)
KNOWN_INFO_HEADER = KNOWN_INFO_HEADER_FONT.render('Known Information', True, RED)
KNOWN_INFO_HEADER_RECT = KNOWN_INFO_HEADER.get_rect()
KNOWN_INFO_HEADER_RECT.midright = (1185, 315)

# GENERAL SETTINGS --------------------

# General Font Style Key
TEXT_HEADER_FONT = pg.font.Font('freesansbold.ttf', 32)
TEXT_COLOR_PARAGRAPH_FONT = pg.font.Font('freesansbold.ttf', 18)

# Tile Status
FREE_TILE = 'FREE_TILE' # arbitrary but unique value
BLOCKED_TILE = 'BLOCKED_TILE' # arbitrary but unique value
TAKEN_TILE = 'TAKEN_TILE' # arbitrary but unique value
# ANIMATION_SPEED = 20 # integer from 1 to 100, higher is faster animation

# Images

# Sounds

# BUTTONS ----------------------------

# Shortcut Method for Displaying Buttons ! Needs to be before buttons!
def makeButtonText(text, color, bgcolor, top, left):
    # Create the Surface and Rect objects for some text
    textSurf = TEXT_COLOR_PARAGRAPH_FONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

# Board Buttons
# -- Top Menu Options
CREATE_GAME_BTN, CREATE_GAME_RECT = makeButtonText('Create Game', WHITE, RED, 775, 100)
JOIN_GAME_BTN, JOIN_GAME_RECT = makeButtonText('Join Game', WHITE, RED, 950, 100)
START_GAME_BTN, START_GAME_RECT = makeButtonText('Start Game', WHITE, RED, 1100, 100)
QUIT_GAME_BTN, QUIT_GAME_RECT = makeButtonText('Quit Game', WHITE, RED, 1250, 100)
# -- Player Action Items
END_TURN_BTN, END_TURN_RECT = makeButtonText('Finish With Turn', WHITE, RED, 750, 650)
MAKE_SUGGESTION_BTN, MAKE_SUGGESTION_RECT = makeButtonText('Make A Suggestion', WHITE, RED, 950, 650)
MAKE_ACCUSATION_BTN, MAKE_ACCUSATION_RECT = makeButtonText('Make An Accusation', WHITE, RED, 1175, 650)

# INFORMATION DISPLAYS ------------------------------

# Player Identification Section

# Cards Display Section
CARD_FONT = pg.font.Font('freesansbold.ttf', 15)
# Card 1
CARD_1 = CARD_FONT.render('Card 1', True, WHITE)
CARD_1_RECT = CARD_1.get_rect()
CARD_1_RECT.midright = (785, 215)
# Card 2
CARD_2 = CARD_FONT.render('Card 2', True, WHITE)
CARD_2_RECT = CARD_2.get_rect()
CARD_2_RECT.midright = (860, 215)
# Card 3
CARD_3 = CARD_FONT.render('Card 3', True, WHITE)
CARD_3_RECT = CARD_3.get_rect()
CARD_3_RECT.midright = (935, 215)
# Card 4
CARD_4 = CARD_FONT.render('Card 4', True, WHITE)
CARD_4_RECT = CARD_4.get_rect()
CARD_4_RECT.midright = (1010, 215)
# Card 5
CARD_5 = CARD_FONT.render('Card 5', True, WHITE)
CARD_5_RECT = CARD_5.get_rect()
CARD_5_RECT.midright = (1085, 215)
# Card 6
CARD_6 = CARD_FONT.render('Card 6', True, WHITE)
CARD_6_RECT = CARD_6.get_rect()
CARD_6_RECT.midright = (1160, 215)
# Card 7
CARD_7 = CARD_FONT.render('Card 7', True, WHITE)
CARD_7_RECT = CARD_7.get_rect()
CARD_7_RECT.midright = (1235, 215)
# Card 8
CARD_8 = CARD_FONT.render('Card 8', True, WHITE)
CARD_8_RECT = CARD_8.get_rect()
CARD_8_RECT.midright = (1310, 215)
# Card 9
CARD_9 = CARD_FONT.render('Card 9', True, WHITE)
CARD_9_RECT = CARD_9.get_rect()
CARD_9_RECT.midright = (1385, 215)

# Player Turn Section

# Known Information Section
KNOWN_INFO_SECTION_FONT = pg.font.Font('freesansbold.ttf', 15)
# Characters
CHARACTERS_SECTION = KNOWN_INFO_SECTION_FONT.render('CHARACTERS', True, WHITE)
CHARACTERS_SECTION_RECT = CHARACTERS_SECTION.get_rect()
CHARACTERS_SECTION_RECT.midright = (885, 375)
# Weapons
WEAPONS_SECTION = KNOWN_INFO_SECTION_FONT.render('WEAPONS', True, WHITE)
WEAPONS_SECTION_RECT = WEAPONS_SECTION.get_rect()
WEAPONS_SECTION_RECT.midright = (1100, 375)
# Rooms
ROOMS_SECTION = KNOWN_INFO_SECTION_FONT.render('ROOMS', True, WHITE)
ROOMS_SECTION_RECT = ROOMS_SECTION.get_rect()
ROOMS_SECTION_RECT.midright = (1310, 375)

# Even do this?
# MOVE_UP_BTN
# MOVE_DOWN_BTN
# MOVE_LEFT_BTN
# MOVE_RIGHT_BTN
