def fib(n):
    """A generator for first n Fibonacci sequence."""
    a = [1, 1]
    for i in range(n):
        yield a[0]
        a = [a[1], a[0]+a[1]]

print(list(fib(int(input("How many number of the Fibonacci sequence you want to see? ")))))