def find(search_list, value):
    left = 0
    right = len(search_list) - 1

    while left <= right:
        median = (left + right) // 2
        if search_list[median] == value:
            return median
        elif search_list[median] < value:
            left = median + 1
        else:
            right = median - 1

    raise ValueError("value not in array")
