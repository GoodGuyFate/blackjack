import random

def create_deck():
    """
  This function creates a list representing a deck of cards for blackjack.

  Returns:
      A list of strings representing a deck of cards.
  """
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K" ]
    deck = []
    for suit in suits:
        for rank in ranks:
            card = rank + " of " + suit
            deck.append(card)
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def deal_card(deck):
    if not deck:
        return "Error: No cards left in deck"
    
    # Generate a randome index between 0 and deck size exclusive
    random_index = random.randrange(len(deck))

    # Remove and return card at the random index
    card = deck.pop(random_index)
    return card

def caclulate_card_value(card):
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
    
    

def main():
    deck = create_deck()
    
    for _ in range(5):
        dealt_card = deal_card(deck.copy())
        print(dealt_card)





if __name__ == "__main__":
    main()