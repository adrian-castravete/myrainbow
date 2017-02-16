#!/usr/bin/env python2
# -*- coding: utf-8 -*-


from __future__ import absolute_import

import os

import rainbow_logging_handler
import yaml


class RainbowLoggingHandler(rainbow_logging_handler.RainbowLoggingHandler):

    def __init__(self, *args, **kwargs):
        kwargs.update(self._read_rc())
        super(RainbowLoggingHandler, self).__init__(*args, **kwargs)

    def _read_rc(self):
        config = {}
        config.update(self._read_rc_file('~/.rainbowrc'))
        return config

    def _read_rc_file(self, file_name):
        path = os.path.expanduser(file_name)
        path = os.path.expandvars(path)
        path = os.path.realpath(path)
        with open(path) as fin:
            config = yaml.load(fin)

        return config
