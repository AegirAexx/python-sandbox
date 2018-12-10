from itertools import product, combinations
# from pprint import pprint


def insert_operators(seq, target):
    # Taking apart the sequence and formating it for itertools.combinations.
    container = []
    for x in seq:
        one, two, three = str(x) + '+', str(x) + '-', str(x) + ''
        container.append([one, two, three])
    container[-1] = [str(seq[-1])]

    # Create the combinations.
    com = list(combinations(product(*container), 1))

    # Create a workable list with string equations.
    eq = list([''.join(x[0]) for x in com])
    # pprint(eq)
    for y in eq:
        acc = 0
        num = 0
        flag = 1
        # print('-------------')
        # print('eq:', y)
        for z in reversed(y):
            if z != '+' and z != '-':
                num += flag * int(z)
                flag *= 10
            elif z == '+':
                acc += num
                flag = 1
                num = 0
            else:
                acc -= num
                flag = 1
                num = 0
        acc += num
        # print('acc:', acc)
        # print('num:', num)
        if acc == target:
            return y + '=' + str(acc)
    return None


# print(insert_operators([14, 8, 2, 17, 5, 9], 83))
# "14+82-17-5+9=83"
print(insert_operators([34, 9, 82, 21, 32], 32850))
# "34982-2132=32850"
# print(insert_operators([1, 2, 3], 5))
# None
