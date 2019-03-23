n = input()
iq = list(map(lambda x: int(x) % 2, input().split()))
print(iq.index(0 if sum(iq) > 1 else 1) + 1)
