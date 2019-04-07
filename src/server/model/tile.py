#space in the board
class Tile:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.connected = []

    def set_connected(self, arr):
        self.connected = arr

    def get_connected(self)
        return self.connected