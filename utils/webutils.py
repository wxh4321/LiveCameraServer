#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 11:28
# @Author  : wxh
# @Site    : 
# @File    : webutils.py
# @Software: PyCharm
# import socket
# def getLocalIP():
#     # 获取计算机名称
#     hostname = socket.gethostname()
#     # 获取本机IP
#     ip = socket.gethostbyname(hostname)
#     print(ip)
#     return ip
#
# if __name__=="__main__":
#     getLocalIP()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
# import socket
#
# #nt -- > windows
# if os.name != "nt":
#     import fcntl
#     import struct
#
#     def get_interface_ip(ifname):
#        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
#                            ifname[:15]))[20:24])
#
# def getLocalIP():
#     ip = socket.gethostbyname(socket.gethostname())
#     if ip.startswith("127.") and os.name != "nt":
#        interfaces = [
#           "wlan0",
#           "eth0",
#           "eth1",
#           "eth2",
#           "wlan1",
#           "wifi0",
#           "ath0",
#           "ath1",
#           "ppp0",
#            ]
#        for ifname in interfaces:
#            try:
#               ip = get_interface_ip(ifname)
#               break
#            except IOError:
#               pass
#     return ip
import socket

def getLocalIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

if __name__ == '__main__':
    print(getLocalIP())