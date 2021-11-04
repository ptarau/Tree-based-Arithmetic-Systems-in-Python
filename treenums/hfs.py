# hereditarily finite sets

class hfs(frozenset):
    def __new__(cls, *args):
        return frozenset.__new__(cls, args)

    def __repr__(self):
        s = super().__repr__()
        if s == "hfs()": return "{}"
        return s[4:-1]


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
    if n == 0: return hfs()
    return hfs(*map(n2hfs, n2ps(n)))


def hfs2n(h):
    if h == hfs(): return 0
    return ps2n(list(map(hfs2n, h)))


def s(hs):
    if hs == hfs(): return hfs(hfs())
    h = hfs()
    ds = set()
    while h in hs:
        ds.add(h)
        h = s(h)
    rs = [x for x in hs if x not in ds]
    rs.append(h)
    return hfs(*rs)


def p(hs):  # inefficient for evens
    h = hfs()
    if h in hs: return hfs(*(hs - hfs(h)))
    r=h
    while h != hs:
        r=h
        h = s(h)
    return r


# examples

empty = hfs()

one = hfs(empty)

two = hfs(empty, one)

print('empty:', empty)
print('one:', one)
print('two:', two)


def nat():
    n = 0
    while True:
        yield n
        n += 1


def take(k, gen):
    for x in gen:
        if k <= 0: break
        yield x
        k -= 1


print(hfs(*take(5, nat())))

'''
# output:

empty: {}
one: {{}}
two: {{}, {{}}}
{0, 1, 2, 3, 4}
'''

for n in range(7):
    print(n, n2hfs(n), hfs2n(n2hfs(n)))

print('-----')
a = hfs()
for i in range(10):
    b = n2hfs(i)
    print('hfs successor:', a, i, b, a == b)
    a = s(a)

print('-----!!!!! ')
a = hfs()
for i in range(30):
    b = a
    a = s(a)
    c = p(a)
    print(i, b, '==', c, b == c, hfs2n(b), '==',hfs2n(c))
