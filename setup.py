#!/usr/bin/env python3

from setuptools import setup, find_packages

long_description = """
Squmfit (pronounced "squim-fit") is a Python library for flexible
non-linear least-squares fitting of models to curves. Squmfit is
distinguished from lmfit in its treatment of fit parameters
as first-class objects, naturally accomodating global fitting across
multiple curves with tied parameters.
"""

setup(
    name = "squmfit",
    description = "Convenient non-linear least squares fitting",
    long_description = long_description,
    version = "0.2",
    author = 'Ben Gamari',
    author_email = 'ben@smart-cactus.org',
    url = 'http://github.com/bgamari/squmfit',
    license = 'BSD',
    packages = find_packages(),
    install_requires=[
        'numpy',
        'scipy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
