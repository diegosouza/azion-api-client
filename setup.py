#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from setuptools import find_packages, setup
from os import path


setup(
    name='azion-api-client',
    version='0.0.1.a1',
    description="A Python API client for Azion management and automation",
    long_description_content_type='text/markdown',
    url='https://github.com/diegosouza/azion-api-client',
    include_package_data=True,
    license='GPL3',
    author='Diego de Souza Mendes',
    author_email='diegosouza.br@gmail.com',
    python_requires='>=3.8',
    entry_points={"console_scripts": ["azion = azion.cli:cli"]},
    install_requires=[
        'pendulum',
        'requests',
        'click',
    ]
)
