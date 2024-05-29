from dataclasses import dataclass
from collections.abc import Callable

from .player import Player


@dataclass
class Round:
    title: str
    question: str
    validation: Callable[[Player, str], bool]
    drink_quantity: int
