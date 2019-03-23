from math import sqrt

n = int(input())
for i in range(round(sqrt(n)) + 1):
    for j in range(round(sqrt(abs(n - i ** 2))) + 1):
        for k in range(round(sqrt(abs(n - i ** 2 - j ** 2))) + 1):
            l = round(sqrt(abs(n - i ** 2 - j ** 2 - k ** 2)))
            if i ** 2 + j ** 2 + k ** 2 + l ** 2 == n:
                print(i if i > 0 else "", j if j > 0 else "", k if k > 0 else "", l if l > 0 else "")
                exit()
