n = int(input())
s = 0
cnt = 0
while n > 0:
    cnt += 1
    s += cnt
    n -= s
print(cnt if n == 0 else cnt - 1)