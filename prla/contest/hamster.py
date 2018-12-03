def hamsters(L):
    if len(L) < 2:
        if L[0] > 5000:
            return tuple((10000 - L[0], L[0]))
        else:
            return tuple((L[0], 10000 - L[0]))
    sl = sorted(L)
    li = range(len(sl))
    dl = {k: v for (k, v) in zip(li, sl)}
    d0 = {k: v for (k, v) in zip(sl, li)}
    d5 = {k: v for (k, v) in zip(
        [abs(x - 5000) for x in sl], li)}
    d10 = {k: v for (k, v) in zip(
        [10000 - x for x in sl], li)}
    lp = dl.get(d5.get(min(d5.keys())))
    le = None
    if lp > 5000:
        le = 10000 - lp
    else:
        le = lp
    fs = max(d0.keys())
    fe = max(d10.keys())
    g = None
    if fs > fe:
        g = fs
    else:
        g = fe
    return tuple((le, g))
