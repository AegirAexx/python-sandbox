''' 10001st prime
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and
    13, we can see that the 6th prime is 13.

    What is the 10001st prime number? '''


def find_prime_number(rank):
    '''Takes the rank of which prime number you want to find and returns it.'''
    prime_rank = 0
    index_i = 2
    while prime_rank < rank:
        index_j = 2
        while index_j <= index_i / index_j:
            if not index_i % index_j:
                break
            index_j += 1
        if index_j > index_i / index_j:
            prime_rank += 1
        index_i += 1
    return index_i - 1


print(find_prime_number(10001))
