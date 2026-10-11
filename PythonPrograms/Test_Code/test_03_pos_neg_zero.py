import runpy

program = runpy.run_path("Code/03_pos_neg_zero.py")
check_number = program["check_number"]

assert check_number(10) == "Positive"
assert check_number(-5) == "Negative"
assert check_number(0) == "Zero"

print("All test cases passed.")
