def primes(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, 1000000):
        if n%i == 0:
            if n == i:
                return True
            else:
                return False

def nthPrime(N):
    i = 1
    prime = 2
    while (i < N):
        prime += 1
        if primes(prime) == True:
            i += 1
    print(prime)

print(nthPrime(10001))