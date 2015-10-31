a, b, c, d = map(int, input().split())

misha = max(3 * a // 10, a - a * c // 250)
vasya = max(3 * b // 10, b - b * d // 250)

if misha > vasya:
    print("Misha")
elif misha < vasya:
    print("Vasya")
else:
    print("Tie")