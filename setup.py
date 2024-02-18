# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='urllib3',
    version='2.2.3',
    description='HTTP library with thread-safe connection pooling, file post, and more.',
    author_email='Andrey Petrov <andrey.petrov@shazow.net>',
    maintainer_email='Seth Michael Larson <sethmichaellarson@gmail.com>, Quentin Pradet <quentin@pradet.me>, Illia Volochii <illia.volochii@gmail.com>',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
    extras_require={
        'brotli': [
            'brotli>=1.0.9; platform_python_implementation == "CPython"',
            'brotlicffi>=0.8.0; platform_python_implementation != "CPython"',
        ],
        'h2': [
            'h2<5,>=4',
        ],
        'socks': [
            'pysocks!=1.5.7,<2.0,>=1.5.6',
        ],
        'zstd': [
            'zstandard>=0.18.0',
        ],
    },
    packages=[
        'urllib3',
        'urllib3.contrib',
        'urllib3.contrib.emscripten',
        'urllib3.http2',
        'urllib3.util',
    ],
    package_dir={'': 'src'},
)
