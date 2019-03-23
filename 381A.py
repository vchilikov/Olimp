n = int(input())
a = list(map(int, input().split()))
score = [0, 0]
step = 1
while len(a):
    step = (step + 1) % 2
    if a[0] > a[-1]:
        score[step] += a.pop(0)
    else:
        score[step] += a.pop()
print(score[0], score[1])