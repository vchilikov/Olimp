def compare(a, b):
    for i in range(len(b)):
        if a[i] != b[i]:
            return a[i]
    return a[-1]

n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
c = sorted(map(int, input().split()))
print(compare(a, b))
print(compare(b, c))