def boom(i):
    return ['boom!' if x % 7 == 0 or '7' in str(x) else str(x) for x in range(1, i + 1)]
