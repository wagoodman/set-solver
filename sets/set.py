from typing import List
from sets.card import Card, CardProperties, BitEnum


class Set:
    def __init__(self, cards: List[Card]):
        if len(cards) > Set.size():
            raise RuntimeError(f"sets can only be of length 3, given {len(cards)}")
        self.cards = cards

    @staticmethod
    def size():
        return 3

    def is_valid(self) -> bool:
        valid: bool = True
        for prop_field_index, prop_field_name in enumerate(CardProperties._fields):
            card_values_for_prop = [
                card.properties[prop_field_index] for card in self.cards
            ]
            are_same = BitEnum.are_same(card_values_for_prop)
            are_different = BitEnum.are_different(card_values_for_prop)

            valid &= are_same | are_different
        return valid

    def __repr__(self):
        ret: str = "Set(\n"
        for c in self.cards:
            ret += f"   {repr(c)}\n"
        return ret + ")"
