# Johns Hopkins University - Whiting School of Engineering
# Engineering for Professionals
# Spring 2019 - Foundations of Software Engineering
# TJ^3 Project Group
#
# This page was last modified (4.19.2019) by Jenna S. Nuth
# Coding with Atom (=
#
# References:
# https://youtu.be/ajR4BZBKTr4
# https://inventwithpython.com/makinggames.pdf
# https://www.raywenderlich.com/2614-multiplayer-game-programming-for-teens-with-python-part-1
#
# SETTINGS

import pygame as pg

# RGB Colors          R      G       B
WHITE       =   (   255,    255,    255 )
BLACK       =   (   0,      0,      0    )
RED         =   (   128,    0,      0    )
GREEN       =   (   0,      155,    0    )
BLUE        =   (   0,      0,      128  )
BROWN       =   (   174,    94,     0    )
YELLOW      =   (   255,    255,    0    )
GREEN       =   (   0,      128,    0    )
GRAY        =   (   128,    128,    128  )
PURPLE      =   (   128,    0,      128  )
LIGHT_BLUE  =   (   100,    130,    200  )
DARKGREY    =   (   40,     40,     40   )
LIGHTGREY   =   (   100,    100,    100  )


# Game Settings
WINDOW_WIDTH = 1500   # 16 * 64 or 32 * 32 or 64 * 16
WINDOW_HEIGHT = 700  # 16 * 48 or 32 * 24 or 64 * 12
WINDOW_SET = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
FPS = 60
TITLE = "Clue Mod"
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
BG_COLOR_WINDOW = BLACK
BG_COLOR_INFO_PANE = LIGHT_BLUE
BOARD_GRID_LINE_COLOR = WHITE

# Font Style Key (object.render('TEXT', True, color))
pg.font.init()
TEXT_HEADER_FONT = pg.font.Font('freesansbold.ttf', 32)
TEXT_COLOR_PARAGRAPH_FONT = pg.font.Font('freesansbold.ttf', 18)
GAME_HEADER_FONT = pg.font.Font('freesansbold.ttf', 50)
GAME_HEADER = GAME_HEADER_FONT.render('CLUE', True, RED)
GAME_HEADER_RECT = GAME_HEADER.get_rect()
GAME_HEADER_RECT.midright = (1200, 50)

# Tile Status
FREE_TILE = 'FREE_TILE' # arbitrary but unique value
BLOCKED_TILE = 'BLOCKED_TILE' # arbitrary but unique value
TAKEN_TILE = 'TAKEN_TILE' # arbitrary but unique value
# ANIMATION_SPEED = 20 # integer from 1 to 100, higher is faster animation

# Images

# Sounds
