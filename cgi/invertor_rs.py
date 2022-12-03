#!/usr/bin/env python3
import configparser
import serial
import time
import re
import crc16
import json
from collections import OrderedDict


config = configparser.ConfigParser()
config.read('invertor.ini')
port = config['DEFAULT']['port']

len_res = {'QPIGS': 110, 'QPIRI': 97, 'QMOD': 5, 'QDI': 79}


def Xcommand(cmd):
    cmd = cmd.encode('utf-8')
    crc = crc16.crc16xmodem(cmd).to_bytes(2, 'big')
    cmd = cmd+crc
    cmd = cmd+b'\r'
    while len(cmd)<8:
        cmd = cmd+b'\0'
    return cmd

class Invertor(object):
    def __init__(self):

        self.ser = serial.Serial(port)
        self.ser.baudrate = 2400
        self.ser.bytesize = serial.EIGHTBITS     # number of bits per bytes
        self.ser.parity = serial.PARITY_NONE     # set parity check: no parity
        self.ser.stopbits = serial.STOPBITS_ONE  # number of stop bits
        self.ser.timeout = 1                     # non-block read
        self.ser.xonxoff = False                 # disable software flow control
        self.ser.rtscts = False                  # disable hardware (RTS/CTS) flow control
        self.ser.dsrdtr = False                  # disable hardware (DSR/DTR) flow control
        self.ser.writeTimeout = 2                # timeout for write

    def close(self):

        self.ser.close()

    def write(self, command):
        resp_len = len_res[command]
        res = ''
        if self.ser.isOpen():
            try:
                self.ser.flushInput()            #flush input buffer, discarding all its contents
                self.ser.flushOutput()           #flush output buffer, aborting current output and discard all that is in buffer
                self.ser.write(Xcommand(command))
                time.sleep(0.1)             #give the serial port sometime to receive the data
                i = 0
                while '\r' not in res and i < 20:
                    res += "".join([chr(i) for i in self.ser.read(8)])
                    i += 1
            except Exception as err:
                return ('Error as', err)
        else: 
            return ('Error', 'port')
        # print(res)
        # print(len(res))
        if len(res) == resp_len:
            return res
        else :
            return ('Error', 'len_resp')


if __name__ == '__main__':
    sila = Invertor()
    respond = sila.write('QPIGS')

    print(respond)
    time.sleep(0.2)
    respond = sila.write('QPIRI')
    print(respond)
    time.sleep(0.2)
    respond = sila.write('QMOD')
    print(respond)
    time.sleep(0.2)
    respond = sila.write('QDI')
    print(respond)
    sila.close()