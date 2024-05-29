from battleship.actions import get_shoot, take_a_shoot
from battleship.player import Player


def fight(attacker: Player, defender: Player) -> None:
    defender.get_grid(obfuscated=True).show()
    shoot = get_shoot()
    grid = defender.get_grid()
    grid = take_a_shoot(grid=grid, shoot=shoot)
    attacker.save_shoot(shoot=shoot)
    defender.set_grid(grid=grid)


class Game:
    def __init__(self, player_one: Player, player_two: Player) -> None:
        self.player_one = player_one
        self.player_two = player_two

    def is_the_end(self) -> bool:
        return self.player_one.is_dead or self.player_two.is_dead

    def run(self) -> None:
        a = self.player_one
        d = self.player_two
        while not self.is_the_end():
            fight(attacker=a, defender=d)
            a, d = d, a
