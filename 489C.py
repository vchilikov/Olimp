m, s = map(int, input().split())
max_res = ""
min_res = ""
if s == 0 and m == 1:
    print(0, 0)
elif s == 0 or 9 * m < s:
    print(-1, -1)
else:
    max_res = "9" * (s // 9)
    if s % 9 > 0:
        max_res += str(s % 9)
    min_res = max_res[::-1]
    max_res = max_res.ljust(m, '0')
    if len(min_res) < m:
        min_res = str(int(min_res[0]) - 1) + min_res[1:]
        min_res = "1" + min_res.rjust(m - 1, "0")
    print(min_res, max_res)
