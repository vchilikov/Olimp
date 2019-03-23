n = int(input())
x = [0] + [1] * n
for i in range(n - 1):
    for j in range(1, n + 1):
        x[j] += x[j - 1]

print(x[-1])
