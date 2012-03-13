#!/usr/bin/env python

# Builtins
from time import time

# numpy/scipy
from numpy import abs, diag, hstack, vstack, dot, finfo
from numpy.random import randn
from numpy.linalg import norm
from scipy.sparse import spdiags

# solver
from tdma import tdma

def test_tdma(n):
    """Test the tridiagonal matrix solver.
    
    Arguments:
    - `n`: Size of the matrix to test
    """
    A = randn(n, n)
    l = hstack((diag(A, -1), 0))
    d = diag(A)
    u = hstack((0, diag(A, 1)))
    
    x = randn(n)
    A = spdiags(vstack((l, d, u)),
                [-1, 0, 1], n, n).todense()
    
    rhs = dot(A, x)
    
    tic = time()
    xhat = tdma(A, rhs)
    toc = time() - tic
    print 'error: {0:.4g}, runtime: {1:.4g} ms, {nxn:,} elements'.format(norm(x - xhat), toc * 1000, nxn=n ** 2)
    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='PyTDMA testing script.')
    parser.add_argument('n',
                        metavar='N',
                        type=int,
                        nargs=1,
                        help='an integer indicating the number of rows and columns of the testing matrix')
    args = parser.parse_args()
    test_tdma(args.n[0])
    
    
