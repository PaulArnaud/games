from .card import Card


from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    cards: dict = field(default_factory=dict)

    def set_round_card(self, round_index: int, card: Card) -> None:
        self.cards[round_index] = card

    def get_card(self, round_index: int) -> Card:
        return self.cards.get(round_index)

    def __repr__(self) -> str:
        return f"{self.name} with cards {self.cards}"