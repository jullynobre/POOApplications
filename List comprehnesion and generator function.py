[int((((1 + 5**0.5) / 2)**x - ((1 - 5**0.5) / 2)**x) / 5**0.5) for x in range(1, 10)]

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
