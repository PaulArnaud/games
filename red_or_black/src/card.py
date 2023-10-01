from dataclasses import dataclass

from .color import Color
from .suit import Suit


@dataclass
class Card:
    rank: int
    suit: Suit

    def __str__(self):
        return f"{self._rank} of {self.suit.name.title()}"

    def __repr__(self) -> str:
        return f"{self._rank}-{self.suit.name}"

    @property
    def color(self) -> Color:
        return self.suit.color

    @property
    def _rank(self) -> str:
        if self.rank == 1:
            return "As"
        elif self.rank == 11:
            return "Jack"
        elif self.rank == 12:
            return "Queen"
        elif self.rank == 13:
            return "King"
        else:
            return f"{self.rank}"

    def __lt__(self, card: "Card") -> bool:
        return self.rank < card.rank

    def __le__(self, card: "Card") -> bool:
        return self.rank <= card.rank
