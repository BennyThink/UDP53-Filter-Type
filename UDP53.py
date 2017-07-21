# coding: utf8
import socket

HOST = '123.206.87.223'
PORT = 53


def send_data(data):
    sock_clt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_clt.connect((HOST, PORT))
    sock_clt.send(data)
    sock_clt.close()


print
print '============= Benny\'s UDP 53 Filter Type Test =============='
print
print 'In this program, you could test your hotspot\'s interception '
print 'of UDP 53.'
print
print 'If your hostpot allows any kind of UDP Packet via Port 53,   '
print 'you may wanna setup an OpenVPN server to bypass Web Auth;    '
print 'if not, DNS Tunnel is actually a bad option.'
print
print '                                     By Benny with love 2017 '
print '                                   https://www.bennythink.com'
print '============================================================='
print
print '----------------------  Start Testing  ----------------------'

try:
    send_data('Hi')
except socket.error as e:
    print
else:
    print "That cannot happen!"

if '10061' in str(e) or '111' in str(e):
    print ':-) Congratulations, you may wanna try OpenVPN!'
    print 'Visit https://www.bennythink.com/udp53.html for more info.'
elif '10060' in str(e) or '110' in str(e):
    print ':-) Sad face, but DNS Tunnel is an option.'
    print 'Visit https://www.bennythink.com/udp53.html for more info.'
else:
    print ':-('
    print 'You probably forget to connect to a Wi-Fi hotspot.'
