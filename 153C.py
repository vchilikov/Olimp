s = input()
k = int(input())
print("".join([chr((ord(ch) - 65 + k) % 26 + 65) for ch in s]))
