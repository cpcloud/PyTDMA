from distutils.core import setup
from Cython.Distutils import build_ext
from Cython.Distutils.extension import Extension
import numpy as np

extra_compile_args = []
extra_link_args = []
ext_modules = [Extension('_tdma', ['tdma.pyx'],
                         extra_compile_args=extra_compile_args,
                         extra_link_args=extra_link_args)]

setup(name='tdma',
      cmdclass={'build_ext': build_ext},
      include_dirs=[np.get_include()],
      ext_modules=ext_modules)
