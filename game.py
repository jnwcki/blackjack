from deck import Deck
from player import Player
from dealer import Dealer


def game():

    deck = Deck()
    player = Player()
    dealer = Dealer()

    player.hand = [deck.hit() for _ in range(2)]
    dealer.hand = [deck.hit() for _ in range(2)]

    print("Welcome to Blackjack.\n")
    playing = True
    while playing is True:
        player.value = sum([cards.value for cards in player.hand])
        dealer.shown_value = sum([cards.value for cards in dealer.hand[1:]])
        dealer.value = sum([cards.value for cards in dealer.hand])

        print("Your Hand: {}".format(list(player.hand[0:])))
        print("Your Hand's Value: {}".format(player.value))

        print("\nDealer's Hand: [xxx Hidden Card xxx], {}".format(dealer.hand[1:]))
        print("Dealer's Hand Value Showing: {}".format(dealer.shown_value))

        if player.value == 21:
            if dealer.value == 21:
                print("Push! Dealer has 21.")
                playing = False
            elif dealer.value > 21:
                print("You Win! Dealer Busts.")
                playing = False
            else:
                print("You Win!")
                playing = False
        elif player.value > 21:
            print("You Lose! Bust!")
            playing = False
        else:
            if dealer.value == 21:
                print("Dealer Wins")
                playing = False
            if dealer.value > 21:
                print("You Win! Dealer Busts.")
                playing = False
            else:
                player_hit = input("\nWould you like to hit? Y/n").lower()
                if player_hit == 'y':
                    player.hand.append(deck.hit())
                else:
                    pass
                if dealer.shown_value < 17:
                    dealer.hand.append(deck.hit())
                else:
                    pass
    else:
        print("Dealer's Hand Was: {}".format(dealer.hand))
        if input("\nGame over. Play again? Y/n").lower() == 'y':
            game()
        else:
            pass
game()
