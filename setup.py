# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import gerrit

if __name__ == "__main__":
    setup(
        name='gerrit.py',
        version=gerrit.__version__,
        description='A Python Wrapper for the Gerrit REST API',
        long_description=open('README.md').read(),
        author='Huang Yaming',
        author_email='yumminhuang+github@gmail.com',
        url='https://github.com/yumminhuang/gerrit.py',
        packages=[
            'gerrit',
        ],
        license=open('LICENSE').read(),
        install_requires=['requests'],
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
