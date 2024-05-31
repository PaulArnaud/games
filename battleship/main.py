from battleship.game import Game
from battleship.player import HumanPlayer, RobotPlayer

if __name__ == "__main__":
    print("The game is ON")
    GRID_SIZE = 3
    SHIPS_SIZES = [1]

    # Player Paul
    paul = HumanPlayer(name="Paul", grid_size=GRID_SIZE)
    paul.setup_ships(ships_sizes=SHIPS_SIZES)

    # Player Lea
    lea = RobotPlayer(name="Robot", grid_size=GRID_SIZE)
    lea.setup_ships(ships_sizes=SHIPS_SIZES)

    game = Game(player_one=paul, player_two=lea)
    game.run()

    print("The game is ENDED")
