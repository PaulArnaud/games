from battleship.box_value import BoxValue
from battleship.coordinate import Coordinate
from battleship.grid import Grid
from battleship.ship import Ship


def place_ship_on_grid(grid: Grid, ship: Ship) -> Grid:
    for coordinate in ship.coordinates:
        grid.set_box(
            column=coordinate.column,
            line=coordinate.line,
            value=BoxValue.FILLED,
        )
    return grid


def place_ships_on_grid(grid: Grid, ships: list[Ship]) -> Grid:
    for ship in ships:
        grid = place_ship_on_grid(grid=grid, ship=ship)
    return grid


def is_the_end(grid: Grid, ships: list[Ship]) -> bool:
    are_ships_dead = []
    for ship in ships:
        ship_status = [
            grid.get_box(column=coordinate.column, line=coordinate.line)
            for coordinate in ship._coordinates
        ]
        are_ships_dead.append(set(ship_status) == {BoxValue.TOUCHED})
    return all(are_ships_dead)


class Player:
    _grid: Grid
    _ships: list[Ship]
    _shoots: list[Coordinate]

    def __init__(self, name: str) -> None:
        self.name = name
        self._shoots = []

    def set_grid(self, grid: Grid) -> None:
        self._grid = grid

    def get_grid(self, obfuscated: bool = False) -> Grid:
        if obfuscated:
            return self._grid.obfuscated()
        else:
            return self._grid

    def set_ships(self, ships: list[Ship]) -> None:
        self._ships = ships

    def get_ships(self) -> list[Ship]:
        return self._ships

    def save_shoot(self, shoot: Coordinate) -> None:
        self._shoots.append(shoot)

    def setup(self) -> None:
        self._grid = place_ships_on_grid(grid=self._grid, ships=self._ships)

    def show(self) -> None:
        print(f"Player: {self.name}")
        print(f"{self.name}'s grid:")
        self._grid.show()

    @property
    def is_dead(self) -> bool:
        return is_the_end(grid=self._grid, ships=self._ships)
