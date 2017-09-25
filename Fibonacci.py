class IsNotFibonacciNumber(Exception):
    def __init__(self):
        super(IsNotFibonacciNumber, self).__init__("This number isn't a fibonacci number")


class FibonacciFunctions:
    next_fibonacci_number = 0

    @staticmethod
    def is_fibonacci(number):
        if number == 0:
            FibonacciFunctions.next_fibonacci_number = 1
            return False
        if number == 1:
            return True

        fib = 1
        last = 1
        penultimate = 0
        while fib < number:
            j = last
            last = fib
            penultimate = j
            fib = last + penultimate

        if fib == number:
            return True

        FibonacciFunctions.next_fibonacci_number = fib
        return False

    @staticmethod
    def next_fibonacci(number):
        fib = 1
        last = 1
        penultimate = 0
        while fib < number:
            j = last
            last = fib
            penultimate = j
            fib = last + penultimate


class FibonacciList(list):
    def __init__(self):
        super(FibonacciList, self).__init__()

    def append(self, number):
        try:
            if FibonacciFunctions.is_fibonacci(number):
                list.append(self, number)
            else:
                raise IsNotFibonacciNumber()
        except IsNotFibonacciNumber as error:
            list.append(self, FibonacciFunctions.next_fibonacci_number)
            TypeError("Error {0}".format(error.args))


fib_list = FibonacciList()
fib_list.append(2)
fib_list.append(3)
fib_list.append(4)
fib_list.append(8)
fib_list.append(9)

print(fib_list)
