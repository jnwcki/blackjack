from hand import Hand


class Dealer(Hand):
    def __init__(self):
        super().__init__()
        self.shown_value = 0
