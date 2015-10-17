n, v = map(int, input().split())
q = [str(i + 1) for i in range(n) if v > min(map(int, input().split()[1:]))]
print(len(q))
print(" ".join(q))