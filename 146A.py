n = int(input())
s = input()
print("YES" if s.replace('7', '').replace('4', '') == '' and sum(map(int, s[:n // 2])) == sum(
    map(int, s[n // 2:])) else "NO")
