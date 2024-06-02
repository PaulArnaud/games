import logging
from battleship.exceptions import InputError, InvalidError


logger = logging.getLogger(__name__)

class Coordinate:
    def __init__(self, line: int, column: int) -> None:
        self.line = line
        self.column = column

    def is_adjacent(self, other: "Coordinate") -> bool:
        if self.line == other.line:
            return self.column == other.column - 1 or self.column == other.column + 1
        if self.column == other.column:
            return self.line == other.line - 1 or self.line == other.line + 1

    def __eq__(self, other: "Coordinate") -> bool:
        return self.column == other.column and self.line == other.line

    def __repr__(self) -> str:
        return f"({self.column}, {self.line})"

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def check_if_valid(self, plan_size: int) -> None:
        if self.line >= plan_size or self.column >= plan_size:
            raise InvalidError("Coordinate is not in the plan")

def ask_for_coordinate(plan_size: int) -> Coordinate:
    available_indexes = list(range(plan_size))
    coordinates = " - ".join([str(_) for _ in available_indexes])
    try:
        line_str = input(f"Line ({coordinates}) ? -> ")
        line = int(line_str)
    except Exception as e:
        logger.error(exc_info=e)
        raise InputError("Input for line value is not valid") from e

    try:
        column_str = input(f"Column ({coordinates}) ? -> ")
        column = int(column_str)
    except Exception as e:
        logger.error(exc_info=e)
        raise InputError("Input for column value is not valid") from e

    coordinate = Coordinate(line=line, column=column)
    coordinate.check_if_valid(plan_size=plan_size)
    return coordinate
