import runpy

program = runpy.run_path("Code/02_largest_of_three.py")
largest_of_three = program["largest_of_three"]

assert largest_of_three(10, 20, 15) == 20
assert largest_of_three(5, 2, 1) == 5
assert largest_of_three(3, 8, 4) == 8

print("All test cases passed.")
