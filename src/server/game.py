#game logic
from model.tile import Tile
from model.tile_type import TileType
from model.card import Card
from model.card_type import CardType
from board import Board
from player import Player

from random import shuffle, randrange

class Game:
    def __init__(self):
        #initialize game variables
        #game objects, etc...
        self.board = Board()

        self.players = []
        self.started = False
        self.current_player_index = 0
        self.case_file = {}

        self.suspects = ["Miss Scarlet", "Professor Plum", "Mrs. Peacock", "Mr. Green", "Mrs. White", "Colonel Mustard"]
        self.suspect_initial_locations = ["h_hl", "h_sl", "h_lc", "h_cb", "h_bk", "h_ld"]
        self.card_list = []

    def initialize_game(self):
        #create cards, shuffle and put 1 of each type to case file
        #shuffle rest of the cards and deal to each player
        #place players to appropriate positions

        weapons = []
        weapons.append(Card("Rope", CardType.WEAPON))
        weapons.append(Card("Lead Pipe", CardType.WEAPON))
        weapons.append(Card("Knife", CardType.WEAPON))
        weapons.append(Card("Wrench", CardType.WEAPON))
        weapons.append(Card("Candlestick", CardType.WEAPON))
        weapons.append(Card("Revolver", CardType.WEAPON))
        weapon_answer = weapons.pop(randrange(len(weapons)))

        rooms = []
        rooms.append(Card("Study", CardType.ROOM))
        rooms.append(Card("Hall", CardType.ROOM))
        rooms.append(Card("Lounge", CardType.ROOM))
        rooms.append(Card("Library", CardType.ROOM))
        rooms.append(Card("Billiard Room", CardType.ROOM))
        rooms.append(Card("Dining Room", CardType.ROOM))
        rooms.append(Card("Conservatory", CardType.ROOM))
        rooms.append(Card("Ballroom", CardType.ROOM))
        rooms.append(Card("Kitchen", CardType.ROOM))
        room_answer = rooms.pop(randrange(len(rooms)))

        suspects = []
        suspects.append(Card("Miss Scarlet", CardType.CHARACTER))
        suspects.append(Card("Professor Plum", CardType.CHARACTER))
        suspects.append(Card("Colonel Mustard", CardType.CHARACTER))
        suspects.append(Card("Mrs. Peacock", CardType.CHARACTER))
        suspects.append(Card("Mr. Green", CardType.CHARACTER))
        suspects.append(Card("Mrs. White", CardType.CHARACTER))
        suspect_answer = suspects.pop(randrange(len(suspects)))

        #answer cards
        self.case_file = {'weapon': weapon_answer, 'room': room_answer, 'suspect': suspect_answer}

        self.card_list.extend(weapons)
        self.card_list.extend(rooms)
        self.card_list.extend(suspects)

        #shuffle and deal cards
        shuffle(self.card_list)
        players_count = len(self.players)
        hands = [self.card_list[i::players_count] for i in range(0, players_count)]
        for i in range(0, len(self.players)):
            self.players[i].cards = hands[i]

        #player placement
        for p in self.players:
            i = self.suspects.index(p.name)
            p.location = self.board.get_tile(self.suspect_initial_locations[i])

    
    def add_player(self, sid):
        if(len(self.players) < 6):
            player = Player(sid, self.suspects[len(self.players)])
            self.players.append(player)
            return self.suspects[len(self.players)-1]

        else:
            return None

    def joinable(self):
        return not self.started and len(self.players) < 6

    def start_game(self):
        self.started = True
        self.initialize_game()
        #TODO: give player turn
        return {"name": self.suspects[0], "id": self.players[0].id}
    
    def next_turn(self):
        self.current_player_index = self.current_player_index + 1
        if(self.current_player_index >= len(self.players)):
            self.current_player_index = 0

    def check_current_player(self, player):
        pass

    def get_player(self, player_id):
        return next((x for x in self.players if x.id == player_id), None)

    def is_player_turn(self, player_id):
        return self.players[self.current_player_index].id == player_id

    def player_moved(self, player_id, tileName):
        #validate move
        #update player location
        #return 
        player = self.get_player(player_id)
        current_location = player.location
        valid_tiles = current_location.get_connected()
        to_tile = next((x for x in valid_tiles if x.name == tileName), None)

        occupied = next((x for x in self.players if x.location == to_tile and not x.disabled), None)

        if(to_tile is None or occupied is not None):
            return False

        player.moved = True
        player.location = to_tile
        return True
    
    def suggestion_made(self, player_id, case):
        player = self.get_player(player_id)
        #TODO: add validation (is player in correct room?, is it player's turn?)

        #bring suspect to same room
        suspect = next((x for x in self.players if x.name == case['suspect']), None)
        if(suspect is not None):
            suspect.location = player.location

        #TODO: make this better
        case['location'] = player.location.name

        player.suggested = True

        for p in self.players:
            #if(p.name is not player.name):
            card = next((x for x in p.cards if x.name == case['suspect'] or x.name == case['weapon'] or x.name == case['location']), None)
            if(card is not None):
                return {"card": card, "player_name": p.name}
        
        return {"card": None}

    def accusation_made(self, player_id, case):
        player = self.get_player(player_id)
        weapon = self.case_file['weapon'].name 
        room = self.case_file['room'].name
        suspect = self.case_file['suspect'].name

        is_correct = case['suspect'] == suspect and case['location'] == room and case['weapon'] == weapon
        if(is_correct):
            #the player won
            #end game
            return True
        else:
            #disable player
            player.disabled = True
            return False

    def disable_player(self, player):
        player.disabled = True

    def end_turn(self, player_id):
        #increment next player index

        self.next_turn()
        while(self.players[self.current_player_index].disabled):
            self.next_turn()
        nextPlayer = self.players[self.current_player_index]
        nextPlayer.moved = False
        nextPlayer.suggested = False

        return nextPlayer


    #other game logic

    


    
