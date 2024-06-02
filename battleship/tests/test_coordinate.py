import pytest

from battleship.coordinate import Coordinate
from battleship.exceptions import InvalidError

TEST_GRID_SIZE = 3


class TestCoordinate:
    @pytest.mark.parametrize("column", range(TEST_GRID_SIZE))
    @pytest.mark.parametrize("line", range(TEST_GRID_SIZE))
    def test_is_adjacent_is_commutative(self, column: int, line: int) -> None:
        c1 = Coordinate(line=line, column=column)
        c2 = Coordinate(line=line + 1, column=column)

        assert c1.is_adjacent(other=c2) == c2.is_adjacent(other=c1)

    @pytest.mark.parametrize("column", range(TEST_GRID_SIZE))
    @pytest.mark.parametrize("line", range(TEST_GRID_SIZE))
    def test_is_adjacent(self, column: int, line: int) -> None:
        c1 = Coordinate(line=line, column=column)
        c2 = Coordinate(line=line + 1, column=column)
        c3 = Coordinate(line=line + 2, column=column)

        assert c1.is_adjacent(other=c2)
        assert c2.is_adjacent(other=c1)

        assert c2.is_adjacent(other=c3)
        assert c3.is_adjacent(other=c2)

        assert not c1.is_adjacent(other=c3)
        assert not c3.is_adjacent(other=c1)

    def test_equal(self) -> None:
        c1 = Coordinate(line=0, column=0)
        c2 = Coordinate(line=0, column=0)

        assert c1 == c2

        c1 = Coordinate(line=0, column=0)
        c2 = Coordinate(line=1, column=0)

        assert c1 != c2

    @pytest.mark.parametrize("test_plan_size", [2, 4, 5])
    def test_check_if_valid(self, test_plan_size: int) -> None:
        c1 = Coordinate(line=0, column=0)

        c1.check_if_valid(plan_size=test_plan_size)

        c2 = Coordinate(line=10, column=0)

        with pytest.raises(InvalidError):
            c2.check_if_valid(plan_size=test_plan_size)
