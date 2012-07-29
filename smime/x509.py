'''
 Python S/MIME library.
 
 (C) Konrad Jopek 2012

 X509 functions from OpenSSL
 
 ----------------------------------------------------------------------------
 "THE BEER-WARE LICENSE":
 <kjopek@gmail.com> wrote this file. As long as you retain this notice you
 can do whatever you want with this stuff. If we meet some day, and you think
 this stuff is worth it, you can buy me a beer in return Konrad Jopek
 ----------------------------------------------------------------------------
'''

from ctypes import c_int, c_void_p, POINTER, c_long
from utils import wrap

FORMATS = {'PEM' : 0, 'DER' : 1}
c_long_p = POINTER(c_long)

#X509 *d2i_X509_bio(BIO *bp,X509 **x509);
der_X509_bio = lambda lib, bio, x509: lib.d2i_X509_bio(bio, x509)

#int	PEM_read_bio(BIO *bp, char **name, char **header,
#       unsigned char **data,long *len);
pem_x509_bio = lambda lib, bio, name, header, data, _len: lib.PEM_read_bio(bio,
               name, header, data, _len)

def x509_init(lib):
    wrap(lib.d2i_X509_bio, [c_void_p, c_void_p], c_void_p)
    wrap(lib.PEM_read_bio, [c_void_p, c_void_p, c_void_p, c_void_p, c_long_p], c_int)
