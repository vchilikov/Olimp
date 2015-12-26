from math import sqrt

n = int(input())
primes = set()
while n % 2 == 0:
    primes.add(2)
    n //= 2
i = 3
while n != 1 and (i < int(sqrt(n)) + 1):
    if n % i == 0:
        primes.add(i)
        n //= i
    else:
        i += 2

primes.add(n)
res = 1
for el in primes:
    res *= el
print(res)
