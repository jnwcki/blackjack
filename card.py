class Card:

    def __init__(self, rank, suit, value=0):

        self.suit = suit
        self.rank = rank
        self.value = value

        if self.rank == 1:
            self.value = 1
        elif self.rank in range(2, 10):
            self.value = self.rank
        else:
            self.value = 10

    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    ranks = [None, 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
             'Nine', 'Ten', 'Jack', 'Queen', 'King'
             ]

    def __repr__(self):
        return "{} of {}".format(Card.ranks[self.rank], Card.suits[self.suit])
