import runpy

program = runpy.run_path("Code/07_primes_in_range.py")
primes_in_range = program["primes_in_range"]

assert primes_in_range(1, 10) == [2, 3, 5, 7]
assert primes_in_range(10, 20) == [11, 13, 17, 19]
assert primes_in_range(1, 5) == [2, 3, 5]

print("All test cases passed.")
