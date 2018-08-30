import math

from scipy.stats import truncnorm
from sqlalchemy import Column, Integer, Text, Numeric
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_truncated_normal(mean=50, sd=12, low=1, upp=99, count=1000):
    x = truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
    for el in x.rvs(count):
        yield math.trunc(round(el))


engine = create_engine('sqlite:///:memory:', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Banner(Base):
    __tablename__ = 'banners'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    weight = Column(Numeric())


Base.metadata.create_all(engine)


for i in range(0, 1000):
    buff = []
    for weight in get_truncated_normal():
        buff.append(Banner(name='asdf', weight=weight))
    session.bulk_save_objects(buff)


our_banner = session.query(Banner).filter_by(name='asdf').first()
print(our_banner.name)


# import requests
# from datetime import datetime, timedelta
#
# cnt = 0
# while True:
#     cnt += 1
#     if cnt % 100 == 0:
#         print(cnt)
#     start = datetime.now()
#     # r = requests.get('https://weather.rambler.ru/health/')
#     # cookies = {'react_split': '1'}
#     # r = requests.get('https://weather.rambler.ru/heartbeat.json', cookies=cookies)
#     r = requests.get('https://weather.rambler.ru/api/v3/mixin/?url_path=v-tveri')
#     # r = requests.get('http://stage.weather.rambler.ru/api/v3/mixin/?format=json&url_path=v-tveri')
#     # r = requests.get('https://api.weather.rambler.ru/api/v3/mixin/?profile_token=dlweuhskdjfdffoiwehfpiuwhefdpiwhefduph&profile')
#     now = datetime.now()
#     if now - start > timedelta(seconds=0.5):
#         print(now - start)
#         # print(r.text)

# import aiohttp
# import asyncio
# import time
# sem = asyncio.Semaphore(5)
#
#
# async def fetch(url):
#     async with sem:
#         print(url)
#         t = time.time()
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as response:
#                 print(response.status)
#         print((time.time() - t))
#
# pik_url = 'http://ugradirect.ru/?asdf={0}'
#
#
# async def main(loop):
#     await asyncio.wait([fetch(pik_url.format(i)) for i in range(100)])
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main(loop))

# import math
#
# for i in range(10000000000):
#     math.sqrt(i)
# import requests
# from bs4 import BeautifulSoup
# from datetime import date
#
#
# class MoonCalendarParser:
#     url_template = 'http://luna.rio-mix.com/lunnyj-kalendar-na-{0}-{1}-goda-moskva.html'
#     months = ['yanvar', 'fevral', 'mart', 'aprel', 'maj', 'iyun', 'iyul', 'avgust', 'sentyabr', 'oktyabr', 'noyabr',
#               'dekabr']
#
#     def __init__(self, year):
#         self.year = year
#
#     def urls(self):
#         return (self.url_template.format(month, self.year) for month in self.months)
#
#     def numbered_urls(self):
#         return zip(range(1, 13), self.urls())
#
#     @staticmethod
#     def load_table_rows_by_url(url):
#         r = requests.get(url)
#         soup = BeautifulSoup(r.text, "html.parser")
#         table = soup.find('table', {'id': 'table'})
#         table_body = table.find('tbody')
#         rows = table_body.find_all('tr')
#         for row in rows[1:]:
#             yield [td.text.strip() for td in row.find_all('td')]
#
#     def days_parser(self):
#         for month, url in self.numbered_urls():
#             for row in self.load_table_rows_by_url(url):
#                 d = date(self.year, month, int(row[1]))
#                 yield [d] + row[2:]
#
#     def parse(self):
#         for row in self.days_parser():
#             print(row[0].strftime('%d.%m.%Y'), row[1:])
#
#
# MoonCalendarParser(2018).parse()

# a = [10, 5, 2,  3, 7, 5]
# c = 12
# s = {}
# res = []
# for i, el in enumerate(a):
#     if c - el in s.keys():
#         for j in s[c - el]:
#             res.append((j, i))
#     s[el] = s.get(el, []) + [i]
#
# l, r = min(res, key=lambda x: abs(x[0] - x[1]))
# print(a[l], a[r])

