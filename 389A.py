n = int(input())
x = list(map(int, input().split()))
while max(x) != min(x):
    x.sort(reverse=True)
    for i in range(n-1):
        if x[i] > x[i+1]:
            x[i] -= x[i+1]
            break
print(sum(x))
