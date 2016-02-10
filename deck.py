import random
from card import Card


class Deck:
    def __init__(self):

        self.deck = Card()

    @property
    def new_deck(self):
        # self.new_deck = [[suit, rank for suit in Card.suit] for rank in Card.rank])
        new_deck = []
        for s in self.deck.suit:
            for r in self.deck.rank:
                new_deck.append(r + ' of ' + s)
        random.shuffle(new_deck)
        return new_deck



    def hit_one(self):
        return self.working_deck.pop()

    def hit_two(self):
        hit_two = []
        for _ in range(2):
            self.deck.pop()
            hit_two.append(self.working_deck.pop())
        return hit_two