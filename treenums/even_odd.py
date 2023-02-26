"""
representation of positive integers as odd-even trees
"""

def to_repr(name, x, xs):
    """
    returns readable representation for Even or Odd instances
    """
    x = x.__repr__()
    xs = "[" + ",".join(y.__repr__() for y in xs) + "]"
    return name + "(" + x + "," + xs + ")"


class Pos:
    """
    class of positive integers 1,2,3...
    """
    pass


class Unit(Pos):
    """
    has sible instace One
    """
    def __init__(self):
        pass

    def __repr__(self):
        return 'One'


One = Unit()


class Even(Pos):
    """
    class of trees corresponding to even numbers
    """
    def __init__(self, x, xs):
        self.x = x
        self.xs = xs
        self.parity = 0

    def __repr__(self):
        return to_repr('Even', self.x, self.xs)


class Odd(Pos):
    """
     class of trees corresponding to odd numbers
     """
    def __init__(self, x, xs):
        self.x = x
        self.xs = xs
        self.parity = 1

    def __repr__(self):
        return to_repr('Odd', self.x, self.xs)


def to_counters(k):
    """
    transform a number seen as in its binary representation
    as a sequence of counters for alternationg 0...0 and 1...1 blocks
    """
    def split_on(b, z):
        if z > 1 and z % 2 == b:
            x, y = split_on(b, (z - b) // 2)
            return 1 + x, y
        return 0, z

    def f(b, k):
        if k == 1: return []
        assert k > 1
        x, y = split_on(b, k)
        return [x] + f(1 - b, y)

    b = k % 2
    return b, f(b, k)


def p(k):
    """
    converts a positve integer to an even-odd tree
    """
    assert k > 0

    b, ks = to_counters(k)

    ys = list(map(p, ks))

    def g(b, ys):
        if b == 1 and ys == []: return One
        x, xs = ys[0], ys[1:]
        if b == 0: return Even(x, xs)
        return Odd(x, xs)

    return g(b, ys)


def p_(t):
    """
       converts an even-odd tree to a positve integer to
       """
    if t == One: return 1
    b, x, xs = t.parity, t.x, t.xs
    if b == 0:
        if xs == []: return 1 << p_(x)
        y, ys = xs[0], xs[1:]
        return (1 << p_(x)) * p_(Odd(y, ys))
    if xs == []: return (1 << (p_(x) + 1)) - 1
    y, ys = xs[0], xs[1:]
    return (1 << p_(x)) * (p_(Even(y, ys)) + 1) - 1


def test_even_odd():
    a = Even(One, [Odd(One, []), One])
    print(a)
    for i in range(1,20):
        t=p(i)
        j=p_(t)
        print(i,'-->',t)
        assert i == j


if __name__ == "__main__":
    test_even_odd()
