from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))


# get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = fh.read()


# version tag
version = open(path.join(here, "VERSION")).read().strip()


# requirements
install_requires = open(path.join(here, "requirements.txt")).read().strip().split("\n")


setup(
    name='coinbase-connector',
    version=version,
    description='Forwarding service from coinbase to kafka.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Maxwell Dylla',
    author_email='maxwell.dylla@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=install_requires,
    include_package_data=True,
)
