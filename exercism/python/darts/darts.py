def score(x, y):
    r = (x ** 2 + y ** 2) ** 0.5
    if r <=1:
        return 10
    elif r <= 5:
        return 5
    elif r <= 10:
        return 1
    else:
        return 0