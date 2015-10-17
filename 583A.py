n = int(input())
h_road = set()
v_road = set()
res = ''
for i in range(n ** 2):
    h, v = map(int, input().split())
    if h not in h_road and v not in v_road:
        h_road.add(h)
        v_road.add(v)
        res += str(i + 1) + ' '
print(res)
