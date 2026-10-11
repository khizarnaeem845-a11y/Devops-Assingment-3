import runpy

program = runpy.run_path("Code/15_second_largest.py")
second_largest = program["second_largest"]

assert second_largest([10, 20, 30, 40]) == 30
assert second_largest([5, 10, 3, 8]) == 8
assert second_largest([1, 2, 3]) == 2

print("All test cases passed.")
