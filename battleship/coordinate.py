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
