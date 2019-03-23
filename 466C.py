n = int(input())
a = list(map(int, input().split()))
res, sum_a = 0, sum(a)
if sum_a % 3 == 0:
    sum_a_3, sum_a_2_3, s, cnt = sum_a // 3, 2 * sum_a // 3, 0, 0
    for i in range(0, n - 1):
        s += a[i]
        if s == sum_a_2_3:
            res += cnt
        cnt += s == sum_a_3
print(res)
