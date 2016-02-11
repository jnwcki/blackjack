class Card:

    def __init__(self, rank, suit):

        self.suit = suit
        self.rank = rank

    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    ranks = [None, 'Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
             'Nine', 'Ten', 'Jack', 'Queen', 'King'
            ]

    def __str__(self):
        return "{} of {}".format(Card.ranks[self.rank], Card.suits[self.suit])