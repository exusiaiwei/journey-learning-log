def is_armstrong_number(number):
    num_str = str(number)
    num_length = len(num_str)
    sum_all = sum(int(c) ** num_length for c in num_str)
    return sum_all == number