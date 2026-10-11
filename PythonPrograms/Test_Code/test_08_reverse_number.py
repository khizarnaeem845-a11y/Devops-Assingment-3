import runpy

program = runpy.run_path("Code/08_reverse_number.py")
reverse_number = program["reverse_number"]

assert reverse_number(123) == 321
assert reverse_number(4567) == 7654
assert reverse_number(100) == 1

print("All test cases passed.")
