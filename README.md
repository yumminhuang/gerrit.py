gerrit.py --- A Python Wrapper for the Gerrit REST API
===
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/yumminhuang/gerrit.py)
[![Python](https://img.shields.io/badge/python-2.7-blue.svg)](https://github.com/yumminhuang/gerrit.py)
[![Build Status](https://travis-ci.org/yumminhuang/gerrit.py.svg?branch=master)](https://travis-ci.org/yumminhuang/gerrit.py)
[![Coverage Status](https://coveralls.io/repos/github/yumminhuang/gerrit.py/badge.svg)](https://coveralls.io/github/yumminhuang/gerrit.py)

:construction: **[WIP] This project is still under development.**

*gerrit.py* provides a simple interface to interact with
 [Gerrit Code Review](https://www.gerritcodereview.com/) via the
 [REST API](https://gerrit-review.googlesource.com/Documentation/rest-api.html).

**Gerrit Version Compatibility**

* [Gerrit Stable-2.11](https://gerrit.googlesource.com/gerrit/+/stable-2.11)

## Install

Install from source code

```shell
python setup.py install
```

## Usage

```python
from gerrit.gerrit import Gerrit
from gerrit.config import Config

g = Gerrit('gerrit.example.com', 'username', 'password')
config = Config(g)
success, version = config.get_version()
print success
# True
print version
# 2.11.10
```

## Acknowledgements

This project is inspired by [CBitLabs/BitBucket-api](https://github.com/CBitLabs/BitBucket-api).
