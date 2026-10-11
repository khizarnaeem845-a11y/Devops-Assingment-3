import runpy

program = runpy.run_path("Code/13_palindrome_string.py")
is_palindrome_string = program["is_palindrome_string"]

assert is_palindrome_string("madam") == True
assert is_palindrome_string("level") == True
assert is_palindrome_string("hello") == False

print("All test cases passed.")
