def fib(n):
    #a, b = 0, 1
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        nextNum = a + b
        a = b
        b = nextNum
        #a, b = b, a+b
    print()
fib(50)