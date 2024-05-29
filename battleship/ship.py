from battleship.coordinate import Coordinate


class Ship:
    def __init__(self, coordinates: list[Coordinate]) -> None:
        self._coordinates = coordinates

    @property
    def coordinates(self) -> list[Coordinate]:
        return self._coordinates
