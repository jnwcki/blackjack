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
    player_stays = False

    while playing is True:
        player.value = sum([cards.value for cards in player.hand])
        dealer.shown_value = sum([cards.value for cards in dealer.hand[1:]])
        dealer.value = sum([cards.value for cards in dealer.hand])

        print("Your Hand: {}".format(list(player.hand[0:])))
        print("Your Hand's Value: {}".format(player.value))

        print("\nDealer's Hand: [xxx Hidden Card xxx], {}".format(dealer.hand[1:]))
        print("Dealer's Hand Value Showing: {}".format(dealer.shown_value))
        print("_" * 60)

        if player.value == 21:                   # If player value is 21
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
        else:                                    # If player value is less than 21
            if dealer.value == 21:
                print("Dealer Wins")
                playing = False
            if dealer.value > 21:
                print("You Win! Dealer Busts.")
                playing = False
            else:                                 # If both player and dealer are less than 21
                if dealer.value < 17:

                    if player_stays is False:
                        player_hit = input("\nWould you like to hit? Y/n").lower()
                        if player_hit == 'y':
                            player.hand.append(deck.hit())
                        else:                          # Player decides to stay
                            dealer.hand.append(deck.hit())
                            player_stays = True
                    else:
                        dealer.hand.append(deck.hit())



                else:                           # Both players done taking cards. Compare hands

                    if player.value > dealer.value:
                        print("You beat the dealer! You Win!")
                        playing = False
                    elif player.value < dealer.value:
                        print("Dealer's hand beats yours. You Lose.")
                        playing = False
                    else:
                        print("Push. Game over.")
                        playing = False

    else:
        print("\n\nDealer's Hand Was: {}  Total Value {}".format(dealer.hand, dealer.value))
        if input("\nGame over. Play again? Y/n").lower() == 'y':
            game()
        else:
            pass
game()
