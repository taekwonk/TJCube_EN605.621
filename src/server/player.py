class Player:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.cards = None
        self.location = None
        self.disabled = False

        self.moved = False
        self.suggested = False


    def initialize(self, cards, location):
        self.cards = cards
        self.location = location

    def move(self, position):
        pass
    
    def suggest(self, data):
        pass
    
    def accuse(self, data):
        pass

    