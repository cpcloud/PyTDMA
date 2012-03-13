import numpy as np
import _tdma

def tdma(A, b):
    """Tridiagonal matrix solver using a Python C extension to make it very
    fast.
    
    Arguments:
    - `A`: Tridiagonal system of equations.
    - `b`: Right hand side of :math:`\mathbf{Ax}=\mathbf{b}`.
    """
    lower = np.hstack((0, np.diag(A, -1)))
    middle = np.diag(A)
    upper = np.hstack((np.diag(A, 1), 0))
    return _tdma.tdma(lower, middle, upper, b)

