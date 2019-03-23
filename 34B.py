n, m = map(int, input().split())
print(-sum(sorted(map(lambda x: int(x) if x[0] == '-' else 0, input().split()))[:m]))
