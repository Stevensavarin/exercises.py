# 0   1   2  3   4    5

# 👇🏾 👇🏾 👇🏾 👇🏾  👇🏾  👇🏾

#  P  y	  t	  h	  o	  n

# 👆🏾 👆🏾 👆🏾 👆🏾  👆🏾  👆🏾

# -6  -5  -4  -3  -2  -1

"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]

print(get_rounds(27))


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return list(rounds_1) + list(rounds_2)

print(concatenate_rounds((27, 28, 29), (35, 36)))


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    if number in rounds:
        return True
    else:
        return False

print(list_contains_round([27, 28, 29, 35, 36], 29))
print(list_contains_round([27, 28, 29, 35, 36], 30))


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    len_hand = len(hand)

    return sum(hand) / len_hand

print(card_average([5, 6, 7]))


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    actual_average = sum(hand) / len(hand)
    #print(actual_average)

    first_last_average = (hand[0] + hand[-1]) / 2
    #print(first_last_average)

    median = hand[len(hand) // 2]
    #print(median)
    
    return actual_average == first_last_average or actual_average == median

print(approx_average_is_average([1, 2, 3]))
print(approx_average_is_average([2, 3, 4, 8, 8]))
print(approx_average_is_average([1, 2, 3, 5, 9]))


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    
    return card_average(hand[::2]) == card_average(hand[1::2])

print(average_even_is_average_odd([1, 2, 3]))
print(average_even_is_average_odd([1, 2, 3, 4]))


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        return hand[:-1] + [hand[-1] * 2]
    else:
        return hand

print(maybe_double_last([5, 9, 11]))
print(maybe_double_last([5, 9, 10]))


