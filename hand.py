from deck import Deck


class Hand:
    def __init__(self):
        self.deck = Deck().working_deck
        self.hand = []
        self.hand_tracker = []
