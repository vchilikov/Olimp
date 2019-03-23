n = int(input())
a = map(int, input().split())
print(" ".join(str(el - (el - 1) % 2) for el in a))
