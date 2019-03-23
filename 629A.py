n = int(input())
result = 0
arr = [0] * n
for i in range(n):
    s = input()
    result += sum(range(s.count('C')))
    for j, ch in enumerate(s):
        arr[j] += ch == 'C'

for i in range(n):
    result += sum(range(arr[i]))
print(result)
