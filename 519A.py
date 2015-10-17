weightFigure = {'q': -9, 'r': -5, 'b': -3, 'n': -3, 'p': -1, 'k': 0,
                'Q': 9, 'R': 5, 'B': 3, 'N': 3, 'P': 1, 'K': 0,
                '.': 0}
weightPosition = 0
for _ in range(8):
    weightPosition += sum(weightFigure[ch] for ch in input())

if weightPosition > 0:
    print("White")
elif weightPosition == 0:
    print("Draw")
else:
    print("Black")
