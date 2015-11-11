n = input()
s = input().replace(' ', '')
while s.find('101') != -1:
    s = s.replace('101', '111')
print(len(s.replace('0', '')))
