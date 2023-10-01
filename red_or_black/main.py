from src import Game, Player, Round
from src.validators import (
    validate_color,
    validate_placement,
    validate_rank,
    validate_suit,
)

if __name__ == "__main__":
    rounds = [
        Round("Red or black", "Red or black ?", validate_color, 1),
        Round("More or less", "More or less ?", validate_rank, 2),
        Round("Inner or outer", "Inner or outer ?", validate_placement, 3),
        Round("Suit", "Suit ?", validate_suit, 4),
    ]

    paul = Player(name="Paul")
    nahel = Player(name="Nahel")
    game = Game(players=[paul, nahel], rounds=rounds)

    print(len(game.deck))
    print(game.players)

    game.play()

    print(len(game.deck))
    for player in game.players:
        print(player)
