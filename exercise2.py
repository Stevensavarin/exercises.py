"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers):
    """Calculate the preparation time.

    :param layers: int - number of layers in our lasagna.
    :return: int - number of minutes that preparation will take.

    Function that takes the number of layers the lasagna will have and multiplies 
    by the number of minutes each layer takes to prepare.`.
    """
    preparation_time_per_layer = 2
    return layers * preparation_time_per_layer

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes that the lasagna has been baking.

    :param number_of_layers: int - number of layers in our lasagna.
    :param elapsed_bake_time: int - number of minutes that lasagna has been baking so far.
    :return: int - number of total (preparation and baking) elapsed minutes.

    Function that takes the number of layers the lasagna will have and the elapsed minutes of total
    preparation and cooking time so far, and returns the number of minutes we have spent making lasagna so far.`.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time