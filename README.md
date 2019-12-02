# sila_inverter
WEB monitor Solar Inverter SILA based on Raspberry Pi
Reply in JSON format.
Supported command 'QPIGS','QDI','QMOD','QPIRI'
#SETUP
Create /etc/udev/rules.d/15-sila.rules
add line 
KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0666", GROUP="plugdev"
reload 
udev sudo udevadm trigger
Connect Inverter to USB port Raspberry
run server.py
web page aviable on port 5000


