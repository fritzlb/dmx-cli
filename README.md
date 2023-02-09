# dmx-cli
A simple tool to send DMX data from CLI - written in Python 3.8+

Runs on RPi 4. Enable UART3 (add dtoverlay=uart3 to /boot/config.txt) and the script will run without any changes.
On GPIO 4 then a tiny hardware is needed to convert UART logic levels to DMX (RS485) logic levels, for example a Max485 or a Texas Instruments SN75176 (a lot cheaper than Max485 but uses a little more power).

Start dmx-server.py and you should be able to control it by running dmx-cli.py. Just run dmx-cli.py for instructions on how to use.


In theory this should also run on other platforms with pyserial installed, maybe changing the serial port in dmx-server.py is required. I didn't test anything except for Pi 4 support.

Now also part of homebridge-dmxplugin
