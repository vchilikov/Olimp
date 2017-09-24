n, k = map(int, input().split())
ids = list(map(int, input().split()))
cnt = 1
while k > cnt:
    k -= cnt
    cnt += 1
print(ids[k - 1])
