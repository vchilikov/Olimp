n, d = map(int, input().split())
m_s = sorted(tuple(map(int, input().split())) for _ in range(n))
s, max_s, i = 0, 0, 0
for j in range(n):
    s += m_s[j][1]
    while m_s[j][0] - m_s[i][0] >= d:
        s -= m_s[i][1]
        i += 1
    max_s = max(max_s, s)
print(max_s)
