#!/usr/bin/python
# coding:utf-8

# UDP53-Filter-Type - UDP53.py
# 2017/10/28 16:58
# Test for Port 53, support both Python 2 and Python 3 under Linux & Windows.

__author__ = 'Benny <benny@bennythink.com>'

import socket

HOST = 'jbls.bennythink.com'
PORT = 53


def send_data():
    err = None
    print('Start Testing...')
    sock_clt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock_clt.connect((HOST, PORT))
        sock_clt.send('Hi')
    except socket.error as e:
        err = e
    except ConnectionRefusedError as e:
        err = e
    finally:
        sock_clt.close()

    return str(err)


def parser(err_msg):
    if '10061' in err_msg or '111' in err_msg:
        return True
    elif '10060' in err_msg or '110' in err_msg:
        return False
    else:
        return None


def deter(err_stat):
    if err_stat:
        print(':-) Congratulations, you may wanna try OpenVPN!')
        print('Visit https://www.bennythink.com/udp53.html for more info.\n')
    elif err_stat is False:
        print(':-) Sad face, but DNS Tunnel is an option.')
        print('Visit https://www.bennythink.com/udp53.html for more info.\n')
    else:
        print(':-(\nYou probably forget to connect to a Wi-Fi hotspot.\n')


def welcome():
    print('============= Benny\'s TCP&UDP 53 Filter Type Test ==========\n')
    print('In this program, you could test your hotspot\'s interception ')
    print('of UDP 53.\n')
    print('If your hotspot allows any kind of  Packet via Port 53,   ')
    print('you may wanna setup an OpenVPN or Shadowsocks server ')
    print('to bypass Web Auth;    ')
    print('if not, DNS Tunnel is actually a bad option.\n')
    print('                                     By Benny with love 2017 ')
    print('                                   https://www.bennythink.com')
    print('=============================================================')


if __name__ == '__main__':
    welcome()
    res1 = parser(send_data())
    deter(res1)

    input('Press Enter to exit.')
