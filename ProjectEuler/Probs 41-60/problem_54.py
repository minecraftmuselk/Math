"""In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of
eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of
queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next
highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards
(separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards.
You can assume that all hands are valid (no invalid characters or repeated cards), each player('s hand is in no specific '
order, and in each hand there is a clear winner.)

How many hands does Player 1 win?"""


from collections import Counter

# Map card characters to numerical values
value_map = {'2': 2, '3': 3, '4': 4, '5': 5,
             '6': 6, '7': 7, '8': 8, '9': 9,
             'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def get_ranks_and_suits(hand):
    ranks = sorted([value_map[card[0]] for card in hand], reverse=True)
    suits = [card[1] for card in hand]
    return ranks, suits

def is_straight(ranks):
    return ranks == list(range(ranks[0], ranks[0] - 5, -1))

def hand_rank(hand):
    ranks, suits = get_ranks_and_suits(hand)
    counts = Counter(ranks)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))
    count_values = [val for val, cnt in sorted_counts]
    count_counts = [cnt for val, cnt in sorted_counts]

    flush = len(set(suits)) == 1
    straight = is_straight(ranks)

    if flush and straight:
        return (8, ranks[0])  # Straight flush
    elif count_counts == [4, 1]:
        return (7, count_values[0], count_values[1])  # Four of a kind
    elif count_counts == [3, 2]:
        return (6, count_values[0], count_values[1])  # Full house
    elif flush:
        return (5, *ranks)  # Flush
    elif straight:
        return (4, ranks[0])  # Straight
    elif count_counts == [3, 1, 1]:
        return (3, count_values[0], count_values[1], count_values[2])  # Three of a kind
    elif count_counts == [2, 2, 1]:
        return (2, count_values[0], count_values[1], count_values[2])  # Two pair
    elif count_counts == [2, 1, 1, 1]:
        return (1, count_values[0], *count_values[1:])  # One pair
    else:
        return (0, *ranks)  # High card

# Read file and compare hands
player1_wins = 0

with open('poker.txt') as f:
    for line in f:
        cards = line.strip().split()
        p1, p2 = cards[:5], cards[5:]
        if hand_rank(p1) > hand_rank(p2):
            player1_wins += 1

print("Player 1 wins:", player1_wins)