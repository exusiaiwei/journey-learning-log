def find(search_list, value):
    median = len(search_list) // 2
    if value not in search_list:
        raise ValueError("value not in array")
    elif value == search_list[median]:
        return median
    elif value < search_list[median]:
        return find(search_list[:median], value)
    else:
        return median + find(search_list[median:], value)
