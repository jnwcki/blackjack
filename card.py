class Card:

    def __init__(self):

        self.suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
        self.rank = ["Two", "Three", "Four",
                     "Five", "Six", "Seven",
                     "Eight", "Nine", "Ten",
                     "Jack", "Queen", "King",
                     "Ace"
                    ]
    # def __str__(self):
    #    return "{} of {}".format(self, rank, suit)


class Deck:
    def __init__(self, *args, **kwargs):

        # self.deck = deck
        self.deck = Card()

    def new_deck(self):
        # self.new_deck = [[suit, rank for suit in Card.suit] for rank in Card.rank])
        new_deck = []
        for s in self.deck.suit:
            for r in self.deck.rank:
                new_deck.append(s + r)
        return new_deck
deck = Deck()
print(deck.new_deck())




