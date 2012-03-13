from numpy.distutils.core import setup, Extension
import os, numpy as np

name = 'tdma'
sources = ['{}.c'.format(name)]

include_dirs = [np.get_include()]

setup(name=name,
      include_dirs=include_dirs,
      ext_modules=[Extension(name=name,
                             sources=sources)])
