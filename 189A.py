def solve(n, a, b, c):
    a, b, c = sorted([a, b, c], reverse=True)
    res = 0
    for i in range(n // a + 1):
        for j in range((n - a * i) // b + 1):
            if (n - a * i - b * j) % c == 0:
                res = max(res, i + j + (n - a * i - b * j) // c)
        if res == n // c:
            break
    return res


n, a, b, c = map(int, input().split())
print(solve(n, a, b, c))