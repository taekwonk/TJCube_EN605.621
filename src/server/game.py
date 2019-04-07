#game logic
from model.tile import Tile
from model.tile_type import TileType
import board
import player

class Game:
    def __init__(self):
        #initialize game variables
        #game objects, etc...
        self.board = Board()

        self.players = []
        self.started = false
        self.current_player_index = 0
        self.case_file = {}
        self.suspects = ["Colonel Mustard", "Miss Scarlet", "Professor Plum", "Mr. Green", "Mrs. White", "Mrs. Peacock"]


    def initialize_game(self):
        #create cards, shuffle and put 1 of each type to case file
        #shuffle all cards and deal to each player
        #place players to appropriate positions
        pass
    
    def add_player(self, sid, name):
        if(len(self.players) < 6):
            player = Player(sid, name)
            self.players.append(player)
            return self.suspects[len(self.players)-1]

        else:
            return None

    def joinable(self):
        return !self.started && len(self.players) < 6

    def start_game(self):
        self.started = true
        self.initialize_game()
        #TODO: give player turn


    #other game logic

    


    
