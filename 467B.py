def count_char(a, b):
    return sum([1 if a[i] != b[i] else 0 for i in range(len(a))])


n, m, k = map(int, input().split())
x = [bin(int(input()))[2:].rjust(n, "0") for i in range(m + 1)]
print(sum([1 if count_char(x[i], x[m]) <= k else 0 for i in range(m)]))
