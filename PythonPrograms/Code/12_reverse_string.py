def reverse_string(text):
    reverse = ""

    for letter in text:
        reverse = letter + reverse

    return reverse
