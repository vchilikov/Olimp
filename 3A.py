def coordinates():
    s = input()
    return " abcdefgh".index(s[0]), int(s[1])


sx, sy = coordinates()
tx, ty = coordinates()
res = ""
cnt = 0
while sx != tx or sy != ty:
    cnt += 1
    if sx < tx:
        res += "R"
        sx += 1
    elif sx > tx:
        res += "L"
        sx -= 1
    if sy < ty:
        res += "U"
        sy += 1
    elif sy > ty:
        res += "D"
        sy -= 1
    res += "\n"

print(cnt)
print(res)
