from card import Card
class Deck:
    [['{}{}'.format(suit, value) for suit in suits] for value in range(1, 16)]