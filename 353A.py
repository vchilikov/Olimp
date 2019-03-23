n = int(input())
sum_a, sum_b = 0, 0
even_odd = 0
for _ in range(n):
    a, b = map(lambda x: int(x) % 2, input().split())
    if a != b:
        even_odd += 1
    sum_a += a
    sum_b += b

if sum_a % 2 == 0 and sum_b % 2 == 0:
    print(0)
elif sum_a % 2 + sum_b % 2 == 2 and even_odd > 1:
    print(1)
else:
    print(-1)