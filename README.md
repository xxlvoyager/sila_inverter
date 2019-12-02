# sila_inverter
WEB monitor Solar Inverter SILA based on Raspberry Pi respond in JSON format.
<br>
Supported command 'QPIGS','QDI','QMOD','QPIRI'
<br>
###SETUP
<br>
Create ```/etc/udev/rules.d/15-sila.rules```
add line to file<br>
```KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0666", GROUP="plugdev"```
<br>
reload udev command
```sudo udevadm trigger```

Connect Inverter to USB port Raspberry<br>
make py files, include folder cgi  executable 
run server.py <br>

web page aviable on port 5000
<BR>
    ```

    - Operation Mode (QMOD) as JSON:
    
    ```
    http://machine_ip:5000/cgi/sila.py?com=QMOD
    
    
    - Status  (QPIGS) as JSON:
    ```
    http://machine_ip:5000/cgi/sila.py?com=QPIGS
  
  
    ```



