#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from setuptools import setup

name = 'textgenrnn'

modules = []
for root, dirs, files in os.walk(name):
    for f in files:
        if f.endswith('.py') and '__init__' not in f:
            module = name + root.partition(name)[-1].replace('/', '.') + '.' + f.partition('.py')[0]
            modules.append(module)

setup(
    name=name,
    packages=[name],
    py_modules=modules,
    version='0.9',  # Downgrade version because we downgraded Python and Keras
    description='Easily train your own text-generating neural network ' \
    'of any size and complexity',
    author='Max Woolf (modified by Colin Grambow)',
    url='https://github.com/minimaxir/textgenrnn',
    keywords=['deep learning', 'tensorflow', 'keras', 'text generation'],
    classifiers=[],
    license='MIT',
    python_requires='==2.7',
    include_package_data=True,
    scripts=[os.path.join('scripts', 'generate_quote.py')]
)
