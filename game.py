from deck import Deck
from player import Player
from dealer import Dealer


def game():
    # Instantiate game deck, player and dealer
    deck = Deck()
    player = Player()
    dealer = Dealer()

    # Initial Deal
    player.hand = [deck.hit() for _ in range(2)]
    dealer.hand = [deck.hit() for _ in range(2)]

    print("\n\nWelcome to Blackjack.\n")
    playing = True
    player_stays = False

    while playing is True:
        player.get_value()
        dealer.get_value()
        print("Your Hand: {}".format(list(player.hand[0:])))
        print("Your Hand's Value: {}".format(player.value))

        print("\nDealer's Hand: [xxx Hidden Card xxx], {}".format(dealer.hand[1:]))
        print("Dealer's Hand Value Showing: {}".format(dealer.shown_value))
        print("_" * 60)
        if player_stays is False:
            if player.value < 21:
                player_hit = input("\nWould you like to hit? Y/n").lower()
                if player_hit != 'n':
                    player.hand.append(deck.hit())
                else:
                    print("You Have Decided To Stay.")
                    player_stays = True
            else:
                player_stays = True
        else:
            if player.value > 21:
                print("You Lose! Bust!")
                playing = False
            else:
                if dealer.value < 17:
                    dealer.hand.append(deck.hit())
                    print("Dealer Hits.")
                else:
                    if dealer.value > 21:
                        print("You Win! Dealer Busts.")
                        playing = False
                    elif dealer.value > player.value:
                        print("Dealer's Hand Beats Yours. You lost.")
                        playing = False
                    elif dealer.value == player.value:
                        print("Push. Nobody won.")
                        playing = False
                    else:
                        print("Your Hand Beats Dealer's Hand! You Win!")
                        playing = False

    print("\n\nDealer's Hand Was: {}  Total Value {}".format(dealer.hand, dealer.value))
    if input("\nGame over. Play again? Y/n").lower() != 'n':
        game()
    else:
        print("Goodbye!")
game()
