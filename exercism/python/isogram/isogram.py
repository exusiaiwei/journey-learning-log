def is_isogram(string):
    word = ''.join(c.lower() for c in string if c.isalpha())
    return len(set(word)) == len(word)
