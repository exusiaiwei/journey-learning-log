def rotate(text, key):
    result = ""
    # Iterate over each character in the text
    for char in text:
        # Check if the character is an alphabet
        if char.isalpha():
            # Determine the shift based on the case of the character
            shift = 65 if char.isupper() else 97
            # Apply the rotation cipher and append the result to the result string
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            # If the character is not an alphabet, append it as it is
            result += char
    return result