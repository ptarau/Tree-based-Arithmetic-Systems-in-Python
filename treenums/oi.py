def o(x):
    return (0, x)


def i(x):
    return (1, x)


def s(x):
    if 0 == x: return (0, x)
    t, v = x
    if 0 == t: return (1, v)
    return (0, s(v))


def p(x):
    if (0, 0) == x: return 0
    t, v = x
    if 1 == t: return (0, v)
    return (1, p(v))


def n2b(n):
    if 0 == n: return 0
    if 0 == n % 2 : return (1, n2b(n // 2-1))
    return (0, n2b((n - 1) // 2))


def b2n(x):
    if 0==x: return 0
    t,v=x
    if 0==t: return 2*b2n(v)+1
    return 2*(b2n(v))+2


x = 0
m = 10
for i in range(m):
    print(i,'->', x, n2b(i), b2n(x))
    x = s(x)

print('')
for i in range(m):
    x = p(x)
    print((m - i - 1), '->',x)
