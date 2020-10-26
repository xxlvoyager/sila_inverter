#!/usr/bin/env python3
import configparser
import sys
import cgi
import time
from parser import *

config = configparser.ConfigParser()
config.read('invertor.ini')

if 'tty' in config['DEFAULT']['port']:
    from invertor_rs import Invertor
else:
    from invertor_hr import Invertor

form = cgi.FieldStorage()
# Try find command in browser request  if not have then 'QPIGS'
# Supported command 'QPIGS','QDI','QMOD','QPIRI'
try:
    com_form = form.getvalue("com")
    if com_form in ('QPIGS', 'QDI', 'QMOD', 'QPIRI'):
        command = com_form
    else:
        command = 'QPIGS'
except:
    command = 'QPIGS'

# Initialize  USB port
sila = Invertor()

respond = sila.write(command)
if 'Error' in respond:
    print("Content-type: text/html")
    print()
    print('<!DOCTYPE html>')
    print('<h1>', respond, '</h1>')
else:
    reply = parse_resp(command, respond)
    print("Content-type: application/json")
    print()
    print(reply)
