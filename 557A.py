n = int(input())
min1, max1 = map(int, input().split())
min2, max2 = map(int, input().split())
min3, max3 = map(int, input().split())
n1, n2, n3 = min1, min2, min3
n1 = min(max1, n - n2 - n3)
n -= n1
n2 = min(max2, n - n3)
n -= n2
n3 = n
print(n1, n2, n3)