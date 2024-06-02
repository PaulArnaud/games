from itertools import pairwise
from typing import Iterable

from battleship.coordinate import Coordinate, ask_for_coordinate
from battleship.exceptions import InvalidError


class Ship:
    def __init__(self, coordinates: Iterable[Coordinate]) -> None:
        self._coordinates = coordinates

    @property
    def coordinates(self) -> Iterable[Coordinate]:
        return self._coordinates

    def is_valid(self) -> bool:
        return all(a.is_adjacent(b) for a, b in pairwise(self.coordinates))

    def check_if_valid(self) -> None:
        if not self.is_valid():
            raise InvalidError


def ask_for_ship(ship_size: int, plan_size: int) -> Ship:
    coordinates = [ask_for_coordinate(plan_size=plan_size) for _ in range(ship_size)]
    ship = Ship(coordinates=coordinates)
    ship.check_if_valid()
    return ship
