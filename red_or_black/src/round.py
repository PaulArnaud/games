from collections.abc import Callable
from dataclasses import dataclass

from .player import Player


@dataclass
class Round:
    title: str
    question: str
    validation: Callable[[Player, str], bool]
    drink_quantity: int
