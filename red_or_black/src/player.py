from dataclasses import dataclass, field

from .card import Card


@dataclass
class Player:
    name: str
    cards: dict = field(default_factory=dict)
    sip_drink: int = 0

    def set_round_card(self, round_index: int, card: Card) -> None:
        self.cards[round_index] = card

    def get_card(self, round_index: int) -> Card:
        return self.cards.get(round_index)

    def __repr__(self) -> str:
        return f"{self.name} - Cards: {self.cards} - Shots: {self.sip_drink}"

    def drink(self, quantity: int) -> None:
        self.sip_drink += quantity
