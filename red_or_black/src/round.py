from .player import Player


from dataclasses import dataclass
from typing import Callable


@dataclass
class Round:
    title: str
    question: str
    validation: Callable[[Player, str], bool]
    drink_quantity: int