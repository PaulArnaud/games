from src import Game, Player, Round
from src.validators import (
    validate_color,
    validate_placement,
    validate_rank,
    validate_suit,
)


def show_players(players: list[Player]) -> None:
    for player in players:
        print(player)


if __name__ == "__main__":
    rounds = [
        Round("Red or black", "Red or black ?\n", validate_color, 1),
        Round("More or less", "More or less ?\n", validate_rank, 2),
        Round("Inner or outer", "Inner or outer ?\n", validate_placement, 3),
        Round("Suit", "Suit ?\n", validate_suit, 4),
    ]

    paul = Player(name="Paul")
    nahel = Player(name="Nahel")
    game = Game(players=[paul, nahel], rounds=rounds)

    print(game.deck)
    show_players(players=game.players)

    game.play()

    print(game.deck)
    show_players(players=game.players)
