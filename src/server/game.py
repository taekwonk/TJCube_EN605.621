#game logic

class Game:
    def __init__(self):
        #initialize game variables
        self.players = {}
        #game objects, etc...
        self.started = false

        self.initialize_board()

    def initialize_board(self):
        pass
    
    def add_player(self, sid, name):
        if(len(self.players) < 9):
            self.players[sid] = name
            return true

        else:
            return false

    def joinable(self):
        return !self.started && len(self.players) < 9

    def start_game(self):
        self.started = true


    #other game logic

    


    
