s, v1, v2, t1, t2 = map(int, input().split())
ms = 2 * t1 + s * v1 - 2 * t2 - s * v2
print(['Friendship', 'First', 'Second'][(1 if ms < 0 else 2) if ms else 0])
