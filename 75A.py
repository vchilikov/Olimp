a = input()
b = input()
print('YES' if int(a.replace('0', '')) + int(b.replace('0', '')) == int(str(int(a) + int(b)).replace('0', '')) else 'NO')
