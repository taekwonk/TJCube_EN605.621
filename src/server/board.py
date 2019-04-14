from model.tile import Tile
from model.tile_type import TileType

class Board:
    def __init__(self):
        study = Tile("Study", TileType.ROOM)
        hall = Tile("Hall", TileType.ROOM)
        lounge = Tile("Lounge", TileType.ROOM)
        library = Tile("Library", TileType.ROOM)
        billiard = Tile("Billiard Room", TileType.ROOM)
        dining = Tile("Dining Room", TileType.ROOM)
        conservatory = Tile("Conservatory", TileType.ROOM)
        ball = Tile("Ball Room", TileType.ROOM)
        kitchen = Tile("Kitchen", TileType.ROOM)

        h_sh = Tile("h_sh", TileType.HALLWAY) #hallway between 'S'tudy and 'H'all
        h_hl = Tile("h_hl", TileType.HALLWAY)
        h_sl = Tile("h_sl", TileType.HALLWAY)
        h_hb = Tile("h_hb", TileType.HALLWAY)
        h_ld = Tile("h_ld", TileType.HALLWAY)
        h_lb = Tile("h_lb", TileType.HALLWAY)
        h_bd = Tile("h_bd", TileType.HALLWAY)
        h_lc = Tile("h_lc", TileType.HALLWAY)
        h_bb = Tile("h_bb", TileType.HALLWAY)
        h_dk = Tile("h_dk", TileType.HALLWAY)
        h_cb = Tile("h_cb", TileType.HALLWAY)
        h_bk = Tile("h_bk", TileType.HALLWAY)

        study.set_connected([h_sh, h_sl, kitchen])
        #TODO: add all connections

        self.board = [study, hall, lounge, library, billiard, dining, conservatory, ball, kitchen, 
                        h_sh, h_hl, h_sl, h_hb, h_ld, h_lb, h_bd, h_lc, h_bb, h_dk, h_cb, h_bk]

    def get_tile(self, name):
        return next((x for x in self.board if x.name == name), None)
        
