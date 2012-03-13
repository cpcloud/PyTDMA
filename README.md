# Welcome to PyTDMA
PyTDMA stands for [*Python Tridiagonal Matrix Algorithm*](http://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm) and is a short and sweet module with (gasp!) only a single function designed to do exactly what the title says it does.

## Dependencies
* [Python](http://www.python.org) >= 2.6
* [NumPy](www.scipy.org) >= 1.5
* [SciPy](www.scipy.org) >= 0.10, if you want to run `test.py`

## Installation/Testing
* From the cloned Git repository: 
** `python setup.py build_ext --inplace` will result in a file called `tdma.so` (if you're on a non Mac UNIX), which is the native extension shared object file.
** `python test.py 1000` will run the test solver with a 1000 by 1000 matrix.
