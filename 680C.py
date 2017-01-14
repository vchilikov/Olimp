prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 4, 9, 25, 49]
cnt = 0
for el in prime:
    print(el)
    cnt += input() == 'yes'

print('composite' if cnt > 1 else 'prime')