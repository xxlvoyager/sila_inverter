# sila_inverter
WEB monitor Solar Inverter SILA based on Raspberry Pi
Reply in JSON format.
<br>
Supported command 'QPIGS','QDI','QMOD','QPIRI'
<br>
<b>SETUP</b>
<br>
Create <i>/etc/udev/rules.d/15-sila.rules</i>
add line 
KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0666", GROUP="plugdev"
reload udev command
<i>sudo udevadm trigger</i>

Connect Inverter to USB port Raspberry
run server.py
web page aviable on port 5000


