from battleship.box_value import BoxValue


class Grid:
    def __init__(self, matrix: list[list[BoxValue]]) -> None:
        self._grid = matrix

    def get_box(self, column: int, line: int) -> BoxValue:
        return self._grid[line][column]

    def set_box(self, column: int, line: int, value: BoxValue) -> None:
        self._grid[line][column] = value

    def __eq__(self, other: "Grid") -> bool:
        return self._grid == other._grid

    def obfuscated(self) -> "Grid":
        copy = []
        for line in self._grid:
            new_line = []
            for column in line:
                if column == BoxValue.FILLED:
                    new_line.append(BoxValue.EMPTY)
                else:
                    new_line.append(column)
            copy.append(new_line)
        return Grid(matrix=copy)

    def __repr__(self) -> str:
        return "\n".join([" ".join(line) for line in self._grid])

    def show(self) -> None:
        print(self)


def create_grid(grid_size: int = 9) -> Grid:
    matrix = [[BoxValue.EMPTY for _ in range(grid_size)] for _ in range(grid_size)]
    return Grid(matrix=matrix)
