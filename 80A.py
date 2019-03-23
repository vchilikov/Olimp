n, m = map(int, input().split())
primes = []
for i in range(2, 50):
    if all(i % el for el in primes):
        primes.append(i)
print("YES" if m in primes and primes.index(m) - primes.index(n) == 1 else "NO")
