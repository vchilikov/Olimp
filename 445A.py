n, m = map(int, input().split())
result = []
for i in range(n):
    s = ''
    for j, el in enumerate(input()):
        s += el if el == '-' else 'WB'[(i + j) % 2]
    result.append(s)
print('\n'.join(result))
