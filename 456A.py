n = int(input())
a_b = sorted([tuple(map(int, input().split())) for i in range(n)], key=lambda x: x[0])
alex = False
for i in range(n - 1):
    if a_b[i][1] > a_b[i + 1][1]:
        alex = True
        break

print("Happy Alex" if alex else "Poor Alex")
