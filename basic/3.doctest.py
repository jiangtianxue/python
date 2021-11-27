from operator import floordiv, mod
# import doctest

def divide_exact(n, d):
    '''
    return the quotient and remainder of dividing n by d.
    >>> q, r = divide_exact(2021, 10)
    >>> q
    202
    >>> r
    1
    '''
    return floordiv(n, d), mod(n, d)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)