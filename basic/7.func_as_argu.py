def cube(k):
    return pow(k, 3)

def summation(n, term):
    '''
    >>> summation(5, cube)
    225
    '''
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k),  k + 1
    return total

import doctest
doctest.testmod(verbose=True)