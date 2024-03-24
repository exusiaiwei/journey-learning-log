def convert(number):
    sound = ''
    if number % 3 == 0: sound += 'Pling'
    if number % 5 == 0: sound += 'Plang'
    if number % 7 == 0: sound += 'Plong'
    if sound == '':
    # which means can't be divided by 3, 5, or 7
        sound = str(number)
    return sound