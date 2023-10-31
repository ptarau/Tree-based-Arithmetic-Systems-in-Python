import numpy as np
from scipy.interpolate import RBFInterpolator
import matplotlib.pyplot as plt


def iplot2d(xy, z, low=-2, hi=2):
    # edges = np.linspace(-2.0, 2.0, 101)
    # low,hi = 0, 1.0
    edges = np.linspace(low, hi, 101)
    centers = edges[:-1] + np.diff(edges[:2])[0] / 2.
    x_i, y_i = np.meshgrid(centers, centers)
    x_i = x_i.reshape(-1, 1)
    y_i = y_i.reshape(-1, 1)
    xy_i = np.concatenate([x_i, y_i], axis=1)

    print('xy_i', xy_i.shape, xy_i)

    # use RBF
    rbf = RBFInterpolator(xy, z, epsilon=2)
    z_i = rbf(xy_i)

    print('z_i', z_i.shape, z_i)

    splot(xy_i[:, 0], xy_i[:, 1], z_i)

    #return

    # plot the result
    fig, ax = plt.subplots()
    X_edges, Y_edges = np.meshgrid(edges, edges)
    lims = dict(cmap='RdBu_r', vmin=low, vmax=hi)
    mapping = ax.pcolormesh(
        X_edges, Y_edges, z_i.reshape(100, 100),
        shading='flat', **lims
    )
    ax.scatter(xy[:, 0], xy[:, 1], 100, z, edgecolor='w', lw=0.1, **lims)
    ax.set(
        title='RBF interpolation - multiquadrics',
        xlim=(low, hi),
        ylim=(low, hi),
    )
    fig.colorbar(mapping)
    plt.show()


def splot(x, y, z):
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import pyplot as plt
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = Axes3D(fig)

    ax.scatter3D(x, y, z, c=z, alpha=1, marker='d', s=150)
    plt.show()


def test_interpol():
    # 2-d tests - setup scattered data
    rng = np.random.default_rng()
    xy = rng.random((100, 2)) * 4.0 - 2.0
    z = xy[:, 0] * np.exp(-xy[:, 0] ** 2 - xy[:, 1] ** 2)

    print('xy', xy.shape)
    print('z', z.shape)

    iplot2d(xy, z)


if __name__ == "__main__":
    test_interpol()
