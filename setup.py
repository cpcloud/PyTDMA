from numpy.distutils.core import setup, Extension
import numpy as np

name = '_tdma'
sources = ['%s.c' % name[1:]]

include_dirs = [np.get_include()]

setup(name=name,
      include_dirs=include_dirs,
      ext_modules=[Extension(name=name,
                             sources=sources)])
