import runpy

program = runpy.run_path("Code/12_reverse_string.py")
reverse_string = program["reverse_string"]

assert reverse_string("hello") == "olleh"
assert reverse_string("python") == "nohtyp"
assert reverse_string("abc") == "cba"

print("All test cases passed.")
