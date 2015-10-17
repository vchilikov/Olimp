n = input()
print(max(int(n), int(n[0:-1]), int(n[0:-2] + n[-1])))
