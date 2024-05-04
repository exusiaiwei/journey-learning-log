def append(list1, list2):
    return list1 + list2


def concat(lists):
    return [item for sublist in lists for item in sublist]


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, lst, initial):
    if not lst:
        return initial
    return foldl(function, lst[1:], function(initial, lst[0]))


def foldr(function, lst, initial):
    if not lst:
        return initial
    return function(foldr(function, lst[1:], initial), lst[0])


def reverse(list):
    return list[::-1]
