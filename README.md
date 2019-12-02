# sila_inverter
WEB monitor Solar Inverter SILA based on Raspberry Pi respond in JSON format.

Supported command 'QPIGS','QDI','QMOD','QPIRI'

 ### SETUP

Create */etc/udev/rules.d/15-sila.rules*
add line to file<br>
 ```KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0666", GROUP="plugdev"```
<br>reload udev via command ```sudo udevadm trigger```

Connect Inverter to USB port Raspberry
<br>
Make py files in folder ```sila_inverter/cgi```  executable. 
Run ```python3 sila_inverter/server.py```
 Now web server aviable on port 5000.
<br>
 ### USING
 

    - List aviable command:
    
    http://machine_ip:5000/
    
    
    - Operation Mode (QMOD) as JSON:
    
    http://machine_ip:5000/cgi/sila.py?com=QMOD
    
    
    - Status  (QPIGS) as JSON:
    
    http://machine_ip:5000/cgi/sila.py?com=QPIGS
  
 



