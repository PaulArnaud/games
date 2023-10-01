from .deck import Deck
from .player import Player
from .round import Round


class Game:
    deck: Deck
    players: list[Player]
    rounds = list[Round]

    def __init__(self, players: list[Player], rounds: list[Round]) -> None:
        self.players = players
        self.rounds = rounds
        self.deck = Deck()
        self.deck.shuffle()

    def play(self) -> None:
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
