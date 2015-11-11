#!/usr/bin/env python

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='organizer',
    version='0.1.0',
    include_package_data=True,
    description='Organizer for your bookmarks.',
    long_description=README,
    author='Ivan Cherepov',
    author_email='cherapau@gmail.com',
    maintainer='Ivan Cherepov',
    maintainer_email='cherapau@gmail.com',
    install_requires=[
        'django==1.8',
        'django-crispy-forms==1.5.2'
    ],
    license='LICENSE.txt',
    packages=['organizer'],
    url='https://github.com/IvanCherepov/Organizer'
)