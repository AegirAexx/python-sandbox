def palindrome(a, b):
    x = a
    y = []
    while True:
        c = x // b
        B = x % b
        y.append(str(B))
        x = c
        if x < 1:
            break
    return ''.join(y) == ''.join(list(reversed(y)))
