s = input()
cnt_arr = [0]
for i in range(len(s) - 1):
    cnt_arr.append(cnt_arr[i] + (s[i] == s[i + 1]))

m = int(input())
res = []
for i in range(m):
    i, j = map(int, input().split())
    res.append(str(cnt_arr[j - 1] - cnt_arr[i - 1]))
print('\n'.join(res))