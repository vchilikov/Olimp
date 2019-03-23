def reduce(x):
    res = int(x)
    while not res % 2:
        res //= 2
    while not res % 3:
        res //= 3
    return res


n = input()
print("Yes" if len(set(map(reduce, input().split()))) == 1 else "No")
