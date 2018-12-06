from collections import Counter
import re


def seq(ranks):
    """ Takes a string of card ranks and returns in they are in sequence."""
    # Possibilities for sequences.
    pattern = ['[A2345]{5}', '[23456]{5}', '[34567]{5}', '[45678]{5}',
               '[56789]{5}', '[6789T]{5}', '[789TJ]{5}', '[89TJQ]{5}',
               '[9TJQK]{5}', '[TJQKA]{5}']
    # If any of them is true.
    return any([re.search(x, ranks) for x in pattern])


def rank_hand(hand_list):
    """ Takes a hand of card for a game of five card poker and returns
    what the player has according to a predetermined poker rank."""

    # Data digestion block.

    # Making the hand of cards into a 2D Array. Works better for Counter().
    second_demension = [list(x) for x in hand_list]

    # Creating a couple of Counters for the rank and suit.
    r_counter = Counter([x[0] for x in second_demension])
    s_counter = Counter([x[1] for x in second_demension])

    # Shorthand variables, to make the code more readable."""

    # Gives a string with the card ranks.
    rank = ''.join([x[0] for x in r_counter.most_common()])
    # Gives a sting with the count sequence.
    rank_c = ''.join(sorted([str(x) for x in r_counter.values()], reverse=True))
    # Gives a sting with the suits in the hand.
    suit = ''.join([x[0] for x in s_counter.most_common()])

    print('rank:', rank)
    print('rank_c:', rank_c)
    print('siut:', suit)

    # Condition block.

    # STEP 1: If the hand contains only one suit.
    if len(suit) == 1:
        # If the hand only contains letters. [10 = T]
        if re.search(r'[0-9]', rank) is None:
            # Royal flush
            return 9
        # If the cards are in sequence.
        elif seq(rank):
            # Straight flush
            return 8
        # Else it's a flush.
        return 5
    # STEP 2: If the hand has only two distinct ranks.
    elif len(rank) == 2:
        # If the secound rank has only one card to it.
        if rank_c[1] == '1':
            # Four of a kind
            return 7
        # Else it's a Full house.
        return 6
    # STEP 3: If the rank is in sequence.
    elif seq(rank):
        # Straight
        return 4
    # STEP 4: If the hand has three distinct ranks.
    elif len(rank) == 3:
        # If the first rank has three cards to it.
        if rank_c[0] == '3':
            # Three of a kind.
            return 3
        # Else it's Two pairs.
        return 2
    # STEP 5: If the hand has four distinct ranks.
    if len(rank) == 4:
        # A pair.
        return 1
    # Else it's the high card.
    return 0


print(rank_hand(['AH', 'TH', 'KD', 'TS', 'TD']))
3
# print(rank_hand(['3D', '2H', '3C', 'QS', '8D']))
# 1
# print(rank_hand(['KD', 'KH', 'KC', 'TS', 'TD']))
# 6
# print(rank_hand(['JD', 'KD', 'TD', 'QD', 'AD']))
# 9
# print(rank_hand(['6D', 'KD', 'TD', '8D', 'AD']))
# 5
