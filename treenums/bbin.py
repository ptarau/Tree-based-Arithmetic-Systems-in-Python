def get_digit2(n):
    assert n > 0
    d = 1 ^ (n & 1)
    return d, n >> 1


def put_digit2(dn):
    d, n = dn
    assert d in (0, 1)
    return 1 + d + n << 1


def get_bdigit(b, n):
    assert n > 0 and b > 0
    q = n // b
    d = n % b
    if d == 0:
        return b - 1, q - 1
    return d - 1, q


def put_bdigit(b, d, m):
    assert 0 <= d < b
    return 1 + d + b * m


def to_bbase(b, n):
    ds = []
    while n > 0:
        d, n = get_bdigit(b, n)
        ds.append(d)
    return ds


def from_bbase(b, ds):
    n = 0
    for d in reversed(ds):
        n = put_bdigit(b, d, n)
    return n


def bmerge(k, ns):
    nss = [to_bbase(k, n) + [k] for n in ns]
    xs = [x for xs in nss for x in xs]
    xs = xs[:-1]
    n = from_bbase(k + 1, xs)
    return n + 1


def bsplit(k, n):
    xs = to_bbase(k + 1, n-1)
    rs = []
    ns = []
    for x in xs:
        if x == k:
            r = from_bbase(k, ns)
            rs.append(r)
            ns = []
        else:
            ns.append(x)

    r = from_bbase(k, ns)
    rs.append(r)
    return rs


a = get_bdigit(3, 42)

b = put_bdigit(3, *a)

c = to_bbase(3, 42)

d = from_bbase(3, c)

e = bmerge(3, [1, 2, 3, 4, 2, 3])

f = bsplit(3, e)
