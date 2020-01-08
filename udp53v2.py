# coding: utf-8
# UDP53-Filter-Type - udp53v2.py
# 2020/1/8 15:14

__author__ = 'Benny <benny@bennythink.com>'

import logging
import socket
import datetime
import argparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
HOST = '127.0.0.1'
PORT = 53

WELCOME = f"""
============= Benny's TCP&UDP 53 Filter Type Test ==========

In this program, you could test your hotspot's interception 
of TCP&UDP 53.

If your TCP 53 is ok, you may want to setup a Shadowsocks
or OpenVPN server to to bypass Web Auth;  
if your UDP 53 is ok, you may want to an OpenVPN
server to to bypass Web Auth; 

if all these two failed, DNS Tunnel is actually an option..

                                By Benny with love {datetime.datetime.today().year} 
                                   https://www.bennythink.com/
=============================================================
"""
SUCCESS = """
Congratulations, your {protocol} {port} is accessible.
How about setup an Shadowsocks or OpenVPN?
Visit https://www.bennythink.com/udp53.html for more info.
"""
FAIL = """
:-) Your {protocol} {port} is inaccessible.
Visit https://www.bennythink.com/udp53.html for more info.
"""
RESULTS = []


def tcp():
    try:
        logging.info(f"Trying TCP on {HOST}:{PORT}")
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.connect((HOST, PORT))
    except ConnectionRefusedError:
        logging.warning("TCP Connection refused from server. That's good.")
        RESULTS.append(f"TCP {PORT} success")
    except Exception as e:
        logging.error(f"Unknown error: {e}")
        RESULTS.append(f"TCP {PORT} fail")


def udp():
    try:
        logging.info(f"Trying UDP on {HOST}:{PORT}")
        socket.setdefaulttimeout(5)
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        soc.sendto(b'hi', (HOST, PORT))
        msg, _ = soc.recvfrom(1024)
        logging.info(f"Message from server o(*￣▽￣*)ブ{msg.decode('u8')}")
        logging.info("UDP Connection received from server. That's good.")
        RESULTS.append(f"UDP {PORT} success")
    except Exception as e:
        logging.error(f"Unknown error: {e}")
        RESULTS.append(f"UDP {PORT} fail")


def main():
    tcp()
    udp()
    print('\n\n')

    if 'success' in RESULTS[0]:
        print(SUCCESS.format(protocol='TCP', port=PORT))
    else:
        print(FAIL.format(protocol='TCP', port=PORT))
    if 'success' in RESULTS[1]:
        print(SUCCESS.format(protocol='UDP', port=PORT))
    else:
        print(FAIL.format(protocol='UDP', port=PORT))

    input("\n\nPress any key to exit.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=53, type=int, help='Port number to test')
    parser.add_argument('-s', type=str, default='115.159.161.154', help='Test host')

    args = parser.parse_args()
    HOST = args.s
    PORT = args.p
    print(WELCOME)
    input("Press any key to continue")
    main()
