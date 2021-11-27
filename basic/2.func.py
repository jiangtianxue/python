from operator import floordiv, mod

def divide_exact(n, d):
    return floordiv(n, d), mod(n, d)

q, r = divide_exact(2021, 10)
print(q, '\t', r)