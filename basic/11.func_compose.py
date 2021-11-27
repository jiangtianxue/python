def square(x):
    return x * x

def triple(x):
    return x * 3

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

squiple = compose1(square, triple)
print(squiple(5))

tripare = compose1(triple, square)
print(tripare(4))