# Welcome to PyTDMA
PyTDMA stands for [***P**ython **T**ri**D**iagonal **M**atrix **A**lgorithm*](http://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm). PyTDMA is a short and sweet module with (gasp!) only a single function, designed to do exactly what it says it does.

## Motivation
* It's part of an assignment for a course that I'm taking on computational statistics.
* It came as a bit of a surprise to me to find that the `spsolve` function in `scipy.sparse` was [*orders of magnitude*](http://en.wikipedia.org/wiki/Order_of_magnitude) slower than this version.

## Dependencies
* [Python](http://www.python.org) >= 2.7
* [NumPy](www.scipy.org) >= 1.5
* [SciPy](www.scipy.org) >= 0.10, if you want to run `test.py` (it has some convenience functions for creating tridiagonal matrices)

## Installation/Testing
* From the cloned Git repository: 
* `whoami@hostname ~$ python setup.py build_ext --inplace` will result in a file called `tdma.so`--if you're on a non-Mac UNIX. This file is the native extension shared object file.
* `whoami@hostname ~$ ./test.py 1000` will run the test solver with a 1000 by 1000 matrix.

### TODO
* Nothing so far.

