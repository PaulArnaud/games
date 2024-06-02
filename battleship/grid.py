import logging

from battleship.box_value import BoxValue
from battleship.coordinate import Coordinate

logger = logging.getLogger(__name__)


class Grid:
    def __init__(self, matrix: list[list[BoxValue]]) -> None:
        self._grid = matrix

    def get_box(self, coordinate: Coordinate) -> BoxValue:
        return self._grid[coordinate.line][coordinate.column]

    def get_boxes(self, coordinates: list[Coordinate]) -> list[BoxValue]:
        return [self.get_box(coordinate=coordinate) for coordinate in coordinates]

    def set_box(self, coordinate: Coordinate, value: BoxValue) -> None:
        self._grid[coordinate.line][coordinate.column] = value

    def set_boxes(self, coordinates: list[Coordinate], value: BoxValue) -> None:
        for coordinate in coordinates:
            self.set_box(coordinate=coordinate, value=value)

    def __eq__(self, other: "Grid") -> bool:
        return self._grid == other._grid

    def __repr__(self) -> str:
        return "\n".join([" ".join(line) for line in self._grid])

    def show(self) -> None:
        logger.info(self)

    @classmethod
    def new(cls, grid_size: int = 9) -> "Grid":
        matrix = [[BoxValue.EMPTY for _ in range(grid_size)] for _ in range(grid_size)]
        return Grid(matrix=matrix)
