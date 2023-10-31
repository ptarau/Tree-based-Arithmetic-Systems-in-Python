from cantor2 import *
from mplot3d import *
from interpol import *

import scipy as sp
from scipy.interpolate import RBFInterpolator


def graph2graphon(es):
    vs = sorted(set(k for (i, j) in es for k in (i, j)))
    # print(vs)
    L = len(vs) - 1
    vs_ = [v / L for v in vs]
    es_ = [(i / L, j / L) for (i, j) in es]

    ks = [pair(i, j) for (i, j) in es]
    print(ks)

    les = list(map(list, es))

    print('LES:', les, '\n', ks)

    # fplot3d(vs, vs, pair)

    M = pair(L, L)
    print('M:', M)

    Z = np.zeros((L + 1, L + 1)) - 1 / L
    for (i, j) in es:
        Z[i, j] = pair(i, j) / M

    print(Z)

    def cpair(x, y):

        x = L * x
        y = L * y

        z = pair(x, y)
        return z / M

    mplot3d(vs_, vs_, Z)

    # iplot2d(np.array(les), np.array(ks), low=-1, hi=1)

    # return

    fplot3d(vs_, vs_, cpair)

    for (i, j) in es:
        print((i, j), '-->', pair(i, j))
    print()

    for x, y in es_:
        print((x, y), '->', cpair(x, y))


def test():
    es = [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 2),
        (2, 3),
        (2, 0),
        (3, 1),
        (0, 4),
        (4, 0),
        (4, 4)
    ]
    graph2graphon(es)
    return

    n = 6
    gs = [(i, j) for i in range(n) for j in range(n)]
    gs_ = [(j, i) for i in range(n) for j in range(n)]
    graph2graphon(gs + gs_)


if __name__ == "__main__":
    test()
