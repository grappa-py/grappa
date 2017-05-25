#!/usr/bin/env python
"""
grappa
======
Behavior-oriented, expressive assertion library for Python.

:copyright: (c) 2017 Tomas Aparicio
:license: MIT
"""

import os
import sys
import codecs
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# Publish command
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup_requires = []
if 'test' in sys.argv:
    setup_requires.append('pytest')


def read_version(package):
    with open(os.path.join(package, '__init__.py'), 'r') as fd:
        for line in fd:
            if line.startswith('__version__ = '):
                return line.split()[-1].strip().strip("'")


# Get package current version
version = read_version('grappa')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests/']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


with codecs.open('requirements-dev.txt', encoding='utf-8') as f:
    tests_require = f.read().splitlines()
with codecs.open('requirements.txt', encoding='utf-8') as f:
    install_requires = f.read().splitlines()
with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()
with codecs.open('History.rst', encoding='utf-8') as f:
    history = f.read()


setup(
    name='grappa',
    version=version,
    author='Tomas Aparicio',
    author_email='tomas@aparicio.me',
    description=(
        'Behavior-oriented, expressive, developer-friendly assertions library'
    ),
    url='https://github.com/grappa-py/grappa',
    license='MIT',
    long_description=readme + '\n\n' + history,
    py_modules=['grappa'],
    zip_safe=False,
    tests_require=tests_require,
    install_requires=install_requires,
    packages=find_packages(exclude=['tests', 'examples']),
    package_data={'': [
        'LICENSE', 'README.rst', 'History.rst',
        'requirements.txt', 'requirements-dev.txt'
    ]},
    package_dir={'grappa': 'grappa'},
    include_package_data=True,
    cmdclass={'test': PyTest},
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
