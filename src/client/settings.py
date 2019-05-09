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

# Known Information Section ----------------------------------------------------
KNOWN_INFO_SECTION_FONT = pg.font.Font('freesansbold.ttf', 15)
CHECK_FONT = pg.font.Font('freesansbold.ttf', 12)

# Shortcut Method for Displaying Buttons ! Needs to be before buttons!
def makeCheckBox(text, color, bgcolor, top, left):
    # Create the Surface and Rect objects for some text
    textSurf = TEXT_COLOR_PARAGRAPH_FONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.midleft = (top, left)
    return (textSurf, textRect)

# Characters
CHARACTERS_SECTION = KNOWN_INFO_SECTION_FONT.render('CHARACTERS', True, WHITE)
CHARACTERS_SECTION_RECT = CHARACTERS_SECTION.get_rect()
CHARACTERS_SECTION_RECT.midright = (885, 375)

# Reverend Green Name and Box
CHECK_CHAR_GREEN = CHECK_FONT.render('Reverend Green', True, WHITE)
CHECK_CHAR_GREEN_RECT = CHECK_CHAR_GREEN.get_rect()
CHECK_CHAR_GREEN_RECT.midleft = (800, 400)
CHECKBOX_GREEN, CHECKBOX_GREEN_RECT = makeButtonText('_', WHITE, RED, 775, 385)
CHECKBOX_GREEN_CHECKED, CHECKBOX_GREEN_CHECKED_RECT = makeButtonText('X', RED, WHITE, 775, 385)
# Colonel Mustard Name and Box
CHECK_CHAR_MUSTARD = CHECK_FONT.render('Colonel Mustard', True, WHITE)
CHECK_CHAR_MUSTARD_RECT = CHECK_CHAR_MUSTARD.get_rect()
CHECK_CHAR_MUSTARD_RECT.midleft = (800, 425)
CHECKBOX_MUSTARD, CHECKBOX_MUSTARD_RECT = makeButtonText('_', WHITE, RED, 775, 410)
CHECKBOX_MUSTARD_CHECKED, CHECKBOX_MUSTARD_CHECKED_RECT = makeButtonText('X', RED, WHITE, 775, 410)
# Mrs. Peacock Name and Box
CHECK_CHAR_PEACOCK = CHECK_FONT.render('Mrs. Peacock', True, WHITE)
CHECK_CHAR_PEACOCK_RECT = CHECK_CHAR_PEACOCK.get_rect()
CHECK_CHAR_PEACOCK_RECT.midleft = (800, 450)
CHECKBOX_PEACOCK, CHECKBOX_PEACOCK_RECT = makeButtonText('_', WHITE, RED, 775, 435)
CHECKBOX_PEACOCK_CHECKED, CHECKBOX_PEACOCK_CHECKED_RECT = makeButtonText('X', RED, WHITE, 775, 435)
# Professor Plum Name and Box
CHECK_CHAR_PLUM = CHECK_FONT.render('Professor Plum', True, WHITE)
CHECK_CHAR_PLUM_RECT = CHECK_CHAR_PLUM.get_rect()
CHECK_CHAR_PLUM_RECT.midleft = (800, 475)
CHECKBOX_PLUM, CHECKBOX_PLUM_RECT = makeButtonText('_', WHITE, RED, 775, 460)
CHECKBOX_PLUM_CHECKED, CHECKBOX_PLUM_CHECKED_RECT = makeButtonText('X', RED, WHITE, 775, 460)
# Miss Scarlet Name and Box
CHECK_CHAR_SCARLET = CHECK_FONT.render('Mrs. Scarlet', True, WHITE)
CHECK_CHAR_SCARLET_RECT = CHECK_CHAR_SCARLET.get_rect()
CHECK_CHAR_SCARLET_RECT.midleft = (800, 500)
CHECKBOX_SCARLET, CHECKBOX_SCARLET_RECT = makeButtonText('_', WHITE, RED, 775, 485)
CHECKBOX_SCARLET_CHECKED, CHECKBOX_SCARLET_CHECKED_RECT = makeButtonText('X', RED, WHITE, 775, 485)
# Mrs. White Name and Box
CHECK_CHAR_WHITE = CHECK_FONT.render('Mr. White', True, WHITE)
CHECK_CHAR_WHITE_RECT = CHECK_CHAR_WHITE.get_rect()
CHECK_CHAR_WHITE_RECT.midleft = (800, 525)
CHECKBOX_WHITE, CHECKBOX_WHITE_RECT = makeButtonText('_', WHITE, RED, 775, 510)
CHECKBOX_WHITE_CHECKED, CHECKBOX_WHITE_CHECKED_RECT = makeButtonText('X', RED, WHITE, 775, 510)

