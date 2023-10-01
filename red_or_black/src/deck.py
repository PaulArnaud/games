from random import Random

from .card import Card
from .suit import suits

SEED = 42


class Deck:
    cards: list[Card]

    def __init__(self, seed: int = SEED) -> None:
        self.cards = [Card(rank=i, suit=suit) for i in range(1, 14) for suit in suits]
        self.random = Random(x=seed)

    def draw(self) -> Card:
        """Draw the first card of the deck"""
        return self.cards.pop(0)

    def shuffle(self) -> None:
        """Shuffle cards of the deck"""
        self.random.shuffle(self.cards)

    def __repr__(self) -> str:
        return f"There is {len(self.cards)} cards in the deck"

    def __len__(self) -> int:
        return len(self.cards)
