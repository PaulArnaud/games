from .models import Color, Suit


from dataclasses import dataclass


@dataclass
class Card:
    rank: int
    suit: Suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self) -> str:
        return f"Card({self.rank},{self.suit})"

    @property
    def color(self) -> Color:
        if self.suit in ("diamonds", "hearts"):
            return "red"
        elif self.suit in ("clubs", "spades"):
            return "black"
        else:
            raise Exception(message="Suit is not known")

    def __lt__(self, card: "Card") -> bool:
        return self.rank < card.rank

    def __le__(self, card: "Card") -> bool:
        return self.rank <= card.rank