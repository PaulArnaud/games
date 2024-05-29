from unittest.mock import Mock

import pytest

from red_or_black.src.card import Card

from ..src.player import Player


@pytest.fixture
def player() -> Player:
    return Player(name="Paul")


class TestPlayer:
    def test_repr(self, player: Player) -> None:
        assert player.__repr__() == "Paul - Cards: {} - Shots: 0"

    def test_set_round_card(self, player: Player) -> None:
        a = Mock(Card)
        index = 0
        player.set_round_card(round_index=index, card=a)

        assert player.cards[index] == a

    def test_get_card(self, player: Player) -> None:
        a = Mock(Card)
        index = 0
        player = Player(name="Paul", cards={index: a})

        assert player.get_card(index) == a
