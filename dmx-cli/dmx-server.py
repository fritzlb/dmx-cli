#!/usr/bin/python
# -*- coding: utf-8 -*-
import serial
import time
from multiprocessing import shared_memory
import atexit

dmxconnection = False
while not dmxconnection:
	try:
		dmx = serial.Serial('/dev/ttyAMA1', baudrate=250000, bytesize=8, stopbits=2)
		dmxconnection = True
	except:
		print("Serial not available.")
		exit()
i = 1
empty_data_list = []
for i in range(513):
	empty_data_list.append(0x00)
try:
	data = shared_memory.ShareableList(empty_data_list, name='dmxdata')
except:
	print("This server application seems to be already running.")
	exit()

def sendDMXdirect(dataIN):
	dmx.break_condition = True
	time.sleep(120/1000000.0)
	dmx.break_condition = False
	time.sleep(12/1000000.0)
	dmx.write(bytearray(dataIN))
def cleanupmess():
	global data
	data.shm.unlink()
	data.shm.close()
	del data
atexit.register(cleanupmess)

while True:
	sendDMXdirect(data)
