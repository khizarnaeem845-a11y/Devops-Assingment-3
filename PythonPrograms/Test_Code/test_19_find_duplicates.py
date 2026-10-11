import runpy

program = runpy.run_path("Code/19_find_duplicates.py")
find_duplicates = program["find_duplicates"]

assert find_duplicates([1, 2, 3, 2, 1]) == [1, 2]
assert find_duplicates([5, 5, 5]) == [5]
assert find_duplicates([1, 2, 3]) == []

print("All test cases passed.")
