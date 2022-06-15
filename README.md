# dmx-cli
A simple tool to generate DMX data from CLI - written in Python

Runs on RPi 4. Enable UART3 (add dtoverlay=uart3 to /boot/config.txt) without modifications.
On GPIO 4 then a tiny hardware is needed, for example a Max485 or SN75176. A basic setup with 2 NPN transistors is possible, too.

Start dmx-server.py and you should be able to control it by running dmx-cli.py. currently WIP, you'll need to modify the code.
