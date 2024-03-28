def score(x, y):
    length = x ** 2 + y ** 2
    if length > 100:
        return 0
    elif 25< length <=100:
        return 1
    elif 1 < length <=25:
        return 5
    else:
        return 10