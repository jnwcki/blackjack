class Hand:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0
        self.shown_value = 0

    def get_value(self):
        self.value = sum([cards.value for cards in self.hand])
        self.shown_value = sum([cards.value for cards in self.hand[1:]])
        self.aces = len([card for card in self.hand if card.value == 11])
        while self.aces > 0:
            if self.value > 21:
                self.value -= 10
                self.aces -= 1
            else:
                break
