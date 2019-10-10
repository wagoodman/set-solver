import enum
import collections
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
        bitwise_or = reduce(ior, [prop.value for prop in others])
        # ensure all bits are set
        return (bitwise_or & (bitwise_or + 1)) == 0


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
        return f"{self.properties.color.as_bit_string()}|{self.properties.shape.as_bit_string()}|{self.properties.fill.as_bit_string()}|{self.properties.number.as_bit_string()}"

    def __repr__(self):
        return f"Card(color:{self.properties.color.name}, shape:{self.properties.shape.name}, fill:{self.properties.fill.name}, number:{self.properties.number.name}) = {self.as_bit_string()} = {self.bits}"