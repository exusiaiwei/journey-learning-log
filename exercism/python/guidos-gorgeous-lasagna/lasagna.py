"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(realtime):
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    elapsed_time= EXPECTED_BAKE_TIME - realtime
    return elapsed_time


# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the total preparation time.

    :param number_of_layers: int - numbers of layers of the lasagna.
    :return: int - total preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the actual elapsed minutes of making the lasagna.
    based on the `PREPARATION_TIME`.
    """
    total_preparation_time = PREPARATION_TIME * number_of_layers
    return total_preparation_time 


# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the elapsed bake time.

    :param number_of_layers: int - number of layers of the lasagna.
    :param elapsed_bake_time: int - elapsed bake time of the lasagna.
    :return: int - elapsed bake time (in minutes) derived from 'number_of_layers' and 'elapsed_bake_time'.

    Function that takes the actual elapsed minutes of making the lasagna.
    based on the `PREPARATION_TIME`.
    """
    total_elapsed_time = number_of_layers * 2 + elapsed_bake_time
    return total_elapsed_time
