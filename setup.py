#!/usr/bin/env python
# pylint: disable=W,I,C
from __future__ import absolute_import

import os
import sys

import re
from setuptools import find_packages, setup

ROOT = os.path.realpath(os.path.join(os.path.dirname(__file__)))

reqs = 'install.py%d.pip' % sys.version_info[0]

rel = lambda *parts: os.path.join(ROOT, *parts)


def get_info(*file_paths):
    """Retrieves the version from __init__.py"""
    filename = rel(*file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^VERSION = [\"]([^\"]*)[\"]",
                              version_file, re.M)
    name_match = re.search(r"^NAME = [\"]([^\"]*)[\"]",
                           version_file, re.M)
    if version_match and name_match:
        return version_match.group(1), name_match.group(1)
    raise RuntimeError("Unable to find version string.")


version, name = get_info('src', 'adminactions', '__init__.py')


def fread(fname):
    return (open(rel('src', 'requirements',
                     'install.any.pip')).read() +
            open(rel('src',
                     'requirements', fname)).read())


tests_require = fread('testing.pip')
dev_require = fread('develop.pip')

setup(
    name=name,
    version=version,
    url='https://github.com/saxix/django-adminactions',
    download_url='https://github.com/saxix/django-adminactions',
    author='sax',
    author_email='s.apostolico@gmail.com',
    description="Collections of useful actions to use with django.contrib.admin.ModelAdmin",
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=fread(reqs),
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'dev': dev_require + tests_require,
    },
    zip_safe=False,
    platforms=['any'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers'],
    long_description=open('README.rst').read()
)
