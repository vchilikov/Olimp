s = input()
ab_f = s.find('AB')
ba_f = s.find('BA')
if ab_f >= 0 and ba_f >= 0 and (abs(ab_f - s.rfind('BA')) > 1 or abs(ba_f - s.rfind('AB')) > 1):
    print("YES")
else:
    print("NO")
