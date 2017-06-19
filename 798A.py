s = input()
cnt = sum(s[i] != s[-i - 1] for i in range(len(s) // 2))
print('YES' if cnt == 1 or (cnt == 0 and len(s) % 2 == 1) else 'NO')
