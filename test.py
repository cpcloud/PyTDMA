import sys
from time import time
from scipy.sparse import spdiags
import numpy as np

# C code import: see tdma.c
from tdma import tdma

def test_tdma(n):
    """Test the tridiagonal matrix solver.
    
    Arguments:
    - `n`: Size of the matrix to test
    """
    A = np.abs(np.random.randn(n, n))
    
    l = np.diag(A, -1)
    d = np.diag(A)
    u = np.diag(A, 1)

    l1 = np.hstack((l, 0))
    l2 = np.hstack((0, l))

    u1 = np.hstack((0, u))
    u2 = np.hstack((u, 0))
    
    x = np.random.randn(n)
    A = spdiags(np.vstack((l1, d, u1)),
                       [-1, 0, 1], n, n).todense()
    rhs = np.dot(A, x)
    tic = time()
    xhat = tdma(l2, d, u2, rhs)
    toc = time() - tic
    return (np.linalg.norm(x - xhat),
            toc * 1000,
            np.linalg.norm(x - xhat) < np.finfo(x.dtype).eps)

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print 'error: {0:.4g}, runtime: {1:.4g} ms, {nxn:,} elements, less than eps: {2}'.format(*test_tdma(n), nxn=n ** 2)
