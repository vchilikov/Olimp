n = input()
b = input().split()
b25 = 0
b50 = 0
for el in b:
    if el == "25":
        b25 += 1
    elif el == "50":
        b25 -= 1
        b50 += 1
    else:
        if b50 > 0:
            b50 -= 1
            b25 -= 1
        else:
            b25 -= 3
    if b25 < 0 or b50 < 0:
        break

if b25 >= 0 and b50 >= 0:
    print("YES")
else:
    print("NO")
