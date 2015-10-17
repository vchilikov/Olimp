t = ""
for ch in input():
    t += ch if ch < "5" else str(9 - int(ch))
print("9" + t[1:] if t[0] == "0" else t)
