n = int(input())
print(2 * (n // 7) + (1 if n % 7 == 6 else 0), 2 * (n // 7) + (n % 7 if n % 7 < 2 else 2))
