
#!/bin/bash
#killall -9 python3
#sudo killall -9 python3
#python3 Firmware.py

sleep 5
(sudo /usr/bin/python3 /home/pi/SmartInCarDisplay/Firmware/Firmware.py >/home/pi/SmartInCarDisplay/Firmware/main_logs.txt 2>&1)

