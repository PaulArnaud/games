import logging

from battleship.box_value import BoxValue
from battleship.player import Player

logger = logging.getLogger(__name__)


class Game:
    def __init__(self, player_one: Player, player_two: Player) -> None:
        self.player_one = player_one
        self.player_two = player_two

    def is_the_end(self) -> bool:
        return self.player_one.is_dead() or self.player_two.is_dead()

    def fight(self, attacker: Player, defender: Player) -> None:
        logger.info(f"=> {attacker.name}'s turn !")
        attacker.show()
        shoot = attacker.ask_for_shoot()
        logger.info(f"{attacker.name} wants to shoot at {shoot}")
        try:
            result = defender.take_a_shoot(shoot=shoot)
            match result:
                case BoxValue.TOUCHED:
                    logger.info("Ship touched !!")
                    # TODO implement touché-coulé
                case BoxValue.WATER:
                    logger.info("Just some water")
            attacker.update_shoots(shoot=shoot, value=result)
        except ValueError:
            self.fight(attacker=attacker, defender=defender)

    def run(self) -> None:
        logger.info("Game started")
        a = self.player_one
        d = self.player_two
        while not self.is_the_end():
            self.fight(attacker=a, defender=d)
            a, d = d, a
        logger.info("Game ended")
