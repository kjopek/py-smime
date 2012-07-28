#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes

class BIO(object):
    BIO_TYPES = { 'MEM' : lambda lib: lib.

    def __init__(self, lib, bio_type):
        self.lib = lib
        self.type = bio_type
        
