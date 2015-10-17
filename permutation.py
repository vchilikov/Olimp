def permutation(x):
    if len(x) == 1:
        return [x]
    res = []
    for i in range(len(x)):
        for el in permutation(x[:i] + x[i + 1:]):
            res += [[x[i]] + el]
    return res


for i in permutation([1, 2, 3, 4]):
    print(i)