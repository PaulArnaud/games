from battleship.box_value import BoxValue
from battleship.coordinate import Coordinate, ask_for_coordinate
from battleship.exceptions import InputError, InvalidError
from battleship.grid import Grid
from battleship.ship import Ship, ask_for_ship


def is_ship_dead(ship: Ship, grid: Grid) -> bool:
    ship_statuses = grid.get_boxes(coordinates=ship.coordinates)
    return set(ship_statuses) == {BoxValue.TOUCHED}


class Player:
    _ships_grid: Grid
    _shoots_grid: Grid
    _ships: list[Ship]
    _shoots: list[Coordinate]

    def __init__(self, name: str, grid_size: int) -> None:
        self.name = name
        self._shoots = []
        self._ships = []
        self._ships_grid = Grid.new(grid_size=grid_size)
        self._shoots_grid = Grid.new(grid_size=grid_size)

    def get_ships_grid(self) -> Grid:
        return self._ships_grid

    def get_shoots_grid(self) -> Grid:
        return self._shoots_grid

    def get_ships(self) -> list[Ship]:
        return self._ships

    def get_shoots(self) -> list[Coordinate]:
        return self._shoots

    def save_shoot(self, shoot: Coordinate) -> None:
        self._shoots.append(shoot)

    def update_shoots(self, shoot: Coordinate, value: BoxValue) -> None:
        self.save_shoot(shoot=shoot)
        self._shoots_grid.set_box(coordinate=shoot, value=value)

    def place_ship_on_grid(self, ship: Ship) -> None:
        boxes = self._ships_grid.get_boxes(coordinates=ship.coordinates)
        if BoxValue.FILLED in boxes:
            raise InvalidError("There is already a ship right there")
        elif BoxValue.TOUCHED in boxes or BoxValue.WATER in boxes:
            raise NotImplementedError
        else:
            self._ships_grid.set_boxes(
                coordinates=ship.coordinates, value=BoxValue.FILLED
            )
            self._ships.append(ship)

    def show(self) -> None:
        print(f"Player: {self.name}")
        print(f"{self.name}'s grid:")
        self._ships_grid.show()

    def get_living_ships(self) -> list[Ship]:
        return [
            ship
            for ship in self._ships
            if not is_ship_dead(ship=ship, grid=self._ships_grid)
        ]

    def is_dead(self) -> bool:
        return len(self.get_living_ships()) == 0

    def take_a_shoot(self, shoot: Coordinate) -> BoxValue:
        box = self._ships_grid.get_box(coordinate=shoot)
        match box:
            case BoxValue.EMPTY:
                self._ships_grid.set_box(coordinate=shoot, value=BoxValue.WATER)
                return BoxValue.WATER
            case BoxValue.FILLED:
                self._ships_grid.set_box(coordinate=shoot, value=BoxValue.TOUCHED)
                return BoxValue.TOUCHED

    def setup_ships(self, ships_sizes: list[int]) -> None:
        for ship_size in ships_sizes:
            self.ask_for_ship(ship_size=ship_size)

    def ask_for_shoot(self) -> Coordinate:
        raise NotImplementedError

    def ask_for_ship(self, ship_size: int) -> Ship:
        raise NotImplementedError


class HumanPlayer(Player):
    def __init__(self, name: str, grid_size: int) -> None:
        super().__init__(name=name, grid_size=grid_size)

    def ask_for_shoot(self) -> Coordinate:
        shoot = ask_for_coordinate()
        if shoot in self._shoots:
            print(f"Play again, you already shoot this coordinate, {shoot}")
            return self.ask_for_shoot()
        return shoot

    def ask_for_ship(self, ship_size: int) -> Ship:
        try:
            ship = ask_for_ship(ship_size=ship_size)
            self.place_ship_on_grid(ship=ship)
        except (InvalidError, InputError):
            return self.ask_for_ship(ship_size=ship_size)


class RobotPlayer(Player):
    ships_position = {1: Ship(coordinates=[Coordinate(line=0, column=0)])}

    def __init__(self, name: str, grid_size: int) -> None:
        super().__init__(name=name, grid_size=grid_size)

    def ask_for_shoot(self) -> Coordinate:
        grid = self.get_shoots_grid()
        for i, line in enumerate(grid._grid):
            for j, _ in enumerate(line):
                c = Coordinate(line=i, column=j)
                value = grid.get_box(coordinate=c)
                if value == BoxValue.EMPTY:
                    return c

    def ask_for_ship(self, ship_size: int) -> Ship:
        try:
            ship = self.ships_position.get(ship_size)
            self.place_ship_on_grid(ship=ship)
        except (InvalidError, InputError):
            return self.ask_for_ship(ship_size=ship_size)
