n, h = map(int, input().split())
print(sum(map(lambda x: (int(x) - 1) // h + 1, input().split())))
