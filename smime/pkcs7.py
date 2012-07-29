'''
 Python S/MIME library.
 
 (C) Konrad Jopek 2012

 PKCS7 functions from OpenSSL
 
 ----------------------------------------------------------------------------
 "THE BEER-WARE LICENSE":
 <kjopek@gmail.com> wrote this file. As long as you retain this notice you
 can do whatever you want with this stuff. If we meet some day, and you think
 this stuff is worth it, you can buy me a beer in return Konrad Jopek
 ----------------------------------------------------------------------------
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import wrap
from ctypes import c_void_p, c_int

# following constants come directly from OpenSSL library:
PKCS7_TEXT            = 0x1
PKCS7_NOCERTS         = 0x2
PKCS7_NOSIGS          = 0x4
PKCS7_NOCHAIN         = 0x8
PKCS7_NOINTERN        = 0x10
PKCS7_NOVERIFY        = 0x20
PKCS7_DETACHED         = 0x40
PKCS7_BINARY          = 0x80
PKCS7_NOATTR          = 0x100
PKCS7_NOSMIMECAP      = 0x200
PKCS7_NOOLDMIMETYPE   = 0x400
PKCS7_CRLFEOL         = 0x800
PKCS7_STREAM          = 0x1000
PKCS7_NOCRL           = 0x2000

SMIME_TEXT            = PKCS7_TEXT
SMIME_NOCERTS         = PKCS7_NOCERTS
SMIME_NOSIGS          = PKCS7_NOSIGS
SMIME_NOCHAIN         = PKCS7_NOCHAIN
SMIME_NOINTERN        = PKCS7_NOINTERN
SMIME_NOVERIFY        = PKCS7_NOVERIFY
SMIME_DETACHED        = PKCS7_DETACHED
SMIME_BINARY          = PKCS7_BINARY
SMIME_NOATTR          = PKCS7_NOATTR

# int PKCS7_set_type(PKCS7 *p7, int type);
set_type = lambda lib, p7, _type: lib.PKCS7_set_type(p7, _type)

#int PKCS7_set_content(PKCS7 *p7, PKCS7 *p7_data);
set_content = lambda lib, p7, p7_data: lib.PKCS7_set_content(p7, p7_data)

#int PKCS7_add_certificate(PKCS7 *p7, X509 *x509);
add_certificate = lambda lib, p7, x509: lib.PKCS7_add_certificate(p7, x509)

#int PKCS7_signatureVerify(BIO *bio, PKCS7 *p7, PKCS7_SIGNER_INFO *si, 
#                          X509 *x509);
signatureVerify = lambda lib, bio, p7, si, x509: lib.PKCS7_signatureVerify(bio, 
                  p7, si, x509)

#int PKCS7_dataVerify(X509_STORE *cert_store, X509_STORE_CTX *ctx,
#	BIO *bio, PKCS7 *p7, PKCS7_SIGNER_INFO *si); 
dataVerify = lambda lib, cert_store, ctx, bio, p7, si: lib.PKCS7_dataVerify(cert_store,
             ctx, bio, p7, si)

#BIO *PKCS7_dataInit(PKCS7 *p7, BIO *bio);
dataInit = lambda lib, p7, bio: lib.PKCS7_dataInit(p7, bio)

#int PKCS7_dataFinal(PKCS7 *p7, BIO *bio);
dataFinal = lambda lib, p7, bio: lib.PKCS7_dataFinal(p7, bio)

#BIO *PKCS7_dataDecode(PKCS7 *p7, EVP_PKEY *pkey, BIO *in_bio, X509 *pcert);
dataDecode = lambda lib, p7, pkey, in_bio, pcert: lib.PKCS7_dataDecode(p7, key, 
             in_bio, pcert)

#PKCS7_SIGNER_INFO *PKCS7_add_signature(PKCS7 *p7, X509 *x509,
#        EVP_PKEY *pkey, const EVP_MD *dgst);
add_signature = lambda lib, p7, x509, pkey, dgest: lib.PKCS7_add_signature(p7, 
                x509, pkey, dgst)

#int PKCS7_verify(PKCS7 *p7, STACK_OF(X509) *certs, X509_STORE *store,
#                 BIO *indata, BIO *out, int flags);
verify = lambda lib, p7, certs, store, indata, out, flags: lib.PKCS7_verify(p7,
         certs, store, indata, out, flags)
         
#PKCS7 *PKCS7_encrypt(STACK_OF(X509) *certs, BIO *in, const EVP_CIPHER *cipher,
#                     int flags);
encrypt = lambda lib, certs, _in, cipher, flags: lib.PKCS7_encrypt(certs, _in,
          cipher, flags)

#int PKCS7_decrypt(PKCS7 *p7, EVP_PKEY *pkey, X509 *cert, BIO *data, int flags);
decrypt = lambda lib, p7, pkey, cert, data, flags: lib.PKCS7_decrypt(p7, pkey,
          cert, data, flags)

#int PKCS7_add_attrib_smimecap(PKCS7_SIGNER_INFO *si,
#                              STACK_OF(X509_ALGOR) *cap);

add_attrib_smimecap = lambda lib, si, cap: lib.PKCS7_add_attrib_smimecap(si, 
                      cap)

#STACK_OF(X509_ALGOR) *PKCS7_get_smimecap(PKCS7_SIGNER_INFO *si);
get_smimecap = lambda lib, si: lib.PKCS7_get_smimecap(si)

#int PKCS7_simple_smimecap(STACK_OF(X509_ALGOR) *sk, int nid, int arg);
simple_smimecap = lambda lib, sk, nid, arg: lib.PKCS7_simple_smimecap(sk, nid, 
                  arg)
                  
#int SMIME_write_PKCS7(BIO *bio, PKCS7 *p7, BIO *data, int flags);
write_PKCS7 = lambda lib, bio, p7, data, flags: lib.SMIME_write_PKCS7(bio, p7,
              data, flags)
              
#PKCS7 *SMIME_read_PKCS7(BIO *bio, BIO **bcont);
read_PKCS7 = lambda lib, bio, bcont: lib.SMIME_read_PKCS7(bio, bcont)

#int SMIME_crlf_copy(BIO *in, BIO *out, int flags);
crlf_copy = lambda lib, _in, out, flags: lib.SMIME_crlf_copy(_in, out, flags)

#int SMIME_text(BIO *in, BIO *out);
text = lambda lib, _in, out: lib.SMIME_text(_in, out)

#PKCS7 *PKCS7_new(void)
new = lambda lib: lib.PKCS7_new()

def pkcs7_init(lib):
    wrap(lib.PKCS7_set_type, [c_void_p, c_int], c_int)
    wrap(lib.PKCS7_set_content, [c_void_p, c_void_p], c_int)
    wrap(lib.PKCS7_add_certificate, [c_void_p, c_void_p], c_int)
    wrap(lib.PKCS7_signatureVerify, [c_void_p, c_void_p, c_void_p, c_void_p], c_int)
    wrap(lib.PKCS7_dataVerify, [c_void_p, c_void_p, c_void_p, c_void_p, c_void_p], c_int)
    wrap(lib.PKCS7_dataInit, [c_void_p, c_void_p], c_void_p)
    wrap(lib.PKCS7_dataFinal, [c_void_p, c_void_p], c_int)
    wrap(lib.PKCS7_dataDecode, [c_void_p, c_void_p, c_void_p, c_void_p], c_void_p)
    wrap(lib.PKCS7_add_signature, [c_void_p, c_void_p, c_void_p, c_void_p], c_void_p)
    wrap(lib.PKCS7_verify, [c_void_p, c_void_p, c_void_p, c_void_p, c_void_p, c_int], c_int)
    wrap(lib.PKCS7_encrypt, [c_void_p, c_void_p, c_void_p, c_int], c_void_p)
    wrap(lib.PKCS7_decrypt, [c_void_p, c_void_p, c_void_p, c_void_p, c_int], c_int)
    wrap(lib.PKCS7_add_attrib_smimecap, [c_void_p, c_void_p], c_int)
    wrap(lib.PKCS7_get_smimecap, [c_void_p], c_void_p)
    wrap(lib.PKCS7_simple_smimecap, [c_void_p, c_int, c_int], c_int)
    wrap(lib.SMIME_write_PKCS7, [c_void_p, c_void_p, c_void_p, c_int], c_int)
    wrap(lib.SMIME_read_PKCS7, [c_void_p, c_void_p], c_void_p)
    wrap(lib.SMIME_crlf_copy, [c_void_p, c_void_p, c_int], c_int)
    wrap(lib.SMIME_text, [c_void_p, c_void_p], c_int)
    wrap(lib.PKCS7_new, [], c_void_p) 
