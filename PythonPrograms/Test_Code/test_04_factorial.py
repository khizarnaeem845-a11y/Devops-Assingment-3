import runpy

program = runpy.run_path("Code/04_factorial.py")
factorial = program["factorial"]

assert factorial(5) == 120
assert factorial(3) == 6
assert factorial(1) == 1
assert factorial(0) == 1

print("All test cases passed.")
