def distance(a, b):
    d = abs(int(b) - int(a))
    return min(d, 10 - d)


input()
print(sum([distance(x, y) for x, y in zip(input(), input())]))
