n = input()
res = 9 * sum(i * (10 ** (i - 1)) for i in range(1, len(n)))
res += (int(n) - 10 ** (len(n) - 1) + 1) * len(n)
print(res)
