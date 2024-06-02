import logging

from battleship.game import Game
from battleship.player import HumanPlayer, RobotPlayer

logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("The game is ON")
    GRID_SIZE = 9
    SHIPS_SIZES = [1]

    logger.info("Setup first player")
    # Player Paul
    paul = HumanPlayer(name="Paul", grid_size=GRID_SIZE)
    paul.setup_ships(ships_sizes=SHIPS_SIZES)

    logger.info("Setup second player")
    # Player Lea
    robot = RobotPlayer(name="Robot", grid_size=GRID_SIZE)
    robot.setup_ships(ships_sizes=SHIPS_SIZES)

    logger.debug(f"Setup game with players({paul.name} & {robot.name})")
    game = Game(player_one=paul, player_two=robot)
    game.run()

    logger.info("The game is ENDED")
