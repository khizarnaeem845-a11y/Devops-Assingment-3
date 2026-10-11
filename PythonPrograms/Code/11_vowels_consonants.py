def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for letter in text.lower():
        if letter in "aeiou":
            vowels = vowels + 1
        elif letter.isalpha():
            consonants = consonants + 1

    return vowels, consonants
