n = int(input())
cnt = 0
for a1 in range(n // 1 + 1):
    for a2 in range(n // 2 + 1):
        for a5 in range(n // 5 + 1):
            for a10 in range(n // 10 + 1):
                if a1 + a2 * 2 + a5 * 5 + a10 * 10 == n:
                    cnt += 1
print(cnt)