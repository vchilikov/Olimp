sh, sm = map(int, input().split(':'))
th, tm = map(int, input().split(':'))
sh -= th
sm -= tm
if sm < 0:
    sm += 60
    sh -= 1
if sh < 0:
    sh += 24
print(str(sh).zfill(2) + ':' + str(sm).zfill(2))
