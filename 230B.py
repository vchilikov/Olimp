from math import sqrt


def primes(n):
    sieve = set(range(3, n + 1, 2))
    if n >= 2:
        sieve.add(2)
    for i in range(3, int(sqrt(n)) + 1, 2):
        if i in sieve:
            sieve -= set(range(2 * i, n + 1, i))
    return sieve

n = input()
a = []
for el in map(int, input().split()):
    sqrt_a = int(sqrt(el))
    a.append(sqrt_a if sqrt_a ** 2 == el else 1)
primes_a = primes(max(a))
print("\n".join("YES" if el in primes_a else "NO" for el in a))