# Weapons
WEAPONS_SECTION = KNOWN_INFO_SECTION_FONT.render('WEAPONS', True, WHITE)
WEAPONS_SECTION_RECT = WEAPONS_SECTION.get_rect()
WEAPONS_SECTION_RECT.midright = (1100, 375)

# Candlestick
CHECK_WEAPON_CANDLESTICK = CHECK_FONT.render('Candlestick', True, WHITE)
CHECK_WEAPON_CANDLESTICK_RECT = CHECK_WEAPON_CANDLESTICK.get_rect()
CHECK_WEAPON_CANDLESTICK_RECT.midleft = (1030, 400)
CHECKBOX_CANDLESTICK, CHECKBOX_CANDLESTICK_RECT = makeButtonText('_', WHITE, RED, 1010, 385)
CHECKBOX_CANDLESTICK_CHECKED, CHECKBOX_CANDLESTICK_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1010, 385)
# Knife
CHECK_WEAPON_KNIFE = CHECK_FONT.render('Knife', True, WHITE)
CHECK_WEAPON_KNIFE_RECT = CHECK_WEAPON_KNIFE.get_rect()
CHECK_WEAPON_KNIFE_RECT.midleft = (1030, 425)
CHECKBOX_KNIFE, CHECKBOX_KNIFE_RECT = makeButtonText('_', WHITE, RED, 1010, 410)
CHECKBOX_KNIFE_CHECKED, CHECKBOX_KNIFE_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1010, 410)
# Lead Pipe
CHECK_WEAPON_LEAD_PIPE = CHECK_FONT.render('Lead Pipe', True, WHITE)
CHECK_WEAPON_LEAD_PIPE_RECT = CHECK_WEAPON_LEAD_PIPE.get_rect()
CHECK_WEAPON_LEAD_PIPE_RECT.midleft = (1030, 450)
CHECKBOX_LEAD_PIPE, CHECKBOX_LEAD_PIPE_RECT = makeButtonText('_', WHITE, RED, 1010, 435)
CHECKBOX_LEAD_PIPE_CHECKED, CHECKBOX_LEAD_PIPE_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1010, 435)
# Revolver
CHECK_WEAPON_REVOLVER = CHECK_FONT.render('Revolver', True, WHITE)
CHECK_WEAPON_REVOLVER_RECT = CHECK_WEAPON_REVOLVER.get_rect()
CHECK_WEAPON_REVOLVER_RECT.midleft = (1030, 475)
CHECKBOX_REVOLVER, CHECKBOX_REVOLVER_RECT = makeButtonText('_', WHITE, RED, 1010, 460)
CHECKBOX_REVOLVER_CHECKED, CHECKBOX_REVOLVER_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1010, 460)
# Rope
CHECK_WEAPON_ROPE = CHECK_FONT.render('Rope', True, WHITE)
CHECK_WEAPON_ROPE_RECT = CHECK_WEAPON_ROPE.get_rect()
CHECK_WEAPON_ROPE_RECT.midleft = (1030, 500)
CHECKBOX_ROPE, CHECKBOX_ROPE_RECT = makeButtonText('_', WHITE, RED, 1010, 485)
CHECKBOX_ROPE_CHECKED, CHECKBOX_ROPE_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1010, 485)
# Wrench
CHECK_WEAPON_WRENCH = CHECK_FONT.render('Wrench', True, WHITE)
CHECK_WEAPON_WRENCH_RECT = CHECK_WEAPON_WRENCH.get_rect()
CHECK_WEAPON_WRENCH_RECT.midleft = (1030, 525)
CHECKBOX_WRENCH, CHECKBOX_WRENCH_RECT = makeButtonText('_', WHITE, RED, 1010, 510)
CHECKBOX_WRENCH_CHECKED, CHECKBOX_WRENCH_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1010, 510)

# Rooms
ROOMS_SECTION = KNOWN_INFO_SECTION_FONT.render('ROOMS', True, WHITE)
ROOMS_SECTION_RECT = ROOMS_SECTION.get_rect()
ROOMS_SECTION_RECT.midright = (1310, 375)

