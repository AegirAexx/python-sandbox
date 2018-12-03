def gymnastics(lis):
    if len(lis) > 2:
        lis = sorted(lis)
        del lis[-1]
        del lis[0]
    return sum(lis) // len(lis)
