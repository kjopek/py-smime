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

