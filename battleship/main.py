from collections import namedtuple
from enum import Enum
from typing import Iterable

Coordinate = namedtuple("Coordinates", ["line", "column"])


class Ship:
    def __init__(self, coordinates: list[Coordinate]) -> None:
        self._coordinates = coordinates

    @property
    def coordinates(self) -> list[Coordinate]:
        return self._coordinates


class BoxValue(str, Enum):
    EMPTY = "0"
    FILLED = "1"
    TOUCHED = "X"
    WATER = "~"


class Grid:
    def __init__(self, matrix: list[list[BoxValue]]) -> None:
        self._grid = matrix

    def get_box(self, column: int, line: int) -> BoxValue:
        return self._grid[line][column]

    def set_box(self, column: int, line: int, value: BoxValue) -> None:
        self._grid[line][column] = value

    def __eq__(self, other: "Grid") -> bool:
        return self._grid == other._grid

    def __repr__(self) -> str:
        return "\n".join([" ".join(line) for line in self._grid])

    def show(self) -> None:
        print(self)


def create_grid(grid_size: int = 9) -> Grid:
    matrix = [[BoxValue.EMPTY for _ in range(grid_size)] for _ in range(grid_size)]
    return Grid(matrix=matrix)


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


def take_a_shoot(grid: Grid, shoot: Coordinate) -> Grid:
    box = grid.get_box(column=shoot.column, line=shoot.line)
    match box:
        case BoxValue.EMPTY:
            print("Just some water")
            grid.set_box(column=shoot.column, line=shoot.line, value=BoxValue.WATER)
        case BoxValue.FILLED:
            print("Ship touched !!")
            grid.set_box(column=shoot.column, line=shoot.line, value=BoxValue.TOUCHED)
        case BoxValue.WATER | BoxValue.TOUCHED:
            print("Already shooten")
            raise ValueError("Already shooten")
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


def get_shoot() -> Coordinate:
    line_str = input("Line: ")
    line = int(line_str)

    column_str = input("Column:")
    column = int(column_str)

    return Coordinate(line=line, column=column)


if __name__ == "__main__":
    print("The game is ON")
    grid = create_grid(3)
    print("Here is the grid...")
    grid.show()

    ship = Ship(coordinates=[Coordinate(0, 0), Coordinate(0, 1)])
    ships = [ship]
    print("Ships setup...")
    grid = place_ships_on_grid(grid=grid, ships=ships)
    grid.show()

    # shoot = Coordinate(0, 0)
    # grid = take_a_shoot(grid=grid, shoot=shoot)
    # grid.show()

    # print(is_the_end(grid=grid, ships=ships))

    # shoot = Coordinate(0, 1)
    # grid = take_a_shoot(grid=grid, shoot=shoot)
    # grid.show()

    # print(is_the_end(grid=grid, ships=ships))

    while not is_the_end(grid=grid, ships=ships):
        shoot = get_shoot()
        try:
            grid = take_a_shoot(grid=grid, shoot=shoot)
            print(f"You shoot at {shoot.line} {shoot.column}")
        except ValueError:
            continue
        print("Here the grid")
        grid.show()

    print("The game is ENDED")
