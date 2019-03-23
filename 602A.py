def input_to_10():
    n, base = map(int, input().split())
    res = 0
    for el in map(int, input().split()):
        res = el + res * base
    return res


a = input_to_10()
b = input_to_10()
if a == b:
    print('=')
elif a < b:
    print('<')
else:
    print('>')
