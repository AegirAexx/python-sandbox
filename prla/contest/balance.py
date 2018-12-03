def balanced(s):
    lis = list(s)
    left = 0
    right = 0
    for x in lis:
        if right > left:
            return False
        elif x == '(':
            left += 1
        elif x == ')':
            right += 1
    return left == right
