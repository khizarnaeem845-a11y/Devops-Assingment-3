def primes_in_range(start, end):
    primes = []

    for number in range(start, end + 1):
        if number < 2:
            continue

        prime = True

        for i in range(2, number):
            if number % i == 0:
                prime = False
                break

        if prime:
            primes.append(number)

    return primes
