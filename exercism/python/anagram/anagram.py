def find_anagrams(word, candidates):
    return [c for c in candidates if c.lower() != word.lower() and sorted(c.lower()) == sorted(word.lower())]
