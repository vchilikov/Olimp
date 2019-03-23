l, r = map(int, input().split())
a, b, c = 0, 0, 0
for i in range(l, r - 1):
    for j in range(2, r - i + 1):
        if i % j == 0:
            a = i
            b = i + j // 2
            c = i + j
            if c % 2 == 0 and b % 2 == 0:
                b += 1
            print(a, b, c)
            exit()
print(-1)
