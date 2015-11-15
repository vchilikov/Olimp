


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