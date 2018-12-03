# def sum_no_3(lis):
#     return sum(x for x in lis if x % 10 != 3)


def sum_no_3(lis):
    return sum(*lis if [] % 10 != 3)


print(sum_no_3([1, 13, 15, 1]))
