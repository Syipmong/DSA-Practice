def fib(n):
    prev = 0
    next = 1
    if n == 1:
        return 1
    else:
        new = prev + next
        for i in range(2, n+1):
            new = prev + next
            prev = next
            next = new
        return new


def fib_rec(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)
# Testing the functions
print("Fibonacci number at position 10 is: ", fib(10))
print("Fibonacci number at position 10 is: ", fib_rec(10))

        