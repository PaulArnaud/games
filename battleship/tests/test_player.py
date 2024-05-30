import pytest

from battleship.box_value import BoxValue
from battleship.coordinate import Coordinate
from battleship.grid import Grid
from battleship.player import Player, is_ship_dead
from battleship.ship import Ship

TEST_GRID_SIZE = 3


@pytest.fixture
def test_player() -> Player:
    grid = Grid.new(grid_size=TEST_GRID_SIZE)
    return Player(name="example", empty_grid=grid)


def test_is_ship_dead() -> None:
    coordinate = Coordinate(line=0, column=0)
    ship = Ship(coordinates=[coordinate])
    grid = Grid(
        matrix=[
            [BoxValue.TOUCHED, BoxValue.EMPTY],
            [BoxValue.EMPTY, BoxValue.EMPTY],
        ]
    )

    assert is_ship_dead(ship=ship, grid=grid)


def test_is_ship_not_dead() -> None:
    coordinate = Coordinate(line=0, column=0)
    ship = Ship(coordinates=[coordinate])
    grid = Grid(
        matrix=[
            [BoxValue.FILLED, BoxValue.EMPTY],
            [BoxValue.EMPTY, BoxValue.EMPTY],
        ]
    )

    assert is_ship_dead(ship=ship, grid=grid)


class TestPlayer:
    def test_save_shoots(self, test_player: Player) -> None:
        assert test_player._shoots == []

        shoot = Coordinate(line=0, column=0)
        test_player.save_shoot(shoot=shoot)

        assert test_player._shoots == [shoot]

    def test_place_ship_on_grid(self, test_player: Player) -> None:
        coordinate = Coordinate(line=1, column=0)
        ship = Ship(coordinates=[coordinate])
        test_player.place_ship_on_grid(ship=ship)

        assert test_player.get_grid().get_box(coordinate=coordinate) == BoxValue.FILLED

    def test_is_dead(self, test_player: Player) -> None:
        assert test_player.is_dead()

    def test_is_not_dead(self, test_player: Player) -> None:
        coordinate = Coordinate(line=1, column=0)
        ship = Ship(coordinates=[coordinate])
        test_player.place_ship_on_grid(ship=ship)

        assert not test_player.is_dead()

    def test_get_living_ships(self, test_player: Player) -> None:
        coordinate = Coordinate(line=1, column=0)
        ship = Ship(coordinates=[coordinate])
        test_player.place_ship_on_grid(ship=ship)

        assert test_player.get_living_ships() == [ship]

    def test_take_a_shoot_on_ship(self, test_player: Player) -> None:
        coordinate = Coordinate(line=1, column=0)
        ship = Ship(coordinates=[coordinate])
        test_player.place_ship_on_grid(ship=ship)

        assert test_player.get_grid().get_box(coordinate=coordinate) == BoxValue.FILLED

        result = test_player.take_a_shoot(shoot=coordinate)

        assert result == BoxValue.TOUCHED

    def test_take_a_shoot_in_water(self, test_player: Player) -> None:
        coordinate = Coordinate(line=1, column=0)
        ship = Ship(coordinates=[coordinate])
        test_player.place_ship_on_grid(ship=ship)

        assert test_player.get_grid().get_box(coordinate=coordinate) == BoxValue.FILLED

        coordinate = Coordinate(line=0, column=0)

        assert test_player.get_grid().get_box(coordinate=coordinate) == BoxValue.EMPTY

        result = test_player.take_a_shoot(shoot=coordinate)

        assert result == BoxValue.WATER
