def square_of_sum(number):
    result = 0
    for item in range(1, number+1):
        result += item
    return result**2


def sum_of_squares(number):
    result = 0
    for item in range(1, number+1):
        result += item**2
    return result


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
