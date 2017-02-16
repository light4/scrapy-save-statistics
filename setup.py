#!/usr/bin/env python

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='scrapy-save-statistics',
    version='0.1',
    description='Scrapy Save Statistics: Save statistics extension for Scrapy',
    long_description=long_description,
    url='https://github.com/light4/scrapy-save-statistics',
    author='Light Ning',
    author_email='lightning1141@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=['scrapy_save_statistics'],
    install_requires=['Scrapy>=1.0'],
)
