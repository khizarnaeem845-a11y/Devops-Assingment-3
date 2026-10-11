import runpy

program = runpy.run_path("Code/11_vowels_consonants.py")
count_vowels_consonants = program["count_vowels_consonants"]

assert count_vowels_consonants("hello") == (2, 3)
assert count_vowels_consonants("python") == (1, 5)
assert count_vowels_consonants("aeiou") == (5, 0)

print("All test cases passed.")
