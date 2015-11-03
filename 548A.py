s = input()
k = int(input())
if len(s) % k != 0:
    print("NO")
    exit()
for i in range(0, len(s), len(s) // k):
    ss = s[i:i + len(s) // k]
    if ss[0:(len(ss) + 1) // 2] != ss[-((len(ss) + 1) // 2):][::-1]:
        print("NO")
        break
else:
    print("YES")
