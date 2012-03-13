import sys
from time import time
from scipy.sparse import spdiags, csc_matrix, csr_matrix
from scipy.sparse.linalg import spsolve
from pylab import *

# C code import: see tdma.c
from tdma import tdma

def test_tdma(n):
    """Test the tridiagonal matrix solver.
    
    Arguments:
    - `n`: Size of the matrix to test
    """
    A = np.abs(randn(n, n))
    l = hstack((diag(A, -1), 0))
    l2 = hstack((0, diag(A, -1)))
    d = diag(A)
    u = hstack((0, diag(A, 1)))
    u2 = hstack((diag(A, 1), 0))
    x = randn(n)
    A = spdiags(vstack((l, d, u)),
                       [-1, 0, 1], n, n).todense()
    rhs = dot(A, x)
    tic = time()
    xhat = tdma(l2, d, u2, rhs)
    toc = time() - tic
    return norm(x - xhat), toc * 1000, norm(x - xhat) < finfo(x.dtype).eps

if __name__ == '__main__':
    n = int(sys.argv[1])
    o = test_tdma(n)
    print 'error: {0:.4g}, runtime: {1:.4g} ms, {nxn:,} elements, less than eps: {2}'.format(*o, nxn=n ** 2)
