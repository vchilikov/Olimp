import os
from datetime import datetime
import resource

import psutil as psutil

start = datetime.now()

# n = int(input())
# c = list(map(int, input().split()))
# a = list(map(lambda x: int(x) - 1, input().split()))
n = 5000
c = [1] * n
a = [i + 1 for i in range(n)]
a[n - 1] = 0

position = [set() for i in range(n)]
for i in range(n):
    next_pos = i
    while next_pos not in position[i]:
        position[i].add(next_pos)

        next_pos = a[next_pos]

for i in range(n - 1):
    if not position[i]:
        continue
    for j in range(i + 1, n):
        if not position[j]:
            continue
        intersection = position[i] & position[j]
        if intersection:
            position[i] = intersection
            position[j] = None

process = psutil.Process(os.getpid())
print(process.memory_info().rss)

res = 0
for el in position:
    if not el:
        continue
    res += min(c[i] for i in el)

print(res)
print(datetime.now() - start)



usage = resource.getrusage(resource.RUSAGE_SELF)

for name, desc in [
    ('ru_utime', 'User time'),
    ('ru_stime', 'System time'),
    ('ru_maxrss', 'Max. Resident Set Size'),
    ('ru_ixrss', 'Shared Memory Size'),
    ('ru_idrss', 'Unshared Memory Size'),
    ('ru_isrss', 'Stack Size'),
    ('ru_inblock', 'Block inputs'),
    ('ru_oublock', 'Block outputs'),
    ]:
    print('%-25s (%-10s) = %s' % (desc, name, getattr(usage, name)))

process = psutil.Process(os.getpid())
print(process.memory_info().rss)