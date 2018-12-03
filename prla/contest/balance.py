# from collections import Counter


# def balanced(s):
#     c = Counter([x for x in s if x == '(' or x == ')'])
#     if c['('] == c[')'] and s.rfind(r"(") < s.rfind(r")"):
#         return True
#     return False

def balanced(s):
    L = 0
    R = 0
    li = list(s)
    re = []
    for x in li:
        if x == '(':
            L += 1
            re.append(x)
        elif x == ')':
            R += 1
            re.append(x)
    x = ''.join(re)
    # print()
    # print('-' * 20)
    # print('input string:', s)
    # print('-' * 20)
    # print('left count:', left)
    # print('right count:', right)
    # print('balance:', left == right and x.rfind('(') < x.rfind(')'))
    # print('clean string:', x)
    # print('-' * 20)
    return L == R and x.rfind('(') < x.rfind(')')


# print(balanced('(()())()'))
# print(balanced('(())())()'))
# print(balanced(")(')(',"))
# print(balanced("('',)"))