# Ballroom
CHECK_ROOM_BALLROOM = CHECK_FONT.render('Ballroom', True, WHITE)
CHECK_ROOM_BALLROOM_RECT = CHECK_ROOM_BALLROOM.get_rect()
CHECK_ROOM_BALLROOM_RECT.midleft = (1270, 400)
CHECKBOX_BALLROOM, CHECKBOX_BALLROOM_RECT = makeButtonText('_', WHITE, RED, 1250, 385)
CHECKBOX_BALLROOM_CHECKED, CHECKBOX_BALLROOM_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1250, 385)
# Billiard room
CHECK_ROOM_BILLIARD = CHECK_FONT.render('Billiard', True, WHITE)
CHECK_ROOM_BILLIARD_RECT = CHECK_ROOM_BILLIARD.get_rect()
CHECK_ROOM_BILLIARD_RECT.midleft = (1270, 425)
CHECKBOX_BILLIARD, CHECKBOX_BILLIARD_RECT = makeButtonText('_', WHITE, RED, 1250, 410)
CHECKBOX_BILLIARD_CHECKED, CHECKBOX_BILLIARD_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1250, 410)
# Conservatory
CHECK_ROOM_CONSERVATORY = CHECK_FONT.render('Conservatory', True, WHITE)
CHECK_ROOM_CONSERVATORY_RECT = CHECK_ROOM_CONSERVATORY.get_rect()
CHECK_ROOM_CONSERVATORY_RECT.midleft = (1270, 450)
CHECKBOX_CONSERVATORY, CHECKBOX_CONSERVATORY_RECT = makeButtonText('_', WHITE, RED, 1250, 435)
CHECKBOX_CONSERVATORY_CHECKED, CHECKBOX_CONSERVATORY_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1250, 435)
# Dining room
CHECK_ROOM_DINING_ROOM = CHECK_FONT.render('Dining Room', True, WHITE)
CHECK_ROOM_DINING_ROOM_RECT = CHECK_ROOM_DINING_ROOM.get_rect()
CHECK_ROOM_DINING_ROOM_RECT.midleft = (1270, 475)
CHECKBOX_DINING_ROOM, CHECKBOX_DINING_ROOM_RECT = makeButtonText('_', WHITE, RED, 1250, 460)
CHECKBOX_DINING_ROOM_CHECKED, CHECKBOX_DINING_ROOM_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1250, 460)
# Hall
CHECK_ROOM_HALL = CHECK_FONT.render('Hall', True, WHITE)
CHECK_ROOM_HALL_RECT = CHECK_ROOM_HALL.get_rect()
CHECK_ROOM_HALL_RECT.midleft = (1270, 500)
CHECKBOX_HALL, CHECKBOX_HALL_RECT = makeButtonText('_', WHITE, RED, 1250, 485)
CHECKBOX_HALL_CHECKED, CHECKBOX_HALL_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1250, 485)
# Kitchen
CHECK_ROOM_KITCHEN = CHECK_FONT.render('Kitchen', True, WHITE)
CHECK_ROOM_KITCHEN_RECT = CHECK_ROOM_KITCHEN.get_rect()
CHECK_ROOM_KITCHEN_RECT.midleft = (1270, 525)
CHECKBOX_KITCHEN, CHECKBOX_KITCHEN_RECT = makeButtonText('_', WHITE, RED, 1250, 510)
CHECKBOX_KITCHEN_CHECKED, CHECKBOX_KITCHEN_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1250, 510)
# Library
CHECK_ROOM_LIBRARY = CHECK_FONT.render('Library', True, WHITE)
CHECK_ROOM_LIBRARY_RECT = CHECK_ROOM_LIBRARY.get_rect()
CHECK_ROOM_LIBRARY_RECT.midleft = (1270, 550)
CHECKBOX_LIBRARY, CHECKBOX_LIBRARY_RECT = makeButtonText('_', WHITE, RED, 1250, 535)
CHECKBOX_LIBRARY_CHECKED, CHECKBOX_LIBRARY_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1250, 535)
# Lounge
CHECK_ROOM_LOUNGE = CHECK_FONT.render('Lounge', True, WHITE)
CHECK_ROOM_LOUNGE_RECT = CHECK_ROOM_LOUNGE.get_rect()
CHECK_ROOM_LOUNGE_RECT.midleft = (1270, 575)
CHECKBOX_LOUNGE, CHECKBOX_LOUNGE_RECT = makeButtonText('_', WHITE, RED, 1250, 560)
CHECKBOX_LOUNGE_CHECKED, CHECKBOX_LOUNGE_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1250, 560)
# Study
CHECK_ROOM_STUDY = CHECK_FONT.render('Study', True, WHITE)
CHECK_ROOM_STUDY_RECT = CHECK_ROOM_STUDY.get_rect()
CHECK_ROOM_STUDY_RECT.midleft = (1270, 600)
CHECKBOX_STUDY, CHECKBOX_STUDY_RECT = makeButtonText('_', WHITE, RED, 1250, 585)
CHECKBOX_STUDY_CHECKED, CHECKBOX_STUDY_CHECKED_RECT = makeButtonText('X', RED, WHITE, 1250, 585)

# Even do this?
# MOVE_UP_BTN
# MOVE_DOWN_BTN
# MOVE_LEFT_BTN
# MOVE_RIGHT_BTN
