import random


def create_deck():
    """
    This function creates a list representing a deck of cards for blackjack.

    Returns:
        A list of strings representing a deck of cards.
    """
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = []
    for suit in suits:
        for rank in ranks:
            card = rank + " of " + suit
            deck.append(card)
    return deck


def deal_card(deck):
    if not deck:
        return "Error: No cards left in deck"

    # Generate a random index between 0 and deck size exclusive
    random_index = random.randrange(len(deck))

    # Remove and return card at the random index
    card = deck.pop(random_index)

    return card


def calculate_card_value(card):
    """
    This function calculates the value of a card or a hand of cards in Blackjack, considering aces as 1 or 11.

    Args:
        card: A string representing a single card (e.g., "A of Spades") or a list of card strings.

    Returns:
        int: The value of the card or the sum of card values in the hand (1 to 21).
    """
    if isinstance(card, list):
        # Handle list of cards (calculate sum of values)
        total_value = 0
        for single_card in card:
            total_value += calculate_card_value(
                single_card
            )  # Recursive call for each card
        return total_value
    else:
        # Handle single card string (original logic)
        rank = card.split()[0]
        if rank == "A":
            return 11
        elif rank in ("J", "Q", "K"):
            return 10
        else:
            return int(rank)


def has_blackjack(hand):
    if hand != 2:
        return False

    card_value1 = calculate_card_value(hand[0])
    card_value2 = calculate_card_value(hand[1])
    hand_value = card_value1 + card_value2

    if hand_value == 21:
        return True
    else:
        return False


def handle_player_turn(deck, hand, calculate_card_value, has_blackjack):
    """
    This function handles the player's turn in Blackjack, allowing them to hit or stand.

    Args:
        deck: A list of strings representing the deck of cards.
        hand: A list of strings representing the player's hand.
        calculate_card_value: A function that calculates the value of a card.
        has_blackjack: A function that checks if a hand has Blackjack.

    Returns:
        int: The final value of the player's hand.
    """

    # Check for Blackjack on initial deal
    if has_blackjack(hand):
        print("Blackjack! You win!")
        return 21

    while True:
        choice = input("Hit (h) or Stand (s)? ").lower()

        if choice == "h":
            dealt_card = deal_card(deck)
            if dealt_card == "Error: No cards left in deck":
                print(dealt_card)
                break
            hand.append(deal_card(deck))
            hand_value = calculate_card_value(hand)
            print("Your hand:", hand)
            print("Your hand value:", hand_value)
            if hand_value > 21:
                print("Bust! Hand value exceeds 21.")
                return hand_value
            elif hand_value == 21:
                break
        elif choice == "s":
            break
        else:
            print("Invalid choice. Please choose 'hit' or 'stand'.")

    hand_value = calculate_card_value(hand)
    return hand_value


def play_dealer_turn(deck, hand, calculate_card_value):
    """
    This function plays the dealer's turn in Blackjack, automatically hitting until reaching 17 or busting.

    Args:
        deck: A list of strings representing the deck of cards.
        hand: A list of strings representing the dealer's hand.
        calculate_card_value: A function that calculates the value of a card.
    """

    while calculate_card_value(hand) < 17:
        dealt_card = deal_card(deck)
        if dealt_card == "Error: No cards left in deck":
            print(dealt_card)
            break
        hand.append(dealt_card)

    hand_value = calculate_card_value(hand)
    if hand_value > 21:
        print("Dealer's hand:", hand)
        print("Dealer's hand value:", hand_value)
    else:
        print("Dealer's hand:", hand)
        print("Dealer's hand value:", hand_value)
    return hand_value


def determine_winner(player_value, dealer_value):
    if player_value == 21 and dealer_value != 21:
        return "Player Blackjack!"
    elif player_value > 21:
        return "Player Bust!", "Bust"
    elif dealer_value > 21:
        return "Dealer Bust! Player Wins!"
    elif player_value > dealer_value:
        return "Player Wins!"
    elif player_value == dealer_value:
        return "Push"
    else:
        return "Dealer Wins"
