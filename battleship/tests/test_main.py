import pytest
from battleship.main import Coordinate, Grid, Ship, create_grid, BoxValue


@pytest.mark.parametrize(
    "grid_size",
    range(10),
)
def test_create_grid(grid_size: int) -> None:
    grid = create_grid(grid_size=grid_size)

    expected_grid = Grid(matrix=[[BoxValue.EMPTY] * grid_size] * grid_size)

    assert grid == expected_grid


@pytest.fixture
def test_grid() -> Grid:
    matrix = [
        [BoxValue.EMPTY, BoxValue.EMPTY, BoxValue.EMPTY],
        [BoxValue.EMPTY, BoxValue.EMPTY, BoxValue.EMPTY],
        [BoxValue.EMPTY, BoxValue.EMPTY, BoxValue.EMPTY],
    ]
    return Grid(matrix=matrix)


class TestGrid:
    @pytest.mark.parametrize("column", range(3))
    @pytest.mark.parametrize("line", range(3))
    def test_get_box(self, test_grid: Grid, column: int, line: int) -> None:
        assert test_grid.get_box(column=column, line=line) == BoxValue.EMPTY

    @pytest.mark.parametrize("column", range(3))
    @pytest.mark.parametrize("line", range(3))
    def test_set_box(self, test_grid: Grid, column: int, line: int) -> None:
        test_grid.set_box(column=column, line=line, value=BoxValue.FILLED)

        assert test_grid.get_box(column=column, line=line) == BoxValue.FILLED

    def test_box_is_equal(self, test_grid: Grid) -> None:
        grid = create_grid(3)
        assert grid == test_grid


class TestShip:
    pass
