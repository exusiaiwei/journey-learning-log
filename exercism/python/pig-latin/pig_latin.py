def translate(text):
    words = text.split()
    pig_latin_words = []
    
    vowels = 'aeiou'
    special_cases = ['xr', 'yt']
    
    for w in words:
        pig_latin_word = ''
        if w[0] in vowels or w[:2] in special_cases:
            pig_latin_word = w + 'ay'
        else:
            vowel_pos = len(w)
            for i, char in enumerate(w):
                if char in vowels or (char =='y' and i > 0):
                    vowel_pos = i
                    if w[i-1:i+1] == 'qu':
                        vowel_pos += 1
                    break
            pig_latin_word = w[vowel_pos:] + w[:vowel_pos] + 'ay'
        pig_latin_words.append(pig_latin_word)
    return ' '.join(pig_latin_words)
