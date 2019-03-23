n = int(input())
for _ in range(n):
    l, s = int(input()),  input()
    for i in range(l // 2):
        if abs(ord(s[i]) - ord(s[l - i - 1])) not in (0, 2):
            print('NO')
            break
    else:
        print('YES')
