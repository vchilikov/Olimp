n = input()
s = [[], [], [0]]
s_1 = 0
for el in map(int, input().split()):
    if el < 0:
        s[0].append(el)
    elif el > 0:
        s[1].append(el)

if len(s[1]) == 0:
    s[1].append(s[0].pop())
    s[1].append(s[0].pop())

if len(s[0]) % 2 == 0:
    s[2].append(s[0].pop())

for el in s:
    print(len(el), " ".join(map(str, el)))
