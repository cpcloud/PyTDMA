cimport numpy as np
import numpy as np

cdef void solve(int n, double* lower,
                double* diag, double* upper,
                double* rhs, double* x):
    cdef double m
    cdef int i, im1, nm1 = n - 1
    for i in xrange(n):
        im1 = i - 1
        m = lower[i] / diag[im1]
        diag[i] -= m * upper[im1]
        rhs[i] -= m * rhs[im1]

    x[nm1] = rhs[nm1] / diag[nm1]
    for i in xrange(n - 2, -1, -1):
        x[i] = (rhs[i] - upper[i] * x[i + 1]) / diag[i]

def tdma(np.ndarray[double, ndim=1] a not None, np.ndarray[double, ndim=1] b not None, np.ndarray[double, ndim=1] c not None, np.ndarray[double, ndim=1] d not None):
    cdef int n = b.shape[0]
    cdef np.ndarray[double, ndim=1] x = np.zeros(n)
    solve(n, <double*> a.data,
          <double*> b.data,
          <double*> c.data,
          <double*> d.data,
          <double*> x.data)
    return x
