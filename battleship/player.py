from battleship.box_value import BoxValue
from battleship.coordinate import Coordinate
from battleship.exceptions import InvalidError
from battleship.grid import Grid
from battleship.ship import Ship


def is_ship_dead(ship: Ship, grid: Grid) -> bool:
    ship_statuses = grid.get_boxes(coordinates=ship.coordinates)
    return set(ship_statuses) == {BoxValue.TOUCHED}


class Player:
    _grid: Grid
    _ships: list[Ship]
    _shoots: list[Coordinate]

    def __init__(self, name: str, empty_grid: Grid) -> None:
        self.name = name
        self._shoots = []
        self._ships = []
        self._grid = empty_grid

    def get_grid(self, obfuscated: bool = False) -> Grid:
        if obfuscated:
            return self._grid.obfuscated()
        else:
            return self._grid

    def get_ships(self) -> list[Ship]:
        return self._ships

    def get_shoots(self) -> list[Coordinate]:
        return self._shoots

    def save_shoot(self, shoot: Coordinate) -> None:
        self._shoots.append(shoot)

    def place_ship_on_grid(self, ship: Ship) -> None:
        boxes = self._grid.get_boxes(coordinates=ship.coordinates)
        if BoxValue.FILLED in boxes:
            raise InvalidError("There is already a ship right there")
        elif BoxValue.TOUCHED in boxes or BoxValue.WATER in boxes:
            raise NotImplementedError
        else:
            self._grid.set_boxes(coordinates=ship.coordinates, value=BoxValue.FILLED)
            self._ships.append(ship)

    def show(self) -> None:
        print(f"Player: {self.name}")
        print(f"{self.name}'s grid:")
        self._grid.show()

    def get_living_ships(self) -> list[Ship]:
        return [
            ship for ship in self._ships if not is_ship_dead(ship=ship, grid=self._grid)
        ]

    def is_dead(self) -> bool:
        return len(self.get_living_ships()) == 0

    def take_a_shoot(self, shoot: Coordinate) -> BoxValue:
        box = self._grid.get_box(coordinate=shoot)
        match box:
            case BoxValue.EMPTY:
                self._grid.set_box(coordinate=shoot, value=BoxValue.WATER)
                return BoxValue.WATER
            case BoxValue.FILLED:
                self._grid.set_box(coordinate=shoot, value=BoxValue.TOUCHED)
                return BoxValue.TOUCHED
            case BoxValue.WATER | BoxValue.TOUCHED:
                print("Already shooten")
                raise ValueError("Already shooten")
