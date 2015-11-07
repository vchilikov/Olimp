from itertools import cycle

s = set()
len_s = 0
for el in cycle('ABCD'):
    if id(el) in s:
        print(el, id(el), len_s)
        break
    else:
        s.add(id(el))
        len_s += 1
