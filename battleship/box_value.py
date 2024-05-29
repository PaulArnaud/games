from enum import Enum


class BoxValue(str, Enum):
    EMPTY = "0"
    FILLED = "1"
    TOUCHED = "X"
    WATER = "~"
