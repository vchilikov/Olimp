insert = """
INSERT INTO category(
            id, name, parent_category_id)
    VALUES ({0}, '{1}', {2});
"""

with open('key.txt', 'r') as f:
    parent_id = 0
    id = 0
    for el in f:
        el = el.strip()
        if el == '':
            continue
        id += 1
        if el[0] == '*':
            parent_id = id
            print(insert.format(id, el[1:], 'null'))
        else:
            print(insert.format(id, el, parent_id))


# class Record:
#     pass
#
#
# class Integer(Record):
#     def sql(self):
#         return 'integer'
#
#
# class Str(Record):
#     def __init__(self, size):
#         self.size = size
#
#     def sql(self):
#         return 'varchar(%d)' % self.size
#
#
# class MyTable:
#     height = Integer()
#     width = Integer()
#     path = Str(128)
#
#     @classmethod
#     def sql(cls):
#         attrs = [(key, val) for key, val in cls.__dict__.items() if isinstance(val, Record)]
#         retString = 'CREATE TABLE %s (\n' % cls.__name__.lower()
#         retString += ',\n'.join(['      %s %s' % (x, y.sql()) for x, y in attrs])
#         retString += '\n)'
#         return retString
#
#
# print(MyTable.sql())

# class FixAttr(type):
#     def __setattr__(self, key, value):
#         if type(getattr(self, key)) == type(value):
#             self.__dict__[key] = value
#         else:
#             raise TypeError
#
#     def __new__(msc, name, bases, dct):
#         dct['__setattr__'] = msc.__setattr__
#         return type.__new__(msc, name, bases, dct)
#
#
# class Image(metaclass=FixAttr):
#     height = 0
#     width = 0
#     path = '/tmp'
#     size = 0
#
#
# img = Image()
# img.height = 340
# print(img.height)
# img.path = '/tmp/x00.jpeg'
# print(img.path)
# img.path = '12345'
# img.path = 320

# class RegBase(type):
#     def __iter__(cls):
#         return iter(cls._instances)
#
#
# class Reg(metaclass=RegBase):
#     _instances = []
#
#     def __init__(self, name):
#         self.name = name
#         self._instances.append(self)
#
#
# x = Reg(name='x')
# y = Reg(name='y')
# z = Reg(name='z')
#
# for i in Reg:
#     print(i.name)

# class Singleton:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#     def __init__(self, a):
#         self.a = a
#
# s1 = Singleton(a=10)
# s2 = Singleton(a=5)
#
# if s1 == s2:
#     print('Yes')
# else:
#     print('No')
#
# print(s1.a)
# print(s2.a)

# class Property(object):
#     def __init__(self, initval=None, name='var'):
#         self.val = initval
#         self.name = name
#
#     def __get__(self, obj, objtype):
#         return self.val
#
#     def __set__(self, obj, val):
#         if type(self.val) == type(val):
#             self.val = val
#         else:
#             raise TypeError
#
#
# class Image(object):
#     height = Property(0)
#     width = Property(0)
#     path = Property('/tmp/')
#     size = Property(0)
#
#
# img = Image()
# img.height = 340
# print(img.height)
# img.path = '/tmp/x00.jpeg'
# print(img.path)
# img.path = 320

# def chain(*args):
#     for i in args:
#         for el in i:
#             yield el
#
#
# i1 = iter([1, 2, 3])
# i2 = iter([4, 5])
# i3 = iter([9])
# c = chain(i1, i2, i3)
#
#
#
# print(list(c))
#



# def f(*args):
#     res = 0
#     for el in args:
#         if not hasattr(el, '__len__'):
#             res += el
#         else:
#             res += sum(el)
#     return res
#
#
#
# print(f(1, 2, 3))
#
# print(f([1, 2, 3]))
#
# print(f((3, 5, 6)))
#
# print(f(3, (5, 6)))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# k = 1
# print([a[i:i+k] for i in range(0, len(a), k)])
#
#
#
# a = [[1, 2, 3, 4],
#      [1, 2, 3, 4],
#      [1, 2, 3, 4]]
#
# for el in a:
#     el += [sum(el)]
#
# a += [[0] * len(a[0])]
# for j in range(len(a[0]) - 1):
#     res = 0
#     for i in range(len(a) - 1):
#         res += a[i][j]
#     a[-1][j] = res
#
# print(str(a))

# import time

# a = [1, 2, 3]
# b = [5, 6, 7]
# d = dict(zip(a, b + [None] * (len(a) - len(b))))
# print(dict(zip(a, b + [None] * (len(a) - len(b)))))
#
# print({v: k for k, v in d.items()})

#
# def decorator(f):
#     def wrapper(*args, **kwargs):
#         t = time.time()
#         res = f(*args, **kwargs)
#         print(time.time() - t)
#         return res
#
#     return wrapper
#
#
# @decorator
# def func(sec):
#     time.sleep(sec)
#
#
# func(10)
#
# a = 5
# print(isinstance(a, int))
# print(issubclass(bool, int))
#

# import random
# import time
# import gc
# a = [random.randint(0, 10**7) for _ in range(10**7)]
#
# print('------------------')
# t = time.time()
# res = []
# a.sort()
# s = set()
# k = 0
# while len(s) < 1000:
#     s.add(a[k])
#     k += 1
# print(time.time() - t)
# print(sorted(s))
#
# t = time.time()
# s = set()
# k = 0
# while len(s) < 10:
#     s.add(a[k])
#     k += 1
# max_s = max(s)
# for el in a:
#     if el < max_s and el not in s:
#         s.add(el)
#         s.remove(max_s)
#         max_s = max(s)
# print(time.time() - t)
# print(sorted(s))

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
