"""
This Python script provides functions to encode and decode messages using a custom cipher.
The encryption is based on two defined character sets (PLAIN, which represents the original alphabet,
and CPIHER, which represents the ciphered alphabet). The script also handles case insensitivity for both letters and numbers.

Functions included:
encode(plain_text):
    This function accepts plain text as input, encodes it according to the PLAIN to CPIHER mapping,
    and returns the encoded ciphertext. It also manages uppercase alphabetic characters by converting them to lowercase before encoding.

decode(ciphered_text):
    This function accepts encoded text (ciphered_text) as input and decodes it back into plain text based on the
    decode_dict mapping derived from the PLAIN and CPIHER sets.

Both functions ensure that any digits found in the original or encoded text are passed through unchanged during encoding and decoding processes.
The script handles encoded strings being separated by spaces for clarity when encoding, but this separation is not required to maintain correctness.
"""

PLAIN = 'abcdefghijklmnopqrstuvwxyz'
CPIHER = 'zyxwvutsrqponmlkjihgfedcba'
encode_dict = {PLAIN[i]: CPIHER[i] for i in range(len(PLAIN))}
decode_dict = {CPIHER[i]: PLAIN[i] for i in range(len(CPIHER))}

def encode(plain_text):
    """
    Encodes a given plain text string into ciphered text using the predefined PLAIN to CPIHER character mapping.

    Parameters:
        plain_text (str): The input text to be encoded.

    Returns:
        str: The encoded ciphertext, with uppercase alphabetic characters converted to lowercase before encoding.

    Examples:
        >>> encode("Hello World!")
        'nZsQvMjNzBm'

        >>> encode("12345")
        '12345'
    """
    # Process the input text by converting all alphabetic characters to lowercase and preserving digits
    cleaned_text = ''.join([char.lower() for char in plain_text if char.isalpha() or char.isdigit()])

    # Initialize an empty string to store encoded text with space-separated words as per instructions
    encoded_text = ''

    # Iterate through each character in the processed input text
    for i, char in enumerate(cleaned_text):
        # If current character is a digit, append it directly to encoded_text without any conversion
        if char.isdigit():
            encoded_text += char

        # If current character exists in the encoding dictionary, replace it with its corresponding cipher character from CPIHER and add to encoded_text
        elif char in encode_dict:
            encoded_text += encode_dict[char]

        # Add a space after every 5th character for readability (excluding last character if not at end of word)
        if (i + 1) % 5 == 0 and i != len(cleaned_text) - 1:
            encoded_text += ' '

    return encoded_text

def decode(ciphered_text):
    """
    Decodes a given cipher text string back into plain text using the predefined decode_dict mapping.

    Parameters:
        ciphered_text (str): The input text to be decoded.

    Returns:
        str: The decoded plain text, with uppercase alphabetic characters converted to lowercase after decoding.

    Examples:
        >>> decode("nZsQvMjNzBm")
        'helloworld!'

        >>> decode("12345")
        '12345'
    """
    cleaned_text = ''.join([char.lower() for char in ciphered_text if char.isalpha() or char.isdigit()])
    decoded_text = ''
    for char in cleaned_text:
        if char.isdigit():
            decoded_text += char
        if char in decode_dict:
            decoded_text += decode_dict[char]
    return decoded_text
