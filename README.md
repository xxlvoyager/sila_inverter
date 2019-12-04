# sila_inverter
WEB monitor Solar Inverter SILA based on Raspberry Pi respond in JSON format.

Supported command 'QPIGS','QDI','QMOD','QPIRI'

 ### SETUP
 Select type of port in *inveror.ini*
 
For ```/dev/hidraw0```

Create */etc/udev/rules.d/15-sila.rules*
add line in file <br>
 ```KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0666", GROUP="plugdev"```
<br> reload udev via command<br>
```sudo udevadm control --reload-rules```
<br>
```sudo udevadm trigger```
<br>
Connect Inverter to USB port Raspberry directly (/dev/hidraw0)
or via tty converter (/dev/ttyUSB0)
<br>
Make py files in folder ```sila_inverter/cgi```  executable. 
<br> Run ```python3 sila_inverter/server.py```
 Now web server aviable on port 5000. ( can change in *ivertor.ini*)
<br>
 ### USING
 

    - List aviable command:
    
    http://machine_ip:5000/
    
    
    - Operation Mode (QMOD) as JSON:
    
    http://machine_ip:5000/cgi/sila.py?com=QMOD
    
    
    - Status  (QPIGS) as JSON:
    
    http://machine_ip:5000/cgi/sila.py?com=QPIGS
  
 



