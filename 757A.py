s = input()
print(min(min(s.count(el) for el in 'Blbsr'), s.count('a') // 2, s.count('u') // 2))
