#!/usr/bin/env python2


from __future__ import absolute_import

from setuptools import setup


with open('readme.rst') as fin:
    long_description = fin.read()


setup(name='myrainbow',
      version='0.1.0',
      description="My take on RainbowLoggingHandler to enable other default colors.",
      long_description=long_description,
      url="https://github.com/adrian-castravete/myrainbow",
      author="Adrian Castravete",
      author_email="adrian@figshare.com",
      license='MIT',
      install_requires=['rainbow_logging_handler'])
