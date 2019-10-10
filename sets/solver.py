import itertools
from typing import List
from sets.card import Card
from sets.set import Set


class Solver:
    def __init__(self, cards: List[Card]):
        self.cards = cards

    def solve(self):
        sets: List[Set] = []
        for candidate_set in itertools.combinations(self.cards, Set.size()):
            s = Set(candidate_set)
            if s.is_valid():
                sets.append(s)
        return sets