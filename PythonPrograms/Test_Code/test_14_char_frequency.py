import runpy

program = runpy.run_path("Code/14_char_frequency.py")
character_frequency = program["character_frequency"]

assert character_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
assert character_frequency("aaa") == {"a": 3}
assert character_frequency("abc") == {"a": 1, "b": 1, "c": 1}

print("All test cases passed.")
