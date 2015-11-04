import timer
import math


@timer.timer
def primes(n):
    sieve = set(range(2, n+1))
    for i in range(2, int(math.sqrt(n)) + 1):
        if i in sieve:
            sieve -= set(range(2 * i, n+1, i))
    return sieve


print(primes(9))
