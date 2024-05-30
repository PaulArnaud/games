from battleship.game import Game, set_ships
from battleship.grid import Grid
from battleship.player import Player

if __name__ == "__main__":
    print("The game is ON")
    GRID_SIZE = 3
    SHIPS_SIZES = [1, 2]

    # Player Paul
    paul_grid = Grid.new(grid_size=GRID_SIZE)
    paul = Player(name="Paul", empty_grid=paul_grid)
    set_ships(ships_sizes=SHIPS_SIZES, player=paul)

    # Player Lea
    lea_grid = Grid.new(grid_size=GRID_SIZE)
    lea = Player(name="Léa", empty_grid=lea_grid)
    set_ships(ships_sizes=SHIPS_SIZES, player=lea)

    game = Game(player_one=paul, player_two=lea)
    game.run()

    print("The game is ENDED")
