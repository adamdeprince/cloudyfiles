#!/usr/bin/env python
"""
cloudyfiles 
======

Right now cloud file access in Python is about where database access
was in the mid 90's.  Each database wrapper author has their very own
nomenclature, sets of commands for doing things that are basically the
same - creating cursors, executing commands and reading rows.

cloudyfiles seeks to do for cloud file providers what the Python
Database API does for database access.  Cloud file style servces like
Rackspace's cloud files and Amazon's S3 really are nothing more than
dictionaries that map fixed strings to

"""

from setuptools import setup

setup(
    name='cloudyfiles',
    version='0.0.0',
    author='Adam DePrince',
    author_email='deprince@googlealumni.com"
    description='Dictionary interface to cloud providers.',
    long_description=__doc__,
    py_modules=[
        "cloudyfiles/__init__",
        "cloudyfiles/s3",
        "cloudyfiles/common",
        "cloudyfiles/cloudfiles",
        "cloudyfiles/django_storage",
    ],
    packages=["cloudyfiles"],
    zip_safe=True,
    license='GPL',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha'
    ],
    scripts=[
    ],
    url="http://wnyc.github.io/cloudyfiles/",
    install_requires=[
        "boto",
        "python-cloudfiles",
        # "appengine",
    ]
)
