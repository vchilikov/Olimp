n = int(input())
res = [0, 0, 0]
for i, el in enumerate(map(int, input().split())):
    res[i % 3] += el
if res[0] == max(res):
    print('chest')
elif res[1] == max(res):
    print('biceps')
else:
    print('back')
