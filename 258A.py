s = input()
f = s.find('0')
print(s[:f] + s[f + 1:] if f >= 0 else s[:-1])
