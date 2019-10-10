#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os

# having a weird problem with the current dir not allowed to be referenced
sys.path.append(os.path.abspath("./"))

from sets.card import Card, Color, Shape, Fill, Number
from sets.solver import Solver


def main():
    cards = [
        Card(Color.Green, Shape.Diamond, Fill.Outlined, Number.One),
        Card(Color.Purple, Shape.Diamond, Fill.Solid, Number.One),
        Card(Color.Red, Shape.Diamond, Fill.Striped, Number.One),
        Card(Color.Purple, Shape.Squiggle, Fill.Striped, Number.Three),
        Card(Color.Green, Shape.Oval, Fill.Striped, Number.Three),
        Card(Color.Green, Shape.Oval, Fill.Outlined, Number.Three),
        Card(Color.Green, Shape.Oval, Fill.Solid, Number.Three),
    ]

    solver = Solver(cards)
    for set in solver.solve():
        print(set)



if __name__ == "__main__":
    main()
