import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def fplot3d(X, Y, f):
    XX, YY = np.meshgrid(Y, X)
    ZZ = f(XX, YY)
    plot3d(XX, YY, ZZ)


def mplot3d(X, Y, ZZ):
    XX, YY = np.meshgrid(Y, X)
    plot3d(XX, YY, ZZ)


def plot3d(XX, YY, ZZ):
    """
    XX,YY,ZZ are 2d matrices
    """
    print('XX', XX.shape)
    print('YY', YY.shape)
    print('ZZ', ZZ.shape)
    fig = plt.figure()
    ax = Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)
    ax.plot_surface(XX, YY, ZZ, rstride=1, cstride=1, cmap=cm.viridis)
    #ax.plot_wireframe(XX, YY, ZZ)

    ax.scatter3D(XX, YY, ZZ, c='r')
    # alternatives: magma, inferno, plasma
    plt.show()


def test_mplot3d():
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-10, 10, 0.25)
    Z = np.arange(-3, 3, 0.25)

    def f(X, Y):
        return np.sqrt(X ** 2 + Y ** 2)

    fplot3d(X, Y, f)


if __name__ == "__main__":
    test_mplot3d()
