n = int(input())
a = input().split() + ['1']
b = []
last = 0
for i in range(1, n + 1):
    if a[i] == '1':
        b.append(str(i - last))
        last = i

print(len(b))
print(" ".join(b))
