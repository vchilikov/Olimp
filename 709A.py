n, b, d = map(int, input().split())
a = map(int, input().split())
result = 0
sum_a = d
for el in a:
    if el > b:
        continue
    sum_a -= el
    if sum_a < 0:
        result += 1
        sum_a = d
print(result)
