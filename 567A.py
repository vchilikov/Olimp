n = int(input())
x = list(map(int, input().split()))
x = [x[-1]] + x + [x[0]]
for i in range(1, n + 1):
    print(min(abs(x[i - 1] - x[i]), abs(x[i + 1] - x[i])), max(abs(x[0] - x[i]), abs(x[-1] - x[i])))
