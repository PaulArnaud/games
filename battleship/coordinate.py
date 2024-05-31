from battleship.exceptions import InputError

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

def ask_for_coordinate() -> Coordinate:
    try:
        line_str = input("Line: ")
        line = int(line_str)
    except Exception as e:
        raise InputError from e

    try:
        column_str = input("Column: ")
        column = int(column_str)
    except Exception as e:
        raise InputError from e

    return Coordinate(line=line, column=column)
