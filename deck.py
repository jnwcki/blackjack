import random
from card import Card


class Deck:
    def __init__(self):

        self.deck = Card()
        self.working_deck = self.new_deck()

    def new_deck(self):
        # self.new_deck = [[suit, rank for suit in Card.suit] for rank in Card.rank])
        new_deck = []
        for s in self.deck.suit:
            for r, v in self.deck.rank.items():
                new_deck.append([v, r + " of " + s])
        random.shuffle(new_deck)
        return new_deck




    def hit_one(self):
        card = self.working_deck.pop()
        return card

    def hit_two(self):
        hit_two = []
        for _ in range(2):
            self.working_deck.pop()

            hit_two.append(self.working_deck.pop())
        return hit_two
