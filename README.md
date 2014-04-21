# Welcome to PyTDMA
PyTDMA stands for [Python TriDiagonal Matrix
Algorithm](http://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm).
PyTDMA is a short and sweet module with only a single function, designed
to do exactly what it says it does.

## Motivation
* It's part of an assignment for a computational statistics course
  that I took.
* It came as a bit of a surprise to me to find that the
  [`spsolve`](http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.spsolve.html#scipy.sparse.linalg.spsolve)
  function in
  [`scipy.sparse.linalg`](http://docs.scipy.org/doc/scipy/reference/sparse.linalg.html)
  was orders of magnitude slower than this version.

## Dependencies
* [Python](http://www.python.org) >= 2.7
* [NumPy](http://numpy.scipy.org) >= 1.5

## Optional Dependencies
* [SciPy](http://www.scipy.org/) >= 0.10 if you want to run `test.py`
  (it has some convenience functions for creating tridiagonal matrices)

## Installation/Testing
* Clone the git repository
* `whoami@hostname ~$ python setup.py build_ext --inplace` will result
  in a file called `_tdma.so`--if you're on a non-Mac UNIX box. This
  is the extension's shared object file.
* `whoami@hostname ~$ ./test.py n` will run the test solver with a randomly generated `n` by `n` matrix.
