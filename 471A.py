def bear_elephant(a, b):
    print("Bear" if a != b else "Elephant")


l = sorted(map(int, input().split()))
if l[0] == l[1] == l[2] == l[3]:
    bear_elephant(l[4], l[5])
elif l[1] == l[2] == l[3] == l[4]:
    bear_elephant(l[0], l[5])
elif l[2] == l[3] == l[4] == l[5]:
    bear_elephant(l[0], l[1])
else:
    print("Alien")
