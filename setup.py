# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in messenger/__init__.py
from messenger import __version__ as version

setup(
	name='messenger',
	version=version,
	description='Messenger',
	author='Doni Afrizal',
	author_email='doni.afrizal@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
