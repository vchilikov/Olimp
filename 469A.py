n = int(input())
LittleX = set(input().split()[1:])
LittleY = set(input().split()[1:])
print("I become the guy." if len(LittleX | LittleY) == n else "Oh, my keyboard!")
