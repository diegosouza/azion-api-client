#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
from os import path

from distutils.util import convert_path
from setuptools import find_packages, setup


version_filename = convert_path("azion/__consts__.py")
with open(version_filename, mode="r", encoding="utf-8") as fobj:
    for line in fobj:
        if "CLIENT_VERSION =" in line:
            version = line.strip().split("=")[-1].strip()


NAME = 'azion-api-client'
DESCRIPTION = "A Python API client for Azion management and automation"
URL = 'https://github.com/diegosouza/azion-api-client'
EMAIL = 'diegosouza.br@gmail.com'
AUTHOR = 'Diego de Souza Mendes'
REQUIRES_PYTHON = '>=3.7'
VERSION = version
REQUIRED = [
    'pendulum',
    'requests',
    'click',
]


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    install_requires=REQUIRED,
    include_package_data=True,
    license='GPL3',
    entry_points={"console_scripts": ["azion = azion.cli:cli"]}
)
