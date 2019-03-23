from math import ceil

a = sum(map(int, input().split()))
b = sum(map(int, input().split()))
n = int(input())
print("YES" if ceil(a / 5) + ceil(b / 10) <= n else "NO")
