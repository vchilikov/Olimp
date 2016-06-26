def permutation(x):
    if len(x) == 1:
        return [x]
    res = []
    for i in range(len(x)):
        for el in permutation(x[:i] + x[i + 1:]):
            res.append((x[i],) + el)
    return res


for i in permutation((1, 2, 3, 4, 5, 6)):
    print(i)
