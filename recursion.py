def recursion(n):
    while n > 1:
        return recursion(n -1) * n
    return n

print(recursion(5))