def fibonacciGenerator(n):
    fib = 1
    last = 1
    penultimate = 0
    for i in range(n):
        yield fib
        j = last
        last = fib
        penultimate = j
        fib = last + penultimate
