import runpy

program = runpy.run_path("Code/01_even_odd.py")
check_even_odd = program["check_even_odd"]

assert check_even_odd(10) == "Even"
assert check_even_odd(7) == "Odd"
assert check_even_odd(0) == "Even"

print("All test cases passed.")
