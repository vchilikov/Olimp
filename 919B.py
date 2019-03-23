k = int(input())

for a1 in range(10):
    for a2 in range(10):
        if a1 + a2 > 10:
            break
        for a3 in range(10):
            if a1 + a2 + a3 > 10:
                break
            for a4 in range(10):
                if a1 + a2 + a3 + a4 > 10:
                    break
                for a5 in range(10):
                    if a1 + a2 + a3 + a4 + a5 > 10:
                        break
                    for a6 in range(10):
                        if a1 + a2 + a3 + a4 + a5 + a6 > 10:
                            break
                        for a7 in range(10):
                            if a1 + a2 + a3 + a4 + a5 + a6 + a7 > 10:
                                break
                            for a8 in range(10):
                                if a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 > 10:
                                    break
                                if a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 == 10:
                                    k -= 1
                                    if k == 0:
                                        print(int("".join(map(str, (a1, a2, a3, a4, a5, a6, a7, a8)))))
                                        exit()
