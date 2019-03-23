n = int(input())
for i in range(n):
    print(" ".join(str(j * n + (i + j) % n + 1) for j in range(n)))
