def simson(f, a, b, h):
    res = f(a) + f(b)
    i = a

    while i < b:
        xr = f(i)
        m = f(i + (h / 2))

        res = res + 2 * xr + 4 * m
        i = i + h
    I = (h * res / 6)
    print(I)