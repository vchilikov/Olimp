from sys import stdout, stdin


def read():
    return stdin.readline().rstrip('\n')


def f(a, b):
    return a / b + b / a


results = []
for _ in range(int(read())):
    read()
    arr = sorted(map(int, read().split()))
    i = 0
    len_arr_minus_one = len(arr) - 1
    prev_el, next_el = None, None
    min_sticks_el = None
    min_sticks = None
    while i < len_arr_minus_one:
        if arr[i] == arr[i + 1]:
            prev_el, next_el = next_el, arr[i]
            i += 2
            if prev_el and next_el:
                if not min_sticks_el:
                    min_sticks_el = (prev_el, next_el)
                    min_sticks = f(prev_el, next_el)
                    continue
                current_value = f(prev_el, next_el)
                if min_sticks > current_value:
                    min_sticks = current_value
                    min_sticks_el = (prev_el, next_el)
        else:
            i += 1
    results.append("{0} {0} {1} {1}".format(min_sticks_el[0], min_sticks_el[1]))

stdout.write('\n'.join(results) + '\n')
