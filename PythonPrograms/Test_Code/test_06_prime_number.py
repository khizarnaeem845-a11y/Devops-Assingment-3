import runpy

program = runpy.run_path("Code/06_prime_number.py")
is_prime = program["is_prime"]

assert is_prime(2) == True
assert is_prime(7) == True
assert is_prime(10) == False
assert is_prime(1) == False

print("All test cases passed.")
