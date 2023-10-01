
from .validators import validate_color, validate_placement, validate_rank, validate_suit

from .round import Round
from .deck import Deck
from .player import Player

class Game:
    deck: Deck
    players: list[Player]
    rounds = [
        Round("Red or black", "Red or black ?", validate_color, 1),
        Round("More or less", "More or less ?", validate_rank, 2),
        Round("Inner or outer", "Inner or outer ?", validate_placement, 3),
        Round("Suit", "Suit ?", validate_suit, 4)
    ]

    def __init__(self, players: list[Player], rounds: list[Round]) -> None:
        self.players = players
        self.rounds = rounds
        self.deck = Deck()
        self.deck.shuffle()

    def _play(self) -> None:
        for i, round in enumerate(self.rounds):
            print(f"----- Round: {round.title} -----")
            for player in self.players:
                print(f"Player {player.name}, it's your turn")
                drawn_card = self.deck.draw()
                answer = input(round.question)

                player.set_round_card(i, drawn_card)
                print(player)
                print(f"You draw a {drawn_card}")
                if round.validation(player, answer):
                    print(f"You can send {round.drink_quantity} drink")
                else:
                    print(f"Drink {round.drink_quantity}")
            print(f"----- End of the round {round.title} -----")



