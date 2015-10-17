n = input()
crime = 0
policeman = 0
for el in map(int, input().split()):
    if el < 0 and policeman == 0:
        crime += 1
    else:
        policeman += el

print(crime)
