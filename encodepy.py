#!/usr/bin/env python
# coding=utf-8

import urllib
import md5
import base64
import binascii
import sys

def mssql_str2ascii(string):
    out = ''
    if len(string):
        out = 'char(%d)' % ord(string[0])
        for char in string[1:]:
            out = out + '+char(%d)' % ord(char)

    print '[+] MSSQL ASCII  : %s' % out

def str2urlencode(string):
    '''
    urlencode加密
    '''
    out = ''
    if len(string):
        for char in string:
            out = out + '%' + binascii.b2a_hex(char)
    print '[+] Url Encode   : %s' % out

def str2hex(string):
    '''
    用处：
    1、Mysql导出一句话木马，select 0x3c3f706870406576616c285b615d293b3f3e into
    outfile 'd:/wwwroot/eval.php'
    2、

    '''
    out = '0x'
    if len(string):
        for char in string:
            out = out + '%s' % binascii.b2a_hex(char)

    print '[+] Hex Encode   : %s' % out

def str2ascii(string):
    out = ''
    if len(string):
        for char in string:
            out = out + '%d ' % ord(char)

    print '[*] ASCII Encode : %s' % out

def str2md5_16(string):
    '''
    MD5加密，返回16位的MD5值
    '''
    print '[+] MD5 Encode   : %s' % md5.new(string).hexdigest()[8:-8]

def str2md5_32(string):
    '''
    MD5加密，返回32位的MD5值
    '''
    print '[+] MD5 Encode   : %s' % md5.new(string).hexdigest()

def str2base64(string):
    '''
    Base64加密
    '''
    print '[+] Base64 Encode: %s' % base64.encodestring(string)

def str2html16(string):
    out = ''
    if len(string):
        for char in string:
            out = out + '&#x%s;' % binascii.b2a_hex(char)

    print '[+] HTML Entity : %s' % out

def str2html10(string):
    out = ''
    if len(string):
        for char in string:
            out = out + '&#%d;' % ord(char)

    print '[+] HTML Entity : %s' % out


def usage():
    print "python %s stringtobeencode" % sys.argv[0]
    sys.exit()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()

    encode_str = sys.argv[1]
    str2md5_32(encode_str)
    str2md5_16(encode_str)
    str2ascii(encode_str)
    str2hex(encode_str)
    str2urlencode(encode_str)
    mssql_str2ascii(encode_str)
    str2base64(encode_str)
    str2html16(encode_str)
    str2html10(encode_str)

