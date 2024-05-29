import pytest

from battleship.player import (
    place_ship_on_grid,
)
from battleship.box_value import BoxValue
from battleship.coordinate import Coordinate
from battleship.grid import Grid, create_grid
from battleship.player import is_the_end
from battleship.ship import Ship

TEST_GRID_SIZE = 3


@pytest.mark.parametrize(
    "grid_size",
    range(10),
)
def test_create_grid(grid_size: int) -> None:
    grid = create_grid(grid_size=grid_size)
    matrix = [[BoxValue.EMPTY for _ in range(grid_size)] for _ in range(grid_size)]
    expected_grid = Grid(matrix=matrix)
    assert grid == expected_grid


@pytest.fixture
def test_grid() -> Grid:
    return create_grid(grid_size=TEST_GRID_SIZE)


class TestGrid:
    @pytest.mark.parametrize("column", range(TEST_GRID_SIZE))
    @pytest.mark.parametrize("line", range(TEST_GRID_SIZE))
    def test_get_box(self, test_grid: Grid, column: int, line: int) -> None:
        assert test_grid.get_box(column=column, line=line) == BoxValue.EMPTY

    @pytest.mark.parametrize("column", range(TEST_GRID_SIZE))
    @pytest.mark.parametrize("line", range(TEST_GRID_SIZE))
    def test_set_box(self, test_grid: Grid, column: int, line: int) -> None:
        test_grid.set_box(column=column, line=line, value=BoxValue.FILLED)

        assert test_grid.get_box(column=column, line=line) == BoxValue.FILLED

    def test_box_is_equal(self, test_grid: Grid) -> None:
        grid = create_grid(TEST_GRID_SIZE)
        assert grid == test_grid


class TestShip:
    def test_coordinates_are_well_set(self) -> None:
        c1 = Coordinate(line=1, column=1)
        c2 = Coordinate(line=1, column=2)
        coordinates = [c1, c2]
        ship = Ship(coordinates=coordinates)

        assert ship.coordinates == coordinates


def test_is_the_end_when_it_is_not_the_end() -> None:
    matrix = [
        [BoxValue.EMPTY, BoxValue.EMPTY],
        [BoxValue.TOUCHED, BoxValue.FILLED],
    ]
    grid = Grid(matrix=matrix)
    ships = [
        Ship(coordinates=[Coordinate(line=1, column=0), Coordinate(line=1, column=1)])
    ]
    assert not is_the_end(grid=grid, ships=ships)


def test_is_the_end_when_it_is_the_end() -> None:
    matrix = [
        [BoxValue.EMPTY, BoxValue.EMPTY],
        [BoxValue.TOUCHED, BoxValue.TOUCHED],
    ]
    grid = Grid(matrix=matrix)
    ships = [
        Ship(coordinates=[Coordinate(line=1, column=0), Coordinate(line=1, column=1)])
    ]
    assert is_the_end(grid=grid, ships=ships)


@pytest.mark.parametrize("column", range(TEST_GRID_SIZE))
@pytest.mark.parametrize("line", range(TEST_GRID_SIZE))
def test_place_ship_on_grid(test_grid: Grid, column: int, line: int) -> None:
    coordinate = Coordinate(line=line, column=column)
    ship = Ship(coordinates=[coordinate])
    grid = place_ship_on_grid(grid=test_grid, ship=ship)

    box = grid.get_box(column=column, line=line)

    assert box == BoxValue.FILLED
