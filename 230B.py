from math import sqrt


def primes(n):
    sieve = set(range(2, n + 1))
    for i in range(2, int(sqrt(n)) + 1):
        if i in sieve:
            sieve -= set(range(2 * i, n + 1, i))
    return sieve


n = input()
a = [int(sqrt(el)) if int(sqrt(el)) ** 2 == el else 1 for el in map(int, input().split())]
primes_a = primes(max(a))
for el in a:
    print("YES" if el in primes_a else "NO")
