#!/usr/bin/env python

from setuptools import setup, find_packages
from eppe import __version__

setup(
	name='paleocore-eppe',
	version=__version__,
	author='Denne Reed',
	author_email='denne.reed@gmail.com',
	description='A Paleo Core app for managing Eyasi Plateau Paleontology Expedition (EPPE) data.',
	url='https://github.com/paleocore/eppe',
	packages=find_packages(),
	include_package_data=True,
	install_requires=('Django>=2.2.24'),
	zip_safe=False,
	license='MIT',
	classifiers=(
		'Development Status :: 3 - Alpha',
		'Environment :: Web Environment',
		'Framework :: Django',
		'Intended Audience :: Developers',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.9',
	),
)