# import re
# from bs4 import BeautifulSoup
#
# html_doc = """фывап https://music.yandex.ru/feed
# dfgdfg
# sdfasda https://music.yandex.ru/feed asdasd sadasdasd gdsf
# gsdfgs
# https://music.yandex.ru/feed
# <a href="http://codeforces.com/problemset/page/3?order=BY_SOLVED_DESC" target="_blank">http://codeforces.com/problemset/page/3?order=BY_SOLVED_DESC</a>
# dfsgsdfgsdfgsdsdfgsdfgdsfпап
# asdhttps://www.google.ru/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8 asdas
# asdasd<a href="http://google.com/problemset/page/3?order=BY_SOLVED_DESC" target="_blank">http://codeforces.com/problemset/page/3?order=BY_SOLVED_DESC</a>asdasd
# """
#
#
# html_doc = """
# фывап <a href="https://music.yandex.ru/feed" target="_blank">https://music.yandex.ru/feed</a>
# dfgdfg
# sdfasda <a href="https://music.yandex.ru/feed" target="_blank">https://music.yandex.ru/feed</a> asdasd sadasdasd gdsf
# gsdfgs
# <a href="https://music.yandex.ru/feed" target="_blank">https://music.yandex.ru/feed</a>
# <a href="http://codeforces.com/problemset/page/3?order=BY_SOLVED_DESC" target="_blank">http://codeforces.com/problemset/page/3?order=BY_SOLVED_DESC</a>
# dfsgsdfgsdfgsdsdfgsdfgdsfпап
# asd<a href="https://www.google.ru/webhp?sourceid=chrome-instant&amp;ion;=1&amp;espv;=2&amp;ie;=UTF-8" target="_blank">https://www.google.ru/webhp?sourceid=chrome-instant&amp;ion;=1&amp;espv;=2&amp;ie;=UTF-8</a> asdas
# asdasd<a href="http://google.com/problemset/page/3?order=BY_SOLVED_DESC" target="_blank">http://codeforces.com/problemset/page/3?order=BY_SOLVED_DESC</a>asdasd
# """
# buff = []
# soup = BeautifulSoup(html_doc, 'html.parser')
# for i, el in enumerate(soup.find_all('a')):
#     buff.append(str(el))
#     el.replace_with('{link%i}' % i)
#
# html_doc = str(soup)
# print(html_doc)
#
# urls = re.compile(
#     r"(((http|ftp|https):\/{2})+(([0-9a-z_-]+\.)+(aero|asia|biz|cat|com|coop|edu|gov|info|int|jobs|mil|mobi|museum|name|net|org|pro|tel|travel|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cu|cv|cx|cy|cz|cz|de|dj|dk|dm|do|dz|ec|ee|eg|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mn|mn|mo|mp|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|nom|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ra|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sj|sk|sl|sm|sn|so|sr|st|su|sv|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw|arpa)(:[0-9]+)?((\/([~0-9a-zA-Z\#\+\%@\.\/_-]+))?(\?[0-9a-zA-Z\+\%@\/&\[\];=_-]+)?)?))\b", re.MULTILINE | re.UNICODE)
# html_doc = urls.sub(r'<a href="\1" target="_blank">\1</a>', html_doc)
#
# for i, el in enumerate(buff):
#     html_doc = html_doc.replace('{link%i}' % i, el)
#
# print(html_doc)

# s = """
# server {
#     listen       80;
#     server_name  www.%s;
#     return       301 http://%s$request_uri;
# }
# """
# res = []
# while True:
#     host_name = input()
#     if host_name == 'end':
#         break
#     res.append(s % (host_name, host_name))
#
# print("\n".join(res))


# def b(**kwargs):
#     print(kwargs)
#
# class Cls():
#     a = b
#
# Cls.a(a=123)

# from random import randint, seed
# seed()
# array = [randint(0, 10) - 5 for i in range(10)]
# print(array)
# m, k = 0, 0
# res = array[0]
# for i in range(0, len(array)):
#     for j in range(i, len(array)):
#         if sum(array[i:j+1]) > res:
#             m, k = i, j
#             res = sum(array[i:j+1])
# print(m, k, res)
# import dis
# import inspect
#
#
# def f():
#     print('121212')
#
# print(dis.dis(f))


# def binary_search(arr, x):
#     l, r = 0, len(arr) - 1
#     if r < 0:
#         return -1
#     while (r - l) > 1:
#         i = (l + r) // 2
#         if x <= arr[i]:
#             r = i
#         else:
#             l = i
#     if arr[l] == x:
#         return l
#     elif arr[r] == x:
#         return r
#     else:
#         return -1
#
#
# print(binary_search([1, 1, 1, 1, 1, 1], 1))

# for i in range(3, 21):
#     list_range = list(range(2, i))
#     sum_range = sum(list_range)
#     if sum_range >= 100:
#         print('#{0}, sum={1}, {2}'.format(len(list_range), sum_range, list_range))
#         break

# name = input('Как тебя зовут? ')
# while True:
#     exit_name = input('Ты уходишь(да/нет)?')
#     if exit_name.upper() == 'НЕТ' or exit_name.upper() == 'ДА':
#         break
# for i in range(5):
#     if exit_name == 'нет':
#         print('Приветстви #{num}. Привет, {name}!'.format(num=i, name=name))
#     else:
#         print('Прощание #{num}. Пока, {name}!'.format(num=i, name=name))
#


# class Infinity:
#     def __init__(self):
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.i += 1
#         return self.i
#
# for i in Infinity():
#     print(i)

