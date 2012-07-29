'''
 Python S/MIME library.
 
 (C) Konrad Jopek 2012
 
 BIO-related functions from OpenSSL

 ----------------------------------------------------------------------------
 "THE BEER-WARE LICENSE":
 <kjopek@gmail.com> wrote this file. As long as you retain this notice you
 can do whatever you want with this stuff. If we meet some day, and you think
 this stuff is worth it, you can buy me a beer in return Konrad Jopek
 ----------------------------------------------------------------------------
''' 

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ctypes import c_int, c_void_p, c_char_p, c_long, c_size_t
from utils import wrap

#BIO *	BIO_new(BIO_METHOD *type);
new = lambda lib, _type: lib.BIO_new(_type)

#int	BIO_free(BIO *a);
free = lambda lib, bio: lib.BIO_free(bio)

#BIO *BIO_new_fd(int fd, int close_flag);
new_fd = lambda lib, fd, close_flag: lib.BIO_new_fd(fd, close_flag)

#int	BIO_read(BIO *b, void *data, int len);
read = lambda lib, bio, data, _len: lib.BIO_read(bio, data, _len)

#int	BIO_gets(BIO *bp,char *buf, int size);
gets = lambda lib, bio, buf, size: lib.BIO_gets(bio, buf, size)

#int	BIO_write(BIO *b, const void *data, int len);
write = lambda lib, bio, data, _len: lib.BIO_write(bio, data, _len)

#int	BIO_puts(BIO *bp,const char *buf);
puts = lambda lib, bio, buf: lib.BIO_puts(bio, buf)

#size_t BIO_ctrl_pending(BIO *b);
ctrl_pending = lambda lib, bio: lib.BIO_ctrl_pending(bio)

#BIO_METHOD *BIO_s_mem(void);
s_mem = lambda lib: lib.BIO_s_mem()

def bio_init(lib):
    wrap(lib.BIO_new, [c_void_p], c_void_p)
    wrap(lib.BIO_free, [c_void_p], c_int)
    wrap(lib.BIO_new_fd, [c_int, c_int], c_void_p)
    wrap(lib.BIO_read, [c_void_p, c_void_p, c_int], c_int)
    wrap(lib.BIO_gets, [c_void_p, c_char_p, c_int], c_int)
    wrap(lib.BIO_write, [c_void_p, c_void_p, c_int], c_int)
    wrap(lib.BIO_puts, [c_void_p, c_char_p], c_int)
    wrap(lib.BIO_ctrl_pending, [c_void_p], c_size_t)
    wrap(lib.BIO_s_mem, [], c_void_p)
