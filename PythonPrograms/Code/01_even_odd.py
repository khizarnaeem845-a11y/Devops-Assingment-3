def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(10))  # Output: Even
print(check_even_odd(7))   # Output: Odd
print(check_even_odd(0))   # Output: Even