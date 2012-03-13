import sys
from time import time
from scipy.sparse import spdiags
from pylab import *

# C code import: see tdma.c
from tdma import tdma

def test_tdma(n):
    """Test the tridiagonal matrix solver.
    
    Arguments:
    - `n`: Size of the matrix to test
    """
    A = np.abs(randn(n, n))
    
    l = diag(A, -1)
    d = diag(A)
    u = diag(A, 1)

    l1 = hstack((l, 0))
    l2 = hstack((0, l))

    u1 = hstack((0, u))
    u2 = hstack((u, 0))
    
    x = randn(n)
    A = spdiags(vstack((l1, d, u1)),
                       [-1, 0, 1], n, n).todense()
    rhs = dot(A, x)
    tic = time()
    xhat = tdma(l2, d, u2, rhs)
    toc = time() - tic
    return norm(x - xhat), toc * 1000, norm(x - xhat) < finfo(x.dtype).eps

if __name__ == '__main__':
    n = int(sys.argv[1])
    print 'error: {0:.4g}, runtime: {1:.4g} ms, {nxn:,} elements, less than eps: {2}'.format(*test_tdma(n), nxn=n ** 2)
