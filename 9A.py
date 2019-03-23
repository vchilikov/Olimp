a, b = 7 - max(map(int, input().split())), 6
for i in [2, 3]:
    if a % i == 0:
        a, b = a // i, b // i
print('{0}/{1}'.format(a, b))
