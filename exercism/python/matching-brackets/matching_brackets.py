def is_paired(input_string):
    pairs = {'{': '}', '[': ']', '(': ')'}
    stack = []
    for char in input_string:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    return not stack
