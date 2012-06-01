from distutils.core import setup
from Cython.Distutils import build_ext
from Cython.Distutils.extension import Extension

extra_compile_args = ['-march=native', '-O3']
extra_link_args = []
ext_modules = [Extension('_tdma',
                         ['tdma.pyx'],
                         extra_compile_args=extra_compile_args,
                         extra_link_args=extra_link_args)]

setup(name='tdma',
      cmdclass={'build_ext': build_ext},
      ext_modules=ext_modules)
