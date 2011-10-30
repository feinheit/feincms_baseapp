# -*- coding: utf-8 -*-from setuptools import setup, find_packages
from baseapp import get_version
setup(
    name='feincms_baseapp',
    version=get_version(),
    description='This is a base app and contenttype for Feincms.',
    author='',
    author_email='',
    url='https://github.com/',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ]
)
