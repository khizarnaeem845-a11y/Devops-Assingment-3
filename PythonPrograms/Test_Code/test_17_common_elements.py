import runpy

program = runpy.run_path("Code/17_common_elements.py")
common_elements = program["common_elements"]

assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
assert common_elements([1, 2, 3], [4, 5, 6]) == []
assert common_elements([1, 2, 2, 3], [2, 3]) == [2, 3]

print("All test cases passed.")
