#!/usr/bin/env python3
import time
import crc16
import usb
import usb.core
import usb.util
import usb.control
import logging

logging.basicConfig(filename='app.log', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
log = logging.getLogger('main')

# USB setiing 
vendorId = 0x0665
productId = 0x5161
interface = 0


def Command(cmd):
    cmd = cmd.encode('utf-8')
    crc = crc16.crc16xmodem(cmd).to_bytes(2, 'big')
    cmd = cmd + crc
    cmd = cmd+b'\r'
    while len(cmd)<8:
        cmd = cmd+b'\0'
    return cmd


class Invertor(object):

    def __init__(self):
        self.log = log
        self.dev = usb.core.find(idVendor=vendorId, idProduct=productId)
        if self.dev.is_kernel_driver_active(interface):
            self.dev.detach_kernel_driver(interface)
        self.dev.set_interface_altsetting(0, 0)

    def write(self,cmd):
        self.dev.ctrl_transfer(0x21, 0x9, 0x200, 0, Command(cmd))
        log.debug(cmd)
        timeout = 50
        res = ""
        i=0
        while '\r' not in res and i<20:
            try:
                res += "".join([chr(i) for i in self.dev.read(0x81,8, timeout) ])
            except usb.core.USBError as e:
                if e.errno == 110:
                    log.debug(e)
                else:
                    raise
            i += 1
        log.debug(res)
        return res


if __name__ == '__main__':
    sila = Invertor()
    sila.send(b'QPIGS\xb7\xa9\r')
    print(sila.get())
