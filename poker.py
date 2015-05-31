import random

def shuffle(deck):
    shuffled_deck = list()

    while(len(deck) > 0):
        sel_pos = int(random.randrange(0,len(deck)))
        shuffled_deck.append(deck[sel_pos])
        deck = deck[:sel_pos] + deck[sel_pos+1:]

    return shuffled_deck

def setup_deck():

    # Clubs, Diamonds, Hearts, and Spades
    card_suits = ["C", "D", "H", "S"]

    # card values (11: Jack, 12: Queen, 13: King, 14: Ace)
    card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    cards = list()
    for suit in card_suits:
        for value in card_values:
            cards.append([value, suit])
    return shuffle(cards)

def deal(num_players, deck):
    player_hands = list();

    for i in range(num_players):
        player_hands.append([deck.pop(), deck.pop()])

    return [player_hands, deck]

def get_num_players():
    num_players = 0
    while(num_players < 2 or num_players > 8):
        num_players = int(
            input("Number of players (2-8): "))
    return num_players

def get_card_distribution(hand_cards):
    card_distribution = list()

    # for each card in the hand, add it to the distribution
    for card in hand_cards:
        placed_in_dist = False

        for value_tally in card_distribution:
            # if the card's value is already in the hand, add this 
            # cards suit to the distribution list under that value
            if value_tally[0] == card[0]:
                value_tally[1].append(card[1])
                placed_in_dist = True

        # if the value didn't already exist in the distribution 
        # then add it
        if not placed_in_dist:
            this_val_tally = [card[0], list()]
            this_val_tally[1].append(card[1])
            card_distribution.append(this_val_tally)

    return sorted(card_distribution)

# Returns the hand with the highest value. As a paramater, 
# takes a list of hands' distributions (each in format that
# get_card_distribution returns).
def hand_comparison(hands_distributions):


deck = setup_deck()

current_state = deal(get_num_players(), deck)


#print(current_state[0][0][0])
#print("hands (" + str(len(current_state[0])) + "):    " + str(current_state[0]))
#print("deck (" + str(len(current_state[1])) + "):    " + str(current_state[1]))

hand_cards = [[6, "C"], [12, "D"], [12, "H"], [7, "S"], [4, "H"]]
#print(get_hand_values(hand_cards))

print(get_card_distribution(hand_cards))
#print(sorted(hand_cards))
#print(get_hand_value(hand_cards, list()))
