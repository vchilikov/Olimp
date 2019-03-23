n = input()
a = input().split()[::-1]
result = []
for el in a:
    if el not in result:
        result.append(el)
print(len(result))
print(" ".join(result[::-1]))
