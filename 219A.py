k = int(input())
s = input()
new_s = ""
for ch in set(s):
    new_s += ch * (s.count(ch) // k)
print(new_s * k if len(s) == len(new_s) * k else -1)
