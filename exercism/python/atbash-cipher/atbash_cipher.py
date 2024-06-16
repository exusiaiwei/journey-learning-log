PLAIN = 'abcdefghijklmnopqrstuvwxyz'
CPIHER = 'zyxwvutsrqponmlkjihgfedcba'
encode_dict = {PLAIN[i]: CPIHER[i] for i in range(len(PLAIN))}
decode_dict = {CPIHER[i]: PLAIN[i] for i in range(len(CPIHER))}

def encode(plain_text):
    cleaned_text = ''.join([char.lower() for char in plain_text if char.isalpha() or char.isdigit()])
    encoded_text = ''
    for i, char in enumerate(cleaned_text):
        if char.isdigit():
            encoded_text += char
        if char in encode_dict:
            encoded_text += encode_dict[char]
        if (i + 1) % 5 == 0 and i != len(cleaned_text) - 1:
            encoded_text += ' '
    return encoded_text


def decode(ciphered_text):
    cleaned_text = ''.join([char.lower() for char in ciphered_text if char.isalpha() or char.isdigit()])
    decoded_text = ''
    for char in cleaned_text:
        if char.isdigit():
            decoded_text += char
        if char in decode_dict:
            decoded_text += decode_dict[char]
    return decoded_text
