import runpy

program = runpy.run_path("Code/10_sum_of_digits.py")
sum_of_digits = program["sum_of_digits"]

assert sum_of_digits(123) == 6
assert sum_of_digits(456) == 15
assert sum_of_digits(100) == 1
assert sum_of_digits(0) == 0

print("All test cases passed.")
