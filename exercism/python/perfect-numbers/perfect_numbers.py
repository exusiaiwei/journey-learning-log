def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    select_number = 0
    for item in range(1, number):
        if number % item == 0:
            select_number += item
    if select_number == number:
        return "perfect"
    if select_number > number:
        return 'abundant'
    return 'deficient'