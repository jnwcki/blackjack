from card import Card
from hand import Hand
from deck import Deck
import itertools

class Player(Hand):
    def __init__(self):
        super().__init__()
        self.hand = []
        self.hand = Deck().hit_two()[0:]


class Dealer(Hand):
    def __init__(self):
        super().__init__()
        self.hand = []
        self.hand = Deck().hit_two()[0:]


def game():
    Deck().new_deck()
    print("Welcome to Blackjack.\n")
    while True:

        print("Your Hand:")
        #pl_hand_chain = itertools.chain(*Player().hand)
        #pl_hand_value = list(itertools.chain(*Player().hand))[::2]
        #print(list(pl_hand_chain)[::-2])
        #print("Your hand is worth: " + str(sum(list(pl_hand_chain))))

        print("\nDealer Hand:")
        #dl_hand_chain = itertools.chain(*Dealer().hand)
        #dl_hand_value = list(itertools.chain(*Dealer().hand))
        #print("[xxx--Hidden--xxx], " + str(list(dl_hand_chain)))
        #print("Dealer's hand showing: " + str(sum(list(dl_hand_chain)[2::2])))
        player_hit = input("\nWould you like to hit? Y/n")


        break
game()


