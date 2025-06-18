from battleship import Board


def test_board():
    print('hi')
    player1 = Board(player = 1)
    player1.print_board()

    player1.place_ship("battleship", [0,0], [0,1])
    print("Placed battleship")
    player1.print_board()
    print("")

    player1.place_ship("submarine", [9,9], [-1,0])
    print("Placed submarine")
    player1.print_board()
    print("")


    player1.place_ship("aircraft_carrier", [9,0], [-1,0])
    print("Placed aircraft_carrier")
    player1.print_board()
    print("")

    player1.place_ship("destroyer", [3,0], [-1,0])
    print("Placed destroyer")
    player1.print_board()
    print("")

    player1.place_ship("cruiser", [8,7], [-1,0])
    print("Placed cruiser")
    player1.print_board()
    print("")

    print("attacking 8,7")
    player1.attack([8,7])  # hit
    player1.print_board()
    print("")

    print("attacking 8,6")
    player1.attack([8,6])  # miss
    player1.print_board()
    print("")

    print("attacking 7,7")
    player1.attack([7,7])  # hit
    player1.print_board()
    print("")

    print("attacking 6,7")
    player1.attack([6,7])  # hit
    player1.print_board()
    print("")

    print("attacking 5,7")
    player1.attack([5,7])  # sink cruiser
    player1.print_board()
    print("")
