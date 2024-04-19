import random
import os
from functions import (
    create_deck,
    deal_card,
    calculate_card_value,
    has_blackjack,
    handle_player_turn,
    play_dealer_turn,
    determine_winner,
    buy_more_chips,
)


def main():
    # Game Setup
    playing = True
    chips = 100  # Starting chips

    while playing:
        # Get player bet
        while True:
            try:
                bet = int(
                    input("Enter your bet (between 1 and {} chips): ".format(chips))
                )
                if 1 <= bet <= chips:
                    break
                else:
                    print("Invalid bet. Please enter a value between 1 and", chips)
            except ValueError:
                print("Invalid bet. Please enter a number.")

        # Initialize deck and hands for each round
        deck = create_deck()
        random.shuffle(deck)  # Shuffle the deck
        player_hand = []
        dealer_hand = []

        # Deal initial cards
        for _ in range(2):  # Deal two cards each
            player_hand.append(deal_card(deck))
            dealer_hand.append(deal_card(deck))

        player_value = calculate_card_value(player_hand)
        print("Your hand:", player_hand)
        print("Your hand value:", player_value)

        # Print only the first card of the dealer's hand
        print("Dealer's first card:", dealer_hand[0])

        # Handle player turn
        player_value = handle_player_turn(
            deck, player_hand, calculate_card_value, has_blackjack
        )

        # Check for player Blackjack or Bust
        if player_value == 21:
            print("Player Blackjack! You win!")
            chips += bet
        elif player_value > 21:
            print("Player Bust! You lose.")
            chips -= bet
            if chips <= 0:
                chips_added = buy_more_chips()
                if chips_added > 0:
                    chips += chips_added
                    print("Added", chips_added, "chips to your balance.")
        else:
            # Play dealer turn if player hasn't busted or achieved Blackjack
            dealer_value = play_dealer_turn(deck, dealer_hand, calculate_card_value)

            # Determine winner and update chips
            winner = determine_winner(player_value, dealer_value)
            print(winner)
            if winner in (
                "Player Blackjack!",
                "Dealer Bust! Player Wins!",
                "Player Wins!",
            ):
                chips += bet
                print("You win!", bet, "chips added to your total.")
            elif winner == "Push":
                print("Push. No chips gained or lost.")
            elif winner in ("Dealer Wins", "Player Bust"):
                print("You lose.", bet, "chips deducted from your total.")
                chips -= bet

                if chips <= 0:
                    chips_added = buy_more_chips()
                    if chips_added > 0:
                        chips += chips_added
                        print("Added", chips_added, "chips to your balance.")
                    else:
                        print("You're out of chips! Thanks for playing.")
                        playing = False

        # Check remaining chips and ask to continue
        if chips > 0:
            play_again = input("Do you want to play again? (y/n) ").lower()
            if play_again != "y":
                playing = False
                print("Thanks for playing! You have", chips, "chips remaining.")
            else:
                # Reset game variables for a new round
                deck = create_deck()
                random.shuffle(deck)
                player_hand = []
                dealer_hand = []
                os.system("cls")
                print("Starting a new round...")


if __name__ == "__main__":
    main()
