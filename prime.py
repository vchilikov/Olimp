from math import sqrt
import timer


@timer.timer
def primes(n):
    sieve = set(range(3, n + 1, 2))
    if n >= 2:
        sieve.add(2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if i in sieve:
            sieve -= set(range(2 * i, n + 1, i))
    return sieve


primes(1000000)
