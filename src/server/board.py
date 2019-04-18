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
        hall.set_connected([h_sh, h_hl, h_hb])
        lounge.set_connected([h_hl, h_ld, conservatory])
        library.set_connected([h_sl, h_lb, h_lc])
        billiard.set_connected([h_hb, h_lb, h_bd, h_bb])
        dining.set_connected([h_ld, h_bd, h_dk])
        conservatory.set_connected([h_lc, h_cb, lounge])
        ball.set_connected([h_cb, h_bb, h_bk])
        kitchen.set_connected([h_bk, h_dk, study])

        h_sh.set_connected([study, hall])
        h_hl.set_connected([hall, lounge])
        h_sl.set_connected([study, library])
        h_hb.set_connected([hall, billiard])
        h_ld.set_connected([lounge, dining])
        h_lb.set_connected([library, billiard])
        h_bd.set_connected([billiard, dining])
        h_lc.set_connected([library, conservatory])
        h_bb.set_connected([billiard, ball])
        h_dk.set_connected([dining, kitchen])
        h_cb.set_connected([conservatory, ball])
        h_bk.set_connected([ball, kitchen])

        self.board = [study, hall, lounge, library, billiard, dining, conservatory, ball, kitchen, 
                        h_sh, h_hl, h_sl, h_hb, h_ld, h_lb, h_bd, h_lc, h_bb, h_dk, h_cb, h_bk]

    def get_tile(self, name):
        return next((x for x in self.board if x.name == name), None)
        
