def num_to_alpha(a):
    res = ""
    while a > 0:
        a_mod = a % 26
        if a_mod == 0:
            res = "Z" + res
            a -= 26
        else:
            res = chr(64 + a_mod) + res
            a -= a_mod
        a //= 26
    return res


def alpha_to_num(a):
    return sum([(ord(a[i]) - 64) * (26 ** (len(a) - i - 1)) for i in range(len(a))])


n = int(input())
for i in range(n):
    s = input()
    if s.count("R") == 1 and s.count("C") == 1 and s[1: s.index("C")].isdigit():
        print(num_to_alpha(int(s[s.index("C") + 1:])) + s[1: s.index("C")])
    else:
        a = "".join(filter(lambda x: x.isalpha(), s))
        d = "".join(filter(lambda x: x.isdigit(), s))
        print("R" + d + "C" + str(alpha_to_num(a)))
