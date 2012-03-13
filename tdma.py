from numpy import hstack, diag
import _tdma

def tdma(A, b):
    """Tridiagonal matrix solver using a Python C extension to make it very
    fast.
    
    Arguments:
    - `A`: Tridiagonal system of equations.
    - `b`: Right hand side of :math:`\mathbf{Ax}=\mathbf{b}`.
    """
    lower = hstack((0, diag(A, -1)))
    middle = diag(A)
    upper = hstack((diag(A, 1), 0))
    return _tdma.tdma(lower, middle, upper, b)

