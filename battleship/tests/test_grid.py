import pytest

from battleship.box_value import BoxValue
from battleship.coordinate import Coordinate
from battleship.grid import Grid

TEST_GRID_SIZE = 3


@pytest.fixture
def test_grid() -> Grid:
    return Grid.new(grid_size=TEST_GRID_SIZE)


class TestGrid:
    def test_repr(self, test_grid: Grid)-> None:
        assert str(test_grid) == "0 0 0\n0 0 0\n0 0 0"

    @pytest.mark.parametrize("column", range(TEST_GRID_SIZE))
    @pytest.mark.parametrize("line", range(TEST_GRID_SIZE))
    def test_get_box(self, test_grid: Grid, column: int, line: int) -> None:
        coordinate = Coordinate(column=column, line=line)
        assert test_grid.get_box(coordinate=coordinate) == BoxValue.EMPTY

    @pytest.mark.parametrize("column", range(TEST_GRID_SIZE))
    @pytest.mark.parametrize("line", range(TEST_GRID_SIZE))
    def test_set_box(self, test_grid: Grid, column: int, line: int) -> None:
        coordinate = Coordinate(column=column, line=line)
        test_grid.set_box(coordinate=coordinate, value=BoxValue.FILLED)

        assert test_grid.get_box(coordinate=coordinate) == BoxValue.FILLED

    def test_set_boxes(self, test_grid: Grid) -> None:
        c1 = Coordinate(column=0, line=0)
        c2 = Coordinate(column=1, line=1)
        c3 = Coordinate(column=2, line=2)
        coordinates = [c1, c2, c3]
        test_grid.set_boxes(coordinates=coordinates, value=BoxValue.FILLED)

        assert test_grid.get_boxes(coordinates=coordinates) == [
            BoxValue.FILLED,
            BoxValue.FILLED,
            BoxValue.FILLED,
        ]

    def test_box_is_equal(self, test_grid: Grid) -> None:
        grid = Grid.new(grid_size=TEST_GRID_SIZE)
        assert grid == test_grid

    @pytest.mark.parametrize(
        "grid_size",
        range(10),
    )
    def test_new_grid(self, grid_size: int) -> None:
        grid = Grid.new(grid_size=grid_size)
        matrix = [[BoxValue.EMPTY for _ in range(grid_size)] for _ in range(grid_size)]
        expected_grid = Grid(matrix=matrix)
        assert grid == expected_grid
