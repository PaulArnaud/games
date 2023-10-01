from .card import Card
from .models import Suit


import random
from typing import get_args


class Deck:
    cards: list[Card]

    def __init__(self) -> None:
        cards = []
        for i in range(1, 14):
            for suit in get_args(Suit):
                cards.append(Card(rank=i, suit=suit))
        self.cards = cards

    def draw(self) -> Card:
        """Draw the first card of the deck"""
        return self.cards.pop(0)

    def shuffle(self) -> None:
        """Shuffle cards of the deck"""
        random.shuffle(self.cards)

    def __len__(self) -> int:
        return len(self.cards)