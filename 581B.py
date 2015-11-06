n = int(input())
h = map(int, input().split()[::-1])
m_h = 0
res = []
for h in h:
    if m_h < h:
        res.append('0')
        m_h = h
    else:
        res.append(str(m_h - h + 1))
print(" ".join(res[::-1]))