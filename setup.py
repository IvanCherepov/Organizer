#!/usr/bin/env python

from setuptools import setup

setup(
    name='organizer',
    version='0.1.0',
    description='organizer for your bookmarks',
    author='IvanCherepov',
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