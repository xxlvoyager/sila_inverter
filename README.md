# sila_inverter
WEB monitor Solar Inverter SILA based on Raspberry Pi respond in JSON format.

Supported command 'QPIGS','QDI','QMOD','QPIRI'

 ### SETUP

Create ```/etc/udev/rules.d/15-sila.rules```
add line to file<br>
 ```KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0666", GROUP="plugdev"```
reload udev via command ```sudo udevadm trigger```

Connect Inverter to USB port Raspberry
<br>
make *.py files in folder cgi  executable 
run python3 server.py
Now web server aviable on port 5000
<BR>
 ### USING
 

    - List avable command:
    
    http://machine_ip:5000/
    
    
    - Operation Mode (QMOD) as JSON:
    
    http://machine_ip:5000/cgi/sila.py?com=QMOD
    
    
    - Status  (QPIGS) as JSON:
    
    http://machine_ip:5000/cgi/sila.py?com=QPIGS
  
 



