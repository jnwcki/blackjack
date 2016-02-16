class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0
        self.shown_value = 0

    def get_value(self):
        self.value = sum([cards.value for cards in self.hand])

    def get_shown_value(self):
        self.shown_value = sum([cards.value for cards in self.hand[1:]])

    def get_aces(self):
        self.aces = len([card for card in self.hand if card.value == 11])

