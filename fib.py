def fib(n):
    prev = 0
    next = 1
    if n == 1:
        return 0
    else:
        new = prev + next
        for i in range(2, n+1):
            new = prev + next
            prev = next
            next = new
        return new
        
def main():
    # Testing the functions
    print("Fibonacci number at position 10 is: ", fib(10))
    
if __name__ == "__main__":
    main()