# from datetime import datetime
# from random import randint
#
#
# def timer(f):
#     def wrapper(*args, **kwargs):
#         t = datetime.now()
#         res = f(*args, **kwargs)
#         print(datetime.now() - t)
#         return res
#
#     return wrapper
#
#
# @timer
# def load_data():
#     max_int = 1000000
#     length = 30000000
#     array1 = [i % max_int for i in range(length)]
#     array2 = [i % max_int for i in range(length)]
#     array3 = [i % max_int for i in range(length)]
#     return array1, array2, array3
#
# @timer
# def unique_data(array1, array2, array3):
#     return list(set(array1 + array2 + array3))
#
# print('Загрузка данных')
# arr1, arr2, arr3 = load_data()
# print('Данные загружены')
# print('Обработка данных')
# arr = unique_data(arr1, arr2, arr3)
# print('Данные обработаны')
#
#


# from datetime import datetime
#
#
# def timer(k):
#     def wrapper1(f):
#         def wrapper2(*args, **kwargs):
#             t = datetime.now()
#             res = f(*args, **kwargs)
#             print(k * (datetime.now() - t))
#             return res
#         return wrapper2
#     return wrapper1
#
# @timer(10)
# def circle(l):
#     j = 1
#     for i in range(l):
#         j += 1
#
# circle(50000000)


# from random import randint, seed
# seed()
# array = [randint(0, 10) - 5 for i in range(10)]
# print(array)
# m, k = 0, 0
# res = array[0]
# for i in range(0, len(array)):
#     for j in range(i, len(array)):
#         if sum(array[i:j+1]) > res:
#             m, k = i, j
#             res = sum(array[i:j+1])
# print(m, k, res)

# from random import randint, seed
# from time import time
#
#
# def var1(a, power):
#     res = []
#     for i in range(len(a) - 1):
#         if i % 1000 == 0:
#             print(i, res)
#         if a[i] is None:
#             continue
#         group = []
#         for j in range(i + 1, len(a)):
#             if a[j] and len(a[i].intersection(a[j])) >= power:
#                 group.append(j)
#                 a[j] = None
#         if group:
#             group.append(i)
#             res.append(group)
#     return res
#
#
# def soft_clusterization(a, power):
#     b = [set() for i in range(len(a))]
#
#     for i in range(len(a)):
#         for el in a[i]:
#             b[el].add(i)
#
#     res = []
#     for i in range(len(a) - 1):
#         if i % 1000 == 0:
#             print(i, res)
#         if a[i] is None:
#             continue
#
#         s = set()
#         for url in a[i]:
#             s.update(b[url])
#
#         group = []
#         for j in s:
#             if j > i and a[j] and len(a[i].intersection(a[j])) >= power:
#                 group.append(j)
#                 a[j] = None
#         if group:
#             group.append(i)
#             res.append(group)
#     return res
#
#
# def hard_clusterization(a, power):
#     b = [set() for i in range(len(a))]
#
#     for i in range(len(a)):
#         for el in a[i]:
#             b[el].add(i)
#
#     res = dict()
#     for i in range(len(a) - 1):
#         if i % 1000 == 0:
#             print(i, res)
#
#         s = set()
#         for url in a[i]:
#             s.update(b[url])
#
#         for j in s:
#             if j > i:
#                 intersect = a[i].intersection(a[j])
#                 if len(intersect) >= power:
#                     urls = tuple(sorted(intersect))
#                     if urls in res:
#                         res[urls].update({i, j})
#                     else:
#                         res[urls] = {i, j}
#
#     print(res)
#     result = dict()
#     for key, value in res.items():
#         len_key = len(key)
#         if len_key in result:
#             result[len_key].update({key: value})
#         else:
#             result[len_key] = {key: value}
#     return result
#
# n = 400000
# power = 4
# a = []
#
# seed()
# for _ in range(n):
#     s = set()
#     while len(s) < 10:
#         s.add(randint(0, n - 1))
#     a.append(s)
#
# print('-----------------------')
# # c = a.copy()
# # t = time()
# # print(var1(c, power))
# # print(time() - t)
# print('-----------------------')
# c = a.copy()
# t = time()
# soft_clusterization(c, power)
# print(time() - t)
# print('-----------------------')
# c = a.copy()
# t = time()
# print(hard_clusterization(c, power))
# print(time() - t)


# a = []
#
# print(a.__iter__())
# print(a.__iter__())
# print(iter(a))
# print(iter(a))
#
# insert = """
# INSERT INTO category(
#             id, name, parent_category_id)
#     VALUES ({0}, '{1}', {2});
# """
#
# with open('key.txt', 'r') as f:
#     parent_id = 0
#     id = 0
#     for el in f:
#         el = el.strip()
#         if el == '':
#             continue
#         id += 1
#         if el[0] == '*':
#             parent_id = id
#             print(insert.format(id, el[1:], 'null'))
#         else:
#             print(insert.format(id, el, parent_id))


# class Record:b = a[:]
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
