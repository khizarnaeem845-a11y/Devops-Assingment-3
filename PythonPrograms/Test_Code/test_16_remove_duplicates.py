import runpy

program = runpy.run_path("Code/16_remove_duplicates.py")
remove_duplicates = program["remove_duplicates"]

assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
assert remove_duplicates([5, 5, 5]) == [5]
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

print("All test cases passed.")
