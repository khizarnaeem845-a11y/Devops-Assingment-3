import runpy

program = runpy.run_path("Code/20_word_frequency.py")
word_frequency = program["word_frequency"]

assert word_frequency("hello world hello") == {"hello": 2, "world": 1}
assert word_frequency("python is easy python") == {"python": 2, "is": 1, "easy": 1}
assert word_frequency("one two one") == {"one": 2, "two": 1}

print("All test cases passed.")
