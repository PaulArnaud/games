from battleship.grid import create_grid
from battleship.coordinate import Coordinate
from battleship.game import Game
from battleship.player import Player
from battleship.ship import Ship

if __name__ == "__main__":
    print("The game is ON")
    # grid = create_grid(3)
    # print("Here is the grid...")
    # grid.show()

    # ship = Ship(coordinates=[Coordinate(0, 0), Coordinate(0, 1)])
    # ships = [ship]
    # print("Ships setup...")
    # grid = place_ships_on_grid(grid=grid, ships=ships)
    # grid.show()

    # shoot = Coordinate(0, 0)
    # grid = take_a_shoot(grid=grid, shoot=shoot)
    # grid.show()

    # print(is_the_end(grid=grid, ships=ships))

    # shoot = Coordinate(0, 1)
    # grid = take_a_shoot(grid=grid, shoot=shoot)
    # grid.show()

    # print(is_the_end(grid=grid, ships=ships))

    # while not is_the_end(grid=grid, ships=ships):
    #     shoot = get_shoot()
    #     try:
    #         grid = take_a_shoot(grid=grid, shoot=shoot)
    #         print(f"You shoot at {shoot.line} {shoot.column}")
    #     except ValueError:
    #         continue
    #     print("Here the grid")
    #     grid.show()
    GRID_SIZE = 3

    # Player Paul
    paul = Player(name="Paul")
    paul_grid = create_grid(grid_size=GRID_SIZE)
    paul.set_grid(grid=paul_grid)
    paul_ships = [Ship(coordinates=[Coordinate(1, 0), Coordinate(1, 1)])]
    paul.set_ships(ships=paul_ships)
    paul.setup()

    # Player Lea
    lea = Player(name="Léa")
    lea_grid = create_grid(grid_size=GRID_SIZE)
    lea.set_grid(grid=lea_grid)
    lea_ships = [Ship(coordinates=[Coordinate(0, 0), Coordinate(0, 1)])]
    lea.set_ships(ships=lea_ships)
    lea.setup()

    game = Game(player_one=paul, player_two=lea)
    game.run()

    print("The game is ENDED")
