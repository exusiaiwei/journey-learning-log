def steps(number):
    counter = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        number = number / 2 if number % 2 == 0 else number *3 + 1
        counter += 1
    return counter