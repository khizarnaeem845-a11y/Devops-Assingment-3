def is_palindrome_string(text):
    text = text.lower()
    reverse = ""

    for letter in text:
        reverse = letter + reverse

    if text == reverse:
        return True
    else:
        return False
