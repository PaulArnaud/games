from .player import Player


def validate_color(player: Player, answer: str) -> bool:
    assert answer in ("red", "black")

    first_card = player.get_card(round_index=0)

    return first_card.color == answer


def validate_rank(player: Player, answer: str) -> bool:
    assert answer in ("more", "less")

    first_card = player.get_card(round_index=0)
    second_card = player.get_card(round_index=1)

    if first_card.rank <= second_card.rank:
        return answer == "more"
    else:
        return answer == "less"


def validate_placement(player: Player, answer: str) -> bool:
    assert answer in ("inner", "outer")

    first_card = player.get_card(round_index=0)
    second_card = player.get_card(round_index=1)
    third_card = player.get_card(round_index=2)

    if first_card.rank > second_card.rank:
        min_card = second_card
        max_card = first_card
    else:
        min_card = first_card
        max_card = second_card

    if min_card.rank <= third_card.rank <= max_card.rank:
        return answer == "inner"
    else:
        return answer == "outer"


def validate_suit(player: Player, answer: str) -> bool:
    assert answer in ("diamonds", "hearts", "spades", "clubs")

    return player.get_card(round_index=3).suit == answer
