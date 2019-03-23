n = int(input())
s = "C." * (n // 2) + "C" * (n % 2)
print(n * n // 2 + n % 2)
for i in range(n):
    print(s if i % 2 == 0 else ("." + s)[:-1])
