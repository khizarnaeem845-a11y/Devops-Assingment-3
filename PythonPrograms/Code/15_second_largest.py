def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()

    return numbers[-2]
