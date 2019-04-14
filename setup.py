"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup

from os import path

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Smart SMS Python',
    packages=['smartsms_py'],
    version='1.0.0',
    long_description=long_description,

    description='Python wrapper for Smart SMS API service.',

    author='Joseph Cobhams',
    author_email='jcobhams@gmail.com',
    url='https://github.com/jcobhams/smartsms-py',
    download_url='',
    long_description_content_type="text/markdown",
    keywords=['SmartSMS', 'Nigeria', 'API Wrapper'],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests'],
)