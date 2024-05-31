from battleship.box_value import BoxValue
from battleship.player import Player


class Game:
    def __init__(self, player_one: Player, player_two: Player) -> None:
        self.player_one = player_one
        self.player_two = player_two

    def is_the_end(self) -> bool:
        return self.player_one.is_dead() or self.player_two.is_dead()

    def fight(self, attacker: Player, defender: Player) -> None:
        print(f"=> {attacker.name}'s turn !")
        attacker.get_shoots_grid().show()
        shoot = attacker.ask_for_shoot()
        try:
            result = defender.take_a_shoot(shoot=shoot)
            match result:
                case BoxValue.TOUCHED:
                    print("Ship touched !!")
                    # TODO implement touché-coulé
                case BoxValue.WATER:
                    print("Just some water")
            attacker.update_shoots(shoot=shoot, value=result)
        except ValueError:
            self.fight(attacker=attacker, defender=defender)

    def run(self) -> None:
        a = self.player_one
        d = self.player_two
        while not self.is_the_end():
            self.fight(attacker=a, defender=d)
            a, d = d, a
