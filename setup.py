#!/usr/bin/env python3

import os
from setuptools import setup


directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(name='ads',
      version='0.1.0',
      description='Package of curated Algorithms and Data Structures written by the community',
      author='Piotr Rybiec',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=['ads',],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"

      ],
      include_package_data=True,
      python_requires='>=3.9'
)



