n, m = map(int, input().split())
candidates = [0] * n
for i in range(m):
    votes = list(map(int, input().split()))
    candidates[votes.index(max(votes))] += 1
print(candidates.index(max(candidates)) + 1)
