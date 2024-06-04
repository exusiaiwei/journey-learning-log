def sum_of_multiples(limit, multiples):
    multiples_set = set()
    for num in range(1, limit):
        for multiple in multiples:
            if multiple == 0:
                continue
            if num % multiple == 0:
                multiples_set.add(num)
                break
    return sum(multiples_set)