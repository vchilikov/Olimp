n, k = map(int, input().split())
sign = 1
res = [1]
res_end = list(range(2 + k, n + 1))

while k > 0:
    res += [res[-1] + sign * k]
    sign = -1 * sign
    k -= 1

print(" ".join(map(str, res + res_end)))
