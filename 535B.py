n = input()
str = '4'
cnt = 0
while int(n) >= int(str[::-1]):
    cnt += 1
    i = str.find('4')
    if i == -1:
        str = '4' * (len(str) + 1)
    else:
        str = "4" * i + '7' + str[i + 1:]
print(cnt)
