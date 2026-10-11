def find_missing_number(numbers, n):
    total = n * (n + 1) // 2

    for number in numbers:
        total = total - number

    return total
