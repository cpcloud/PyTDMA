#!/usr/bin/env python

import argparse
from time import time

import numpy as np
import scipy

from sklearn.utils.extmath import safe_sparse_dot, norm

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
                             [-1, 0, 1], n, n)

    b = safe_sparse_dot(A, x)

    tic = time()
    xhat = tdma(A, b)
    toc = time() - tic

    print 'error: {0:.4g}, runtime: {1:.4g} ms, {2:,} elements'.format(norm(x - xhat),
                                                                       toc * 1000,
                                                                       n ** 2)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='PyTDMA testing script.')
    parser.add_argument('n',
                        metavar='N',
                        type=int,
                        nargs=1,
                        help='an integer indicating the number of rows and columns of the testing matrix')
    args = parser.parse_args()
    test_tdma(args.n[0])
