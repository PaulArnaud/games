from mock import Mock
import pytest
from ..src.card import Card
from ..src.suit import Suit



@pytest.fixture
def suit() -> Suit:
    return Mock(Suit)

class TestCard:
    def test_repr(self) -> None:
        card = Card(rank=1, suit=Suit(name="spades", color="red"))
        assert card.__repr__() == "Card(As,spades)"

    def test_color(self) -> None:
        card = Card(rank=1, suit=Suit(name="", color="black"))
        assert card.color == "black"

        card = Card(rank=1, suit=Suit(name="", color="red"))
        assert card.color == "red"

    def test_lt(self, suit: Suit) -> None:
        card_1 = Card(rank=1, suit=suit)
        card_2 = Card(rank=2, suit=suit)
        assert card_1 < card_2

    def test_le(self, suit: Suit) -> None:
        card_1 = Card(rank=1, suit=suit)
        card_2 = Card(rank=2, suit=suit)
        card_3 = Card(rank=1, suit=suit)
        assert card_1 <= card_2
        assert card_1 <= card_3
