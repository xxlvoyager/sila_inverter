# sila_inverter
<img src='https://img.shields.io/badge/WEB MONITOR-SILA INVERTER-blue?style=for-the-badge&logo=appveyor'>

WEB monitor Solar Inverter SILA based on Raspberry Pi respond in JSON format.

Supported command 'QPIGS','QDI','QMOD','QPIRI'


 ## SETUP
Connect Inverter to USB port Raspberry directly (/dev/hidraw0)
or via tty converter (/dev/ttyUSB0)

Select type of port in *invertor.ini* <br>

For `/dev/hidraw0` Create */etc/udev/rules.d/15-sila.rules*

add line in file 

 `KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0666", GROUP="plugdev"`

reload udev via command

`sudo udevadm control --reload-rules`


`sudo udevadm trigger`


Make py files in folder `sila_inverter/cgi`  executable. 

Run `python3 sila_inverter/server.py`

> Now web server aviable on port 5000.


 ## USING
 

###    - List available command:
    
    http://machine_ip:5000/
    
    
###    - Operation Mode (QMOD) as JSON:
    
    http://machine_ip:5000/cgi/sila.py?com=QMOD
    
    
###    - Status  (QPIGS) as JSON:
    
    http://machine_ip:5000/cgi/sila.py?com=QPIGS
  
 



