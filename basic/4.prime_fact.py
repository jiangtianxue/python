def prime_factors(n):
    '''
    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(858)
    2
    3
    11
    13
    '''
    while n>1:
        k = smallest_prime_factor(n)
        # print(k)
        n = n // k
        print(k)


def smallest_prime_factor(n):
    k = 2
    while n % k != 0:
        k = k + 1
    return k 

prime_factors(858)