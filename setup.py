import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
	README = readme.read()


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='django-forgive',
	version='0.0.1',
	packages=['forgive'],
	include_package_data=True,
	description='Forgive service inspired by prostite.com',
	url='http://langley.tk/',
	author='Amy Woodehy',
	author_email='AmyWoodehy@gmail.com',
	classifiers=[
		'Framework :: Django',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 2',
	],
)
