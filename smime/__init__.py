'''
 Python S/MIME library.
 
 (C) Konrad Jopek 2012
 
 Some functionality is common with M2Crypto, but M2Crypto uses limited version
 of PKCS7_sign function which does not provide possibility to create S/MIME 
 objects with specified digest algorithm. PKCS7_sign currently supports only
 SHA-1.

 ----------------------------------------------------------------------------
 "THE BEER-WARE LICENSE":
 <kjopek@gmail.com> wrote this file. As long as you retain this notice you
 can do whatever you want with this stuff. If we meet some day, and you think
 this stuff is worth it, you can buy me a beer in return Konrad Jopek
 ----------------------------------------------------------------------------
''' 

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes
import weakref
from bio import bio_init
from pkcs7 import pkcs7_init
from x509 import x509_init
from evp import evp_init

# common functions for library
def load_library(path='/usr/lib/libssl.so'):
    '''
    Loads OpenSSL library
    
    @param: path Path to library .so file
    @return: CDLL object associated with OpenSSL library file
    '''
    ssl = ctypes.CDLL(path)
    ssl.SSL_library_init()
    ssl.SSL_load_error_strings()

    bio_init(ssl)
    pkcs7_init(ssl)
    x509_init(ssl)
    evp_init(ssl)
    return ssl
