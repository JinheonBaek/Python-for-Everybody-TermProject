import math

def zero_finder(f, start, end, eps=1E-9):
    y1 = f(start)
    y2 = f(end)

    if y1 * y2 >= 0:
        return

    x = (start + end) / 2
    y = f(x)
    while math.fabs(y) >= eps:
        if y1 * y < 0:
            end = x
        else:
            start = x
        x = (start + end) / 2
        y = f(x)

    return x

def solution_finder(f, start, end, n=100, eps=1E-9):
    #init
    n = 10000
    length = end - start
    sol = []

    for i in range(n):
        x = zero_finder(f, start + length * i / n, start + length * (i + 1) / n, eps)

        if x is not None:
            sol.append(x)

    return sol