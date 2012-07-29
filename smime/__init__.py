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
import zlib

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

SMIME_SIGN      = 0x01
SMIME_COMPRESS  = 0x02
SMIME_ENCRYPY   = 0x04

class SMIME(object):
    '''
    The main class for (un)wrapping messages according to SMIME standard.
    This code is based on C API of OpenSSL. I tried to follow the schema of
    openssl smime command.
    '''

    MD_ALGS = {'SHA256' : evp.evp_md_sha256(),
               'SHA384' : evp.evp_md_sha384(),
               'SHA512' : evp.evp_md_sha512()}
                
    def __init__(self, ssl_lib_path='/usr/lib/libssl.so'):
        self.ssl = load_library(ssl_lib_path)
        self.cert = None
        self.pkey = None
    
    # public interface
    
    def wrap_message(self, msg, activity=SMIME_SIGN, md='):
        '''
        Signs / compresses / encrypts the message according to the activity
        variable. Please note that you cannot process message without SMIME_SIGN.
        
        @param: msg Message to process
        @param: activity Specifies what library shoud do with message
        @param: md Hash algorithm to use. Can be one of ['SHA256', 'SHA384', 'SHA512']
        
        @return: String with PKCS7-formatted output
        '''
        assert md in self.MD_ALGS, 'Unknown algorithm: %s' % md
        assert pkey is not None, 'Load private key first'
        assert type(msg) == str, 'Message must be a string'
        
        if activity & SMIME_ENCRYPT:
            assert cert is not None, 'Load certificate to encrypt with'
        
    def unwrap_message(self, msg):
        '''
        Decrypts / decompresses / checks the signature of message.
        Returns decrypted and uncompressed message if signature is valid, 
        otherwise raises an Exception
        
        @param: msg Message to develop, PKCS7 formatted
        @return: String with message
        '''
        
        assert type(msg) == str, 'Message must be a string'
        
     # private helpers
     
     def _load_file(self, filename):
        '''
        Converts the content of filename into a BIO object
        
        WARNING: you must free the memory allocated by BIO_new on your own!
        
        @param: filename Name of file to open
        @return: created BIO
        '''
        
        fp = None
    
     def _load_string(self, s):
        '''
        Converts string to BIO memory object
        
        WARNING: you must free the memory allocated by BIO_new on your own!
        
        @param: s String to convert
        @return 
        '''
