from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

graph = defaultdict(set)
for i in range(n - 1):
    x, y = map(int, input().split())
    graph[x - 1].add(y - 1)
    graph[y - 1].add(x - 1)

result = 0
row = {0}
prev_row = set()
while row:
    new_row = set()
    for el in row:
        children = graph[el] - prev_row
        if children:
            for next_el in children:
                if a[next_el]:
                    a[next_el] = a[el] + 1
                if a[next_el] <= m:
                    new_row.add(next_el)
        elif a[el] <= m:
            result += 1
    prev_row = row
    row = new_row

print(result)
