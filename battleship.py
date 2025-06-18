from typing import List


class Ship:
    def __init__(self, name, length):
        self.name = name
        self.starting_peg = [None, None]
        self.vector = [None, None]
        self.length = length
        self.hits = 0

    def sunk(self):
        return self.hits == self.length

class Space:
    def __init__(self):
        self.status = 'EMPTY'
        self.ship = None

    def __str__(self):
        return f"{self.status[0]}"

class Board:
    def __init__(self, player: int):
        self.player = player
        self.board_size = 10
        self.board_grid= [[Space() for _ in range(10)] for _ in range(10)]
        self.ships = dict()
        self.ships["destroyer"] = Ship("destroyer", 2)
        self.ships["submarine"] = Ship("submarine", 3)
        self.ships["cruiser"] = Ship("cruiser", 4)
        self.ships["battleship"] = Ship("battleship", 5)
        self.ships["aircraft_carrier"] = Ship("aircraft_carrier", 6)


    def print_board(self):
        for row in range(self.board_size):
            result = "".join(map(str, self.board_grid[row]))
            print(result)

    def place_ship(self, ship_str, starting_peg, vector):
        assert (abs(vector[0]) == 1 and vector[1]) == 0 or (
                vector[0] == 0 and abs(vector[1]) == 1)
        # make sure the ship is not placed
        ship:Ship = self.ships.get(ship_str)
        assert ship
        assert ship.starting_peg == [None, None]

        # make sure we can place the ship
        row = starting_peg[0]
        col = starting_peg[1]
        offset = 0
        while offset in range(ship.length):
            assert 0 <= row < self.board_size
            assert 0 <= col < self.board_size
            space: Space = self.board_grid[row][col]
            assert space.status == "EMPTY"
            offset += 1
            row += vector[0]
            col += vector[1]

        # if we made it here we are good to place
        ship.starting_peg=starting_peg
        ship.vector=vector
        row = starting_peg[0]
        col = starting_peg[1]
        offset = 0
        while offset in range(ship.length):
            space: Space = self.board_grid[row][col]
            space.status = "OCCUPIED"
            space.ship = ship
            offset += 1
            row += vector[0]
            col += vector[1]

    def attack(self, attack_peg):
        row = attack_peg[0]
        col = attack_peg[1]
        assert 0 <= row < self.board_size
        assert 0 <= col < self.board_size
        space = self.board_grid[row][col]
        assert space.status == "OCCUPIED" or space.status == "EMPTY"
        ship = space.ship
        if ship is None:
            space.status = "WHITE"
            print("MISS!")
        else:
            space.status = "RED"
            print("HIT!!!")
            ship.hits += 1
            if ship.sunk():
                print(f"You sunk my {ship.name}")




