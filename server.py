# coding: utf-8
# UDP53-Filter-Type - server.py
# 2020/1/8 15:47

__author__ = 'Benny <benny@bennythink.com>'

# server
import socket

server = socket.socket(type=socket.SOCK_DGRAM)
server.bind(('0.0.0.0', 53))
while True:
    print('53，正在等待被连接...')
    data, address = server.recvfrom(1024)
    print("client>>", data.decode('utf-8'))
    print("客户端连接的socket地址：", address)
    server.sendto(b'drink more water!', address)
    # server.close()
