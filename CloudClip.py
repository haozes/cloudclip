__author__ = 'haozes'

import pyperclip
import socket
import time
from threading import Thread

import fcntl
import struct
import os

gLastContent = ''
gServer = None

if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi0",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip

def sendPaste(data):
    pass


def setClipboard(data):
    print('set clipboardto:'+ data)
    pyperclip.copy(data)
    gLastContent = data
    pass


def getClipboardData():
    return pyperclip.paste()


def isClipDataChanged():
    return gLagLastContentstContent != getClipboardData()


def listenProc(svr):
    while True:
        data, addr = svr.recvfrom(2048)
        str = data.decode()
        ip = addr[0]
        print("rcv datafrom:" + ip)
        if (ip != get_lan_ip())  and len(str) > 0:
            setClipboard(str)
        time.sleep(3)
    pass


def run(port):
    gServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    gServer.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    gServer.bind(('', port))

    t = Thread(target=listenProc, args=(gServer,))
    t.start()
    while True:
        if isClipDataChanged():
            print("clipboard data changed..")
            str = getClipboardData()
            gLastContent = str
            gServer.sendto(bytes(str, "utf-8"), ("255.255.255.255", port))
        time.sleep(3)
    pass


run(6000)