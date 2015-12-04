import random
import time
a = [random.randint(0, 10**7) for _ in range(10**7)]
b = a[:]
print('------------------')
t = time.time()
res = []
a.sort()
s = set()
k = 0
while len(s) < 5:
    s.add(a[k])
    k += 1
print(time.time() - t)
print(sorted(s))

t = time.time()
s = set()
k = 0
while len(s) < 5:
    s.add(b[k])
    k += 1
max_s = max(s)
for i in range(k, len(b)):
    if b[i] < max_s and b[i] not in s:
        s.add(b[i])
        s.remove(max_s)
        max_s = max(s)
print(time.time() - t)
print(sorted(s))

# import random
#
# n = 5
# g = [random.randint(1, 100) for i in range(n)]
# f = [random.randint(1, 80) for i in range(n + 1)]
# print(g, sum(g))
# print(f, sum(f))
# sum = 0
# res = 0
# for i in range(n):
#     sum += g[i] - f[i]
#     if sum < 0:
#         sum = 0
#         res = i + 1
# sum -= f[-1]
# for i in range(2):
#     sum += g[i] - f[i]
#
# print('NO' if res == n or sum < 0 else res + 1)


    # def decorator_maker(name):
    #     def decorator(f):
    #         def wrapper(self, *args, **kwargs):
    #             print('begin ' + name)
    #             res = f(self, *args, **kwargs)
    #             print('end' + name)
    #             return res
    #         return wrapper
    #     return decorator
    #
    # class A:
    #     @decorator_maker('__init__')
    #     def __init__(self):
    #         print('A')
    #
    #     @decorator_maker('print_info')
    #     def print_info(self):
    #         return 'print_info'
    #
    # a = A()
    # print(a.print_info())

    # class Student:
    #     __obj = None
    #
    #     def __new__(cls, *args, **kwargs):
    #         if cls.__obj is None:
    #             cls.__obj = super().__new__(cls)
    #         return cls.__obj
    #
    #     def __init__(self, name):
    #         self.name = name
    #
    #
    # v = Student("Вася")
    # p = Student('Петя')
    #
    # print(v.name)
    # print(p.name)
