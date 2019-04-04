#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='textgenrnn',
    packages=['textgenrnn'],  # this must be the same as the name above
    version='0.9',  # Downgrade version because we downgraded Python and Keras
    description='Easily train your own text-generating neural network ' \
    'of any size and complexity',
    author='Max Woolf',
    author_email='max@minimaxir.com',
    url='https://github.com/minimaxir/textgenrnn',
    keywords=['deep learning', 'tensorflow', 'keras', 'text generation'],
    classifiers=[],
    license='MIT',
    python_requires='>=2.7',
    include_package_data=True,
)
