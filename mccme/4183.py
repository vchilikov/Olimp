def nod(a, b):
    while a!=0 and b!=0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b


a, b, c, d = map(int, input().split())

a_new = a * d + b * c
b_new = b * d

if a_new == 0:
    print(0)
    exit()

sign = "-" if a_new / b_new < 0 else ""

a_new = abs(a_new)
b_new = abs(b_new)
nod_ab = nod(a_new, b_new)
a_new = a_new // nod_ab
b_new = b_new // nod_ab
celoe = (a_new // b_new)
a_new = (a_new % b_new)

if celoe == 0 and a_new == 0:
    print(0)
else:
    print(sign + (str(celoe) + " " if celoe != 0 else "") + (str(a_new) + "/" + str(b_new) if a_new != 0 else ""))