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

def is_flush(hand_dist):

    # doesn't have 5 unique values, so can't be a flush
    if(len(hand_dist) != 5):
        return False

    else:
        flushes_suit = hand_dist[0][1][0]
        is_hand_flush = True # asume flush until different suit seen

        # check to make sure all other cards in hand of same suit
        for card in hand_dist:
            if card[1][0] != flushes_suit:
                is_hand_flush = False
                break

        return is_hand_flush


# determine whether the given and distribution is a straight
def is_straight(hand_dist):
    hand_dist = sorted(hand_dist)

    if(len(hand_dist) == 5):
        for i in range(1, len(hand_dist)):

            if (hand_dist[i][0] != hand_dist[i-1][0] + 1) and (hand_dist[i][0] != 14
                or hand_dist[0][0] != 2):
                return False

        # made it through the hand and it's a straight
        return True

    # unique dist lenght < 5 so cannot be a straight
    else:
        return False

# get the value of the top card of a straight
# assumes the hand distribution input represents a straight
def get_straight_top_value(hand_dist):

    hand_dist = sorted(hand_dist)
    straight_high_value = 0
    if(hand_dist[len(hand_dist) - 1][0] == 14 
        and hand_dist[len(hand_dist) - 2][0] != 13):
        return hand_dist[len(hand_dist) - 2][0]
    else:
        return hand_dist[len(hand_dist) - 1][0]

# Get the maximum straight(s) by value out of the straights whose index in the 
# hands_distributions list are specified in the straight_indexes list
# def get_max_straights(straight_indexes, hands_distributions):
#     max_straights = list()
#     for straight_index in straight_indexes:
#         this_straight = sorted(hands_distributions[straight_index])

#         straight_high_value = get_straight_top_value(this_straight)

#         # if max straights is empty or the high value of this straight is greater than 
#         # the current highest straight's value, then clear the max_straights list and 
#         # append the new max straight's index
#         if(len(max_straights) == 0 or max_straights[0][0] < straight_high_value):
#             max_straights = list()
#             max_straights.append([straight_high_value, straight_index])

#         # if this straight's high value is equal to the current max straight's high
#         # value, then append this straight it to the max_straights list
#         elif max_straights[0][0] == straight_high_value:
#             max_straights.append([straight_high_value, straight_index])


#     return_list_straights = list()

#     for max_straight in max_straights:
#         return_list_straights.append(max_straight[1])

#     return return_list_straights

# Returns the a list of indexes of the hands in hands_distributions with the largest 
# value (if returned list length > 1, then there is a tie between 1 or more hands)
#def hand_comparison(hands_distributions):


def get_hand_attributes(hand_dist):

    # stores the attributes of the hand (flush, straight, 2-pair, etc.)
    hand_attributes = list()

    ##################################
    # check the hand for a straight flushe
    if is_straight(hand_dist) and is_flush(hand_dist):
        top_value = get_straight_top_value(hand_dist)
        hand_attributes.append([8, top_value])
    ##################################


    ##################################
    # check the hand for 4 of a kind
    for value_tally in hand_dist:
        if(len(value_tally[1]) == 4):
            hand_attributes.append([7, value_tally[0]])
    ##################################

    return hand_attributes

deck = setup_deck()

current_state = deal(get_num_players(), deck)


#print(current_state[0][0][0])
#print("hands (" + str(len(current_state[0])) + "):    " + str(current_state[0]))
#print("deck (" + str(len(current_state[1])) + "):    " + str(current_state[1]))

hand_a = [[13, "C"], [11, "C"], [12, "C"], [9, "C"], [10, "C"]]
hand_b = [[13, "D"], [11, "D"], [12, "D"], [9, "D"], [10, "D"]]
hand_c = [[13, "H"], [11, "H"], [12, "H"], [9, "H"], [10, "H"]]
hand_d = [[2, "H"], [3, "H"], [5, "H"], [14, "H"], [4, "H"]]
hand_d = [[2, "H"], [2, "C"], [2, "D"], [2, "S"], [4, "H"]]


print(get_hand_attributes(get_card_distribution(hand_d)))
#print(hand_comparison([get_card_distribution(hand_a), get_card_distribution(hand_b), get_card_distribution(hand_c), get_card_distribution(hand_d)]))
#print(get_hand_values(hand_cards))

#hand_comparison()
#print(is_straight(hand_cards))
#print(get_card_distribution(hand_cards))
#print(sorted(hand_cards))
#print(get_hand_value(hand_cards, list()))
