def make_adder(n):
    """
    >>> adder_three = make_adder(3)
    >>> adder_three(4)
    7
    """
    def adder(k):
        return k + n
    
    return adder

import doctest
doctest.testmod(verbose=True)

# 这种合并的调用方式也是可以的
print(make_adder(17)(13))

