d1, d2, d3 = map(int, input().split())
print(min(2 * (min(d1, d2) + d3), d1 + d2 + d3, 2 * (d1 + d2)))
