# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='whmcs-restful',
    version='1.0.0',
    description='whmcs v.7 restful api for others',
    long_description='just whmcs v.7 restful api for others',
    url='git@github.com:riesal/whmcs-restful.git',
    license='Apache-2.0'
)
