import math


def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0 and i != n:
            return "not prime"
    return "prime"


def summation_of_primes(m):
    count = 0
    for j in range(2, m + 1):
        if is_prime(j) == "prime":
            count += j
    return count


print(summation_of_primes(2000000))
