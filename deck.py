import random
from card import Card


class Deck:
    def __init__(self):
        self.deck = [Card(rank, suit) for rank in range(1, 14) for suit in range(0, 3)]
        random.shuffle(self.deck)

    def hit(self):
        return self.deck.pop()
