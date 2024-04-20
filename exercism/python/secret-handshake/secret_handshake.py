def commands(binary_str):
    list_of_actions = ["wink", "double blink", "close your eyes", "jump"]
    binary_str = binary_str[::-1]
    actions = []
    for i, action in enumerate(list_of_actions):
        if binary_str[i] == "1":
            actions.append(action)
    if binary_str[4] == "1":
        actions = actions[::-1]
    return actions
