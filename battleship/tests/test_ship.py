from battleship.coordinate import Coordinate
from battleship.ship import Ship


class TestShip:
    def test_coordinates_are_well_set(self) -> None:
        c1 = Coordinate(line=1, column=1)
        c2 = Coordinate(line=1, column=2)
        coordinates = [c1, c2]
        ship = Ship(coordinates=coordinates)

        assert ship.coordinates == coordinates

    def test_is_valid(self) -> None:
        c1 = Coordinate(line=1, column=1)
        c2 = Coordinate(line=1, column=2)
        coordinates = [c1, c2]
        ship = Ship(coordinates=coordinates)
        assert ship.is_valid()

    def test_is_not_valid(self) -> None:
        c1 = Coordinate(line=1, column=1)
        c2 = Coordinate(line=1, column=3)
        coordinates = [c1, c2]
        ship = Ship(coordinates=coordinates)
        assert not ship.is_valid()
