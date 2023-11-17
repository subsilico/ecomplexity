from setuptools import setup
from Cython.Build import cythonize
import numpy

## python3 setup.py build_ext --inplace

# Define the extension module
extensions = [
    # Replace 'simulation.pyx' with the path to your Cython source file
    # Add any additional Cython files to this list
    "ecomplexity.pyx"
]

# Use cythonize on the extension object.
setup(
    name='Monte Carlo Simulation',
    ext_modules=cythonize(extensions),
    include_dirs=[numpy.get_include()]  # This helps to find numpy headers
)
