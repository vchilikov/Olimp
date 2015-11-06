n = input()
a = input().split()
a_5 = a.count('5') // 9
a_1 = a.count('0')
if a_1 == 0:
    print(-1)
elif a_5 == 0:
    print(0)
else:
    print("5" * 9 * a_5 + "0" * a_1)