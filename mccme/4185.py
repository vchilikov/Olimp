import math
n = int(input())
res = "Impossible"
for i in range(1, round(math.sqrt(n)) + 1):
    j = round(math.sqrt(abs(n - i ** 2)))
    if i ** 2 + j ** 2 == n and j > 0:
        res = str(i) + " " + str(j)
        break
print(res)
