def fibonacci(n):
    fib = [1, 1]
    i = 0
    while len(str(fib[len(fib) - 1])) < n:
        fib.append(fib[i] + fib[i + 1])
        i += 1
    print(len(fib))


fibonacci(1000)
