r = int(input())
arr = list(map(int, input().split()))
cnt = 0
while len(arr):
    arr = [x for x in arr if x >= r]
    if len(arr):
        r = min(arr) + 3
        cnt += 1
print(cnt)
