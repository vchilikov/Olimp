a = list(map(int, input().split()))

i = 0
while i < len(a) - 1 and a[i] < a[i + 1]:
    i += 1

print("YES" if i == len(a) - 1 else "NO")
