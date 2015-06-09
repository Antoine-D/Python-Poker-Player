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

# returns the attributes of a hand in list with tuples size two of each attr
# ex: [[7, ["C", "S"]], [11, ["C", "D"], [3, ["H"]]] =====> [["two of kind", 7], ["two of kind", 11]]
def get_hand_attributes(hand_dist):

    # stores the attributes of the hand (flush, straight, 2-pair, etc.)
    hand_attributes = list()


    # check the hand for a straight
    if is_straight(hand_dist):
        top_value = get_straight_top_value(hand_dist)
        hand_attributes.append(["straight", top_value])

    # check the hand for a flush
    if is_flush(hand_dist):
        top_value = get_straight_top_value(hand_dist)
        hand_attributes.append(["flush", sorted(hand_dist)[len(hand_dist)-1]])


    # check the hand for 2, 3, and 4 of a kind
    for value_tally in hand_dist:

        if(len(value_tally[1]) == 4):
            hand_attributes.append(["4 of kind", value_tally[0]])

        elif(len(value_tally[1]) == 3):
            hand_attributes.append(["3 of kind", value_tally[0]])

        elif(len(value_tally[1]) == 2):
            hand_attributes.append(["2 of kind", value_tally[0]])


    return hand_attributes

def get_hand_attribute(attribute_to_pull, hand_attributes):
    for attribute in hand_attributes:
        if attribute[0] == attribute_to_pull:
            return attribute[1]

    # if reached here then the hand doesn't have an attribute with 
    # the name attribute_to_pull
    return 0

def widdle_straight_flushes(hands_to_compare, hands_attributes):

    straight_flushes = list()
    for hand_index, hand in enumerate(hands_to_compare):
        flush_value = get_hand_attribute("flush", hands_attributes[hand_index])
        straight_value = get_hand_attribute("straight", hands_attributes[hand_index])

        if flush_value != 0 and straight_value != 0:
            straight_flushes.append([hand_index, straight_value])

    if len(hands_to_compare) > 0:
        remaining_hands_to_compare = list()
        remaining_hands_attributes = list()
        for hand_index, hand in enumerate(hands_to_compare):
            for straight_flush in straight_flushes:
                if straight_flush[0] == hand_index:
                    remaining_hands_to_compare.append(hand)
                    remaining_hands_attributes.append(hands_attributes[hand_index])

        hands_to_compare = remaining_hands_to_compare
        hands_attributes = remaining_hands_attributes
    
    return hands_to_compare, hands_attributes

def widdle_four_of_kinds():
    four_kinds = list()
    for hand_index, hand in enumerate(hands_to_compare):
        four_of_kind_value = get_hand_attribute("4 of kind", hands_attributes)

        if four_of_kind_value != 0:
            four_kinds.append([hand_index, four_of_kind_value])

    if len(four_kinds) > 0:
        remaining_hands_to_compare = list()
        remaining_hands_attributes = list()
        for hand_index, hand in enumerate(hands_to_compare):
            for straight_flush in straight_flushes:
                if straight_flush[0] == hand_index:
                    remaining_hands_to_compare.append(hand)
                    remaining_hands_attributes.append(hands_attributes[hand_index])

        hands_to_compare = remaining_hands_to_compare
        hands_attributes = remaining_hands_attributes

        return hands_to_compare, hands_attributes



def widdle_hands(hand_to_check, hands_to_compare, hands_attributes):
    if hand_to_check == "straight flush":
        return widdle_straight_flushes(hands_to_compare, hands_attributes)
    elif hand_to_check == "four of a kind":
        #return widdle_four_of_kinds(hands_to_compare, hands_attributes)
        r=2
    elif hand_to_check == "full house":
        r = 2
    elif hand_to_check == "flush":
        r = 2
    elif hand_to_check == "straight":
        r = 2
    elif hand_to_check == "three of kind":
        r = 2
    elif hand_to_check == "two pair":
        r = 2
    elif hand_to_check == "one pair":
        r = 2
    elif hand_to_check == "high card":
        r = 2

    return widdle_straight_flushes(hands_to_compare, hands_attributes)




def compare_hands(hands_to_compare, hands_attributes):

    # get the attributes for each of the
    hands_attributes = list()
    for hand in hands_to_compare:
        hands_attributes.append(get_hand_attributes(get_card_distribution(hand)))

    hands_to_check = ["straight flush", "four of a kind", "full house", "flush", "straight", "three of kind", "two pair", "one pair", "high card"]
    for potential_hand in hands_to_check:

        hands_to_compare, hands_attributes = widdle_hands(
            potential_hand, hands_to_compare, hands_attributes)

        if(len(hands_to_compare) == 1):
            return hands_to_compare[0]

deck = setup_deck()

current_state = deal(get_num_players(), deck)


# testing
hand_a = [[13, "C"], [11, "C"], [12, "C"], [9, "C"], [10, "C"]]
hand_b = [[13, "D"], [11, "D"], [12, "D"], [14, "D"], [10, "D"]]
hand_c = [[5, "H"], [14, "H"], [2, "H"], [3, "H"], [4, "H"]]
hand_d = [[2, "H"], [2, "C"], [2, "D"], [2, "S"], [4, "H"]]

hand_e = [[2, "H"], [2, "C"], [3, "D"], [3, "S"], [3, "H"]]
hand_f = [[2, "H"], [2, "C"], [4, "D"], [11, "S"], [7, "H"]]
#print(get_hand_attributes(get_card_distribution(hand_f)))

hands_attributes = list()
hands_attributes.append(get_hand_attributes(get_card_distribution(hand_a)))
hands_attributes.append(get_hand_attributes(get_card_distribution(hand_b)))
hands_attributes.append(get_hand_attributes(get_card_distribution(hand_c)))
hands_attributes.append(get_hand_attributes(get_card_distribution(hand_d)))

hands_to_compare = list()
hands_to_compare.append(hand_a)
hands_to_compare.append(hand_b)
hands_to_compare.append(hand_c)
hands_to_compare.append(hand_d)


print(widdle_straight_flushes(hands_to_compare, hands_attributes))
#print(get_hand_attributes(get_card_distribution(hand_a)))   
