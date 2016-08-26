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


@timer.timer
def primes2(n):
    arr = [True] * (n + 1)
    sqrt_n = int(sqrt(n))
    for i in range(2, sqrt_n + 1):
        if arr[i]:
            for j in range(i * i, n + 1, i):
                arr[j] = False

    result = []
    for i in range(2, n + 1):
        if arr[i]:
            result.append(i)

    return result


n = 10000000

res = primes(n)
res2 = primes2(n)

if res != set(res2):
    print('Error')
