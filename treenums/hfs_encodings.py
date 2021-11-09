def bsucc(bits):
    l = len(bits)
    for i, b in enumerate(bits):
        if 0 == b:
            bits[i] = 1
            break
        else:
            bits[i] = 0
            if i == len(bits) - 1:
                bits.append(1)
                break
    return bits


def n2ps(n):
    ps = []
    p = 0
    while (n):
        if n & 1: ps.append(p)
        n = n >> 1
        p += 1
    return ps


def ps2n(ps):
    return sum(1 << p for p in ps)


def n2hfs(n):
    if n == 0: return []
    return [n2hfs(p) for p in n2ps(n)]


def hfs2ps(xs):
    return list(map(hfs2n, xs))


def ps2hfs(ps):
    return list(map(n2hfs, ps))


def hfs2n(hfs):
    if hfs == []: return 0
    return ps2n(hfs2n(x) for x in hfs)


def hfs2pars(h, size=None):
    ps = []
    def walk(hs):
        ps.append(1)
        list(map(walk, hs))
        ps.append(2)
    walk(h)
    if size is not None:
        size0 = len(ps)
        if size0 < size:
            ps.extend((size - size0) * [0])
    return (ps)


def psucc(ps):
    if ps == []: return [0]
    rs = []
    i = 0
    while i < len(ps) and i == ps[i]:
        i += 1
    rs.append(i)
    rs.extend(ps[i:])
    return rs


def ptwice(ps):
    return list(map(lambda x: x + 1, ps))


def phalf(ps):
    return [p - 1 for p in ps if p > 0]


def ppred(ps):
    assert ps
    p = ps[0]
    if p == 0: return ps[1:]
    return list(range(p)) + ps[1:]


# operations on hfs

# predecessor
def p(hs):
    assert hs
    h = hs[0]
    if h == []: return hs[1:]
    rs = []
    while h:
        h = p(h)
        rs.append(h)
    rs.reverse()
    rs.extend(hs[1:])
    return rs


# succcessor
def s(hs):
    if hs == []: return [[]]
    rs = []
    i = 0
    h = []
    while i < len(hs) and h == hs[i]:
        h = s(h)
        i += 1
    rs.append(h)
    rs.extend(hs[i:])
    return rs


# double
def d(hs):
    return [s(x) for x in hs]


# half (seen as x // 2)
def h(hs):
    return [p(x) for x in hs if x]


def o(hs):
    return s(d(hs))


def i(hs):
    return d(s(hs))


# tests

def tests():
    bs = [1, 1, 1, 1, 1, 1, 1, 1]

    print(bs)
    print(bsucc(bs))
    print('')
    a = [0, 1, 2, 7, 8, 11, 13]
    print(a)
    b = psucc(a)
    print(b)
    print(psucc(b))

    print('-----')
    a = []
    for _ in range(5):
        print(a)
        a = psucc(a)

    print(ps2n(n2ps(1234567)))
    print(hfs2n(n2hfs(1234567)))

    for n in range(5):
        print(n, n2hfs(n), hfs2n(n2hfs(n)))

    one = s([])
    two = s(one)
    print('THREE', s(two))

    print('-----')
    a = []
    for i in range(10):
        print('hfs succ', i, a, hfs2n(a), a == n2hfs(i))
        a = s(a)

    print('---- PRED:')

    a = []
    for i in range(30):
        b = a
        a = psucc(a)
        c = ppred(a)
        print(i, b, c, b == c)

    print('----- s + p')

    a = []
    for i in range(30):
        b = a
        a = s(a)
        c = p(a)
        print(i, b, '==', c, b == c)

    print('----- d + r')

    a = []
    for i in range(30):
        c = d(a)
        b = h(c)

        print(i, a, '==', b, a == b)

        a = s(a)


if __name__ == "__main__":
    tests()
