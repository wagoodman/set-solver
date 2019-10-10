#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

# having a weird problem with the current dir not allowed to be referenced
sys.path.append(os.path.abspath("./"))

from sets.card import Card, Color, Shape, Fill, Number
from sets.set import Set


def main():
    s = Set(
        cards=[
            Card(Color.Green, Shape.Diamond, Fill.Outlined, Number.One),
            Card(Color.Purple, Shape.Diamond, Fill.Solid, Number.One),
            Card(Color.Red, Shape.Diamond, Fill.Striped, Number.One),
        ]
    )
    print(s)
    print(s.is_valid())


if __name__ == "__main__":
    main()
