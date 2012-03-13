#include <Python.h>
#include <stdbool.h>
#include <numpy/arrayobject.h>

static void
solve(npy_intp n,
      double* lower,
      double* diag,
      double* upper,
      double* rhs,
      double* x)
{
    double m;
    npy_intp i;

    for (i = 1; i < n; ++i) {
        m = lower[i] / diag[i - 1];
        diag[i] -= m * upper[i - 1];
        rhs[i] -= m * rhs[i - 1];
    }

    x[n - 1] = rhs[n - 1] / diag[n - 1];

    for (i = n - 2; i >= 0; --i) {
        x[i] = (rhs[i] - upper[i] * x[i + 1]) / diag[i];
    }
}

static PyObject*
tdma(PyObject* module, PyObject* args)
{
    /* unused input variable, refers to the module */
    (void) module;

    /* setup the input arrays */
    PyObject* ain = NULL, *bin = NULL, *cin = NULL, *din = NULL;

    /* parse the inputs, pass the type and the input pointer */
    if (!PyArg_ParseTuple(args, "O!O!O!O!",
                          &PyArray_Type, &ain,
                          &PyArray_Type, &bin,
                          &PyArray_Type, &cin,
                          &PyArray_Type, &din)) {
        return NULL;
    }

    /* lower diagonal */
    PyObject* a = PyArray_FROM_OTF(ain, NPY_DOUBLE, NPY_IN_ARRAY);
    if (!a) {
        return NULL;
    }

    /* diagonal */
    PyObject* b = PyArray_FROM_OTF(bin, NPY_DOUBLE, NPY_IN_ARRAY);
    if (!b) {
        Py_XDECREF(a);
        return NULL;
    }

    /* upper diagonal */
    PyObject* c = PyArray_FROM_OTF(cin, NPY_DOUBLE, NPY_IN_ARRAY);
    if (!c) {
        Py_XDECREF(a);
        Py_XDECREF(b);
        return NULL;
    }

    /* right hand side of the equation */
    PyObject* d = PyArray_FROM_OTF(din, NPY_DOUBLE, NPY_IN_ARRAY);
    if (!d) {
        Py_XDECREF(a);
        Py_XDECREF(b);
        Py_XDECREF(c);
        return NULL;
    }

    /* get the dimensions of the rhs vector */
    npy_intp* dims = PyArray_DIMS(b);

    /* create a vector for the solution */
    PyObject* xout = PyArray_ZEROS(PyArray_NDIM(b),
                                   dims,
                                   NPY_DOUBLE,
                                   false);

    /* get the raw data of each array */
    double* ad = (double*) PyArray_DATA(a),
        *bd = (double*) PyArray_DATA(b),
        *cd = (double*) PyArray_DATA(c),
        *dd = (double*) PyArray_DATA(d),
        *xd = (double*) PyArray_DATA(xout);

    /* run the solver */
    solve(dims[0], ad, bd, cd, dd, xd);

    /* delete the references to the arrays */
    Py_DECREF(a);
    Py_DECREF(b);
    Py_DECREF(c);
    Py_DECREF(d);

    /* increase the reference count of the output array since it is new */
    Py_XINCREF(xout);
    return xout;
}

/* method table for the module */
static PyMethodDef tdma_methods[] = {
    {"tdma", tdma, METH_VARARGS, "Tridiagonal matrix solver."},
    {NULL}
};

/* module initialization */
PyMODINIT_FUNC
init_tdma(void)
{
    (void) Py_InitModule3("_tdma",
                          tdma_methods,
                          "Tridiagonal matrix solver module.");
    import_array();
}
