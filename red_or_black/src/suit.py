from dataclasses import dataclass

from .color import Color


@dataclass
class Suit:
    name: str
    color: Color


diamonds = Suit(name="diamonds", color="red")
hearts = Suit(name="hearts", color="red")
spades = Suit(name="spades", color="black")
clubs = Suit(name="clubs", color="black")

suits = [diamonds, hearts, spades, clubs]
