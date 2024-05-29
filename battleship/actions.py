from battleship.box_value import BoxValue
from battleship.coordinate import Coordinate
from battleship.grid import Grid


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


def get_shoot() -> Coordinate:
    line_str = input("Line: ")
    line = int(line_str)

    column_str = input("Column:")
    column = int(column_str)

    return Coordinate(line=line, column=column)


