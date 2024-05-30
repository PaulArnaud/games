from battleship.box_value import BoxValue
from battleship.coordinate import Coordinate
from battleship.exceptions import InputError, InvalidError
from battleship.player import Player
from battleship.ship import Ship


def ask_for_coordinate() -> Coordinate:
    try:
        line_str = input("Line: ")
        line = int(line_str)
    except Exception as e:
        raise InputError from e

    try:
        column_str = input("Column: ")
        column = int(column_str)
    except Exception as e:
        raise InputError from e

    return Coordinate(line=line, column=column)


def get_ship(ship_size: int) -> Ship:
    print(f"Enter coordinates for the ship of size {ship_size}")
    coordinates = [ask_for_coordinate() for _ in range(ship_size)]
    ship = Ship(coordinates=coordinates)
    ship.check_if_valid()
    return ship


def set_ship(ship_size: int, player: Player) -> None:
    try:
        ship = get_ship(ship_size=ship_size)
        player.place_ship_on_grid(ship=ship)
    except (InvalidError, InputError):
        return set_ship(ship_size=ship_size, player=player)


def set_ships(ships_sizes: list[int], player: Player) -> None:
    print(f"=> {player.name}'s turn: select coordinates for your ships")
    for ship_size in ships_sizes:
        set_ship(ship_size=ship_size, player=player)


def fight(attacker: Player, defender: Player) -> None:
    print(f"=> {attacker.name}'s turn !")
    defender.get_grid(obfuscated=True).show()
    shoot = ask_for_coordinate()
    try:
        result = defender.take_a_shoot(shoot=shoot)
        match result:
            case BoxValue.TOUCHED:
                print("Ship touched !!")
                # TODO implement touché-coulé
            case BoxValue.WATER:
                print("Just some water")
        attacker.save_shoot(shoot=shoot)
    except ValueError:
        print(f"Play again, you already shoot this coordinate, {shoot}")
        fight(attacker=attacker, defender=defender)


class Game:
    def __init__(self, player_one: Player, player_two: Player) -> None:
        self.player_one = player_one
        self.player_two = player_two

    def is_the_end(self) -> bool:
        return self.player_one.is_dead() or self.player_two.is_dead()

    def run(self) -> None:
        a = self.player_one
        d = self.player_two
        while not self.is_the_end():
            fight(attacker=a, defender=d)
            a, d = d, a
