import enum
import collections
import uuid
from functools import reduce
from operator import ior
from typing import List, TypeVar

CardProperties = collections.namedtuple("CardProperties", "color shape fill number")
BitEnumType = TypeVar("BitEnumType", bound="BitEnum")


class BitEnum(enum.Enum):
    def as_bit_string(self) -> str:
        return ("{0:0%db}" % self.bit_length()).format(self.value)

    def bit_length(self) -> int:
        return len(self.__class__)

    @staticmethod
    def are_same(others: List[BitEnumType]) -> bool:
        bitwise_or = reduce(ior, [prop.value for prop in others])
        # ensure there is exactly one bit set
        return (bitwise_or & (bitwise_or - 1)) == 0

    @staticmethod
    def are_different(others: List[BitEnumType]) -> bool:
        bit_size = max([prop.bit_length() for prop in others])
        all_bits_set = reduce(ior, [1 << i for i in range(bit_size)])
        bitwise_or = reduce(ior, [prop.value for prop in others])
        # ensure all bits are set
        return bitwise_or == all_bits_set


class Color(BitEnum):
    Red = 1 << 0
    Green = 1 << 1
    Purple = 1 << 2


class Shape(BitEnum):
    Diamond = 1 << 0
    Oval = 1 << 1
    Squiggle = 1 << 2


class Fill(BitEnum):
    Solid = 1 << 0
    Striped = 1 << 1
    Outlined = 1 << 2


class Number(BitEnum):
    One = 1 << 0
    Two = 1 << 1
    Three = 1 << 2


class Card:
    def __init__(self, color: Color, shape: Shape, fill: Fill, number: Number):
        self.id = str(uuid.uuid4())[:8]
        self.properties = CardProperties(
            color=color, shape=shape, fill=fill, number=number
        )

        self.bits: int = 0
        skip_size: int = 0
        for index, prop in enumerate(reversed(self.properties)):
            self.bits |= prop.value << skip_size
            skip_size += prop.bit_length()

        self.bit_length = sum([prop.bit_length() for prop in self.properties])

    def as_bit_string(self):
        return "|".join([prop.as_bit_string() for prop in self.properties])

    def __repr__(self):
        props = ', '.join([f"{prop.name}"for prop in self.properties])
        return f"Card {self.id}: {self.as_bit_string()} ({props})"
