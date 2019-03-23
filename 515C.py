def f(x):
    result = 1
    while x > 0:
        result *= [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880][x % 10]
        x //= 10
    return result


n = input()
a = f(int(input()))
res = ""
for el in [7, 5, 3, 2]:
    while a % el == 0:
        a //= f(el)
        res += str(el)
print(res)
