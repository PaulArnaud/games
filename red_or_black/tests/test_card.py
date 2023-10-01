from ..src.card import Card

class TestCard:
    def test_repr(self) -> None:
        card = Card(rank=1, suit="spades")

        assert card.__repr__() == "Card(1,spades)"
    
    def test_color(self) -> None:
        card = Card(rank=1, suit="clubs")
        assert card.color == "black"
        
        card = Card(rank=1, suit="spades")
        assert card.color == "black"
        
        card = Card(rank=1, suit="diamonds")
        assert card.color == "red"
        
        card = Card(rank=1, suit="hearts")
        assert card.color == "red"

    def test_lt(self) -> None:
        card_1 = Card(rank=1, suit="clubs")
        card_2 = Card(rank=2, suit="diamonds")
        assert card_1 < card_2
    
    def test_le(self) -> None:
        card_1 = Card(rank=1, suit="clubs")
        card_2 = Card(rank=2, suit="diamonds")
        card_3 = Card(rank=1, suit="diamonds")
        assert card_1 <= card_2
        assert card_1 <= card_3
