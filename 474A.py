offset = -1 if input() == "R" else 1
keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
print("".join(keyboard[keyboard.index(ch) + offset] for ch in input()))
