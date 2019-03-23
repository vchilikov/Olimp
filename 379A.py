a, b = map(int, input().split())
cnt = a
while a >= b:
    cnt += a // b
    a = a // b + a % b
print(cnt)
