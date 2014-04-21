cimport numpy as np
import numpy as np

cdef void solve(Py_ssize_t n, double[:] lower, double[:] diag, double[:] upper,
                double[:] rhs, double[:] x):
    cdef:
        double m
        Py_ssize_t i, im1, nm1 = n - 1

    for i in xrange(n):
        im1 = i - 1
        m = lower[i] / diag[im1]
        diag[i] -= m * upper[im1]
        rhs[i] -= m * rhs[im1]

    x[nm1] = rhs[nm1] / diag[nm1]

    for i in xrange(n - 2, -1, -1):
        x[i] = (rhs[i] - upper[i] * x[i + 1]) / diag[i]


cpdef double[:] tdma(double[:] a, double[:] b, double[:] c,
                                      double[:] d):
    cdef:
        Py_ssize_t n = b.shape[0]
        double[:] x = np.zeros(n, dtype=np.float64)
    solve(n, a, b, c, d, x)
    return x
