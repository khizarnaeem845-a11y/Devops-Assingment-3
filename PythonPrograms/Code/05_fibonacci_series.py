def fibonacci_series(number):
    series = []
    a = 0
    b = 1

    for i in range(number):
        series.append(a)
        a, b = b, a + b

    return series
