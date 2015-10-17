n = int(input())
last = ''
cnt = 0
for i in range(n):
    current = input()
    if last != current:
        last = current
        cnt += 1
print(cnt)
