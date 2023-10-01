from .deck import Deck
from .logging import Logger
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
        Logger.print_game_info("And the game begin !")
        for i, round in enumerate(self.rounds):
            Logger.print_game_info(f"----- Round: {round.title} -----")
            for player in self.players:
                Logger.print_game_question(f"Player {player.name}, it's your turn")
                drawn_card = self.deck.draw()
                answer = input(round.question)

                player.set_round_card(i, drawn_card)
                Logger.print_game_info(f"You draw a {drawn_card}")
                answer_is_correct = round.validation(player, answer)
                if answer_is_correct:
                    Logger.print_game_order(
                        f"You can send {round.drink_quantity} drink"
                    )
                    players_selection = "\n".join(
                        [f"{i}) {player.name}" for i, player in enumerate(self.players)]
                    )
                    player_number = input(f"Choose a player !\n{players_selection}\n")
                    self.players[int(player_number)].drink(
                        quantity=round.drink_quantity
                    )
                else:
                    Logger.print_game_order(f"Drink {round.drink_quantity}")
                    player.drink(quantity=round.drink_quantity)
            print(f"----- End of the round {round.title} -----")
