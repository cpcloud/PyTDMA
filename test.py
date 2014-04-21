#!/usr/bin/env python

import argparse
import time

import numpy as np
import scipy.sparse

# solver
from tdma import tdma


def test_tdma(n):
    """Test the tridiagonal matrix solver.

    Parameters
    ----------
    n : int
        Size of the matrix to test
    """
    l = np.hstack((np.random.randn(n - 1), 0))
    d = np.random.randn(n)
    u = np.hstack((0, np.random.randn(n - 1)))

    x = np.random.randn(n)
    A = scipy.sparse.spdiags(np.vstack((l, d, u)),
                             [-1, 0, 1], n, n).todense()

    b = A.dot(x)

    tic = time.time()
    xhat = tdma(A, b)
    toc = time.time()

    fmt = 'error: {0:.4g}, runtime: {1:.4g} ms, {2:,} elements'
    print(fmt.format(np.linalg.norm(x - xhat), (toc - tic) * 1000, n ** 2))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='PyTDMA testing script.')
    parser.add_argument('n', type=int, nargs=1,
                        help='an integer indicating the number of rows and '
                        'columns of the testing matrix')
    args = parser.parse_args()
    test_tdma(args.n[0])
