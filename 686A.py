n, x = map(int, input().split())
kids = 0
for i in range(n):
    znak, d = input().split()
    d = int(d)
    if znak == '+':
        x += d
    elif d <= x:
        x -= d
    else:
        kids += 1
print(x, kids)
