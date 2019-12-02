#!/usr/bin/env python3
import sys
import cgi
import time
from parser import *
from invertor import Invertor

form = cgi.FieldStorage()
# Try find command in browser request  if not have then 'QPIGS'
# Supported command 'QPIGS','QDI','QMOD','QPIRI'
try:
    com_form=form.getvalue("com")
    if com_form in ('QPIGS','QDI','QMOD','QPIRI'):
        command = com_form
    else:
        command ='QPIGS'
except:
    command ='QPIGS'

# Initialize  USB port
sila=Invertor()

def request(command):
    sila.send(Command(command))
    respond=sila.get()

    reply=parse_resp(command,respond)
    #Check error
    if json.loads(reply)["error"]:
        # If error try one more
        #print('one more')

        sila.send(Command(command))
        respond=sila.get()
        return  parse_resp(command,respond)
    else:
        return reply


#Respond to browser

print ("Content-type: application/json")
print () 
print(request(command))
