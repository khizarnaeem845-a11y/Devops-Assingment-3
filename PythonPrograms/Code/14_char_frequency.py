def character_frequency(text):
    frequency = {}

    for letter in text:
        if letter in frequency:
            frequency[letter] = frequency[letter] + 1
        else:
            frequency[letter] = 1

    return frequency
