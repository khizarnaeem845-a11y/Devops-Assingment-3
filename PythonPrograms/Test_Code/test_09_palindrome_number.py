import runpy

program = runpy.run_path("Code/09_palindrome_number.py")
is_palindrome_number = program["is_palindrome_number"]

assert is_palindrome_number(121) == True
assert is_palindrome_number(1221) == True
assert is_palindrome_number(123) == False

print("All test cases passed.")
