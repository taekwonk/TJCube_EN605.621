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

# Game Header
# Font Style Key (object.render('TEXT', True, color))
GAME_HEADER_FONT = pg.font.Font('freesansbold.ttf', 50)
GAME_HEADER = GAME_HEADER_FONT.render('CLUE', True, RED)
GAME_HEADER_RECT = GAME_HEADER.get_rect()
GAME_HEADER_RECT.midright = (1125, 50)

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

# MOVE_UP_BTN
# MOVE_DOWN_BTN
# MOVE_LEFT_BTN
# MOVE_RIGHT_BTN
