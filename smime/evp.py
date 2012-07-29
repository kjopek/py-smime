'''
 Python S/MIME library.
 
 (C) Konrad Jopek 2012
 
 EVP-related functions from OpenSSL

 ----------------------------------------------------------------------------
 "THE BEER-WARE LICENSE":
 <kjopek@gmail.com> wrote this file. As long as you retain this notice you
 can do whatever you want with this stuff. If we meet some day, and you think
 this stuff is worth it, you can buy me a beer in return Konrad Jopek
 ----------------------------------------------------------------------------
''' 

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ctypes import c_int, c_void_p, c_char_p, c_long, CFUNCTYPE
from utils import wrap

c_pass_callback_t = CFUNCTYPE(c_char_p)

# PEM_read_bio_PrivateKey
pem_read_bio_private_key = lambda lib, bio, evp, callback, arg: lib.PEM_read_bio_PrivateKey(bio,
                           evp, callback, arg)

evp_md_sha256 = lambda lib: lib.EVP_sha256()
evp_md_sha384 = lambda lib: lib.EVP_sha384()
evp_md_sha512 = lambda lib: lib.EVP_sha512()

def evp_init(lib):
    wrap(lib.PEM_read_bio_PrivateKey, [c_void_p, c_void_p, c_pass_callback_t, 
                                       c_void_p], c_void_p)
    wrap(lib.EVP_sha256, [], c_void_p)
    wrap(lib.EVP_sha384, [], c_void_p)
    wrap(lib.EVP_sha512, [], c_void_p)
