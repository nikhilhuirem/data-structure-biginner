# Recursive implementation to calculate the n-th Fibonacci number
def fibonacci(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return n

    # Recursive case: fib(n) = fib(n - 1) + fib(n - 1)
    return fibonacci(n - 1) + fibonacci(n - 2) 


def func3():
    print("Three")

def func2():
    func3()
    print("Two")

def func1():
    func2()
    print("One")

func1()