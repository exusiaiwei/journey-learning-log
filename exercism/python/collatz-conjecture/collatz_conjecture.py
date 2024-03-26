def steps(number):
    times = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1
        times += 1    
    return times