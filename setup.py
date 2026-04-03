import kh2fmbr
from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
	name = 'kh2fmbr',
	packages = find_packages(),
	include_package_data=True,
	version = '0.0.1',
	long_description = long_description,
	long_description_content_type='text/markdown',
	license = 'MIT',
	author = 'roromaniac',
	author_email= 'rando4ukraine@gmail.com',
	maintainer_email = 'rando4ukraine@gmail.com',
	url = 'https://github.com/roromaniac/khbr',
	classifiers = [
		"Intended Audience :: Developers",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3"
	],
	install_requires=[
        'PyYAML',
    ],
	platforms = 'any'
)
