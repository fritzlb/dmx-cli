#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import shared_memory
from multiprocessing import resource_tracker
import sys

try:
	data = shared_memory.ShareableList(sequence=None, name='dmxdata')
except Exception as error:
	print("It seems like the server application isn't running :(")
	print(error)
	exit()


args = sys.argv[1:]
if len(args) == 0:
	print("dmx-cli by fritzlb")
	print()
	print("Usage: dmx-cli.py -channel value")
	print()
	print("Changing multiple channels at once is supported.")
	print("dmx-cli.py -channel1 value1 -channel2 value2 ...")

for i in range(len(args)):
	if args[i][:1] == '-':
		parse_ok = True
		try:
			channel = int(args[i][1:])
			value = int(args[i+1])
		except:
			print("ERROR: Received invalid channel number or value")
			parse_ok = False
			channel = 1 #this isn't parsed, everything's fine
			value = 0
		if channel == 0:
			print("WARNING: You are modifying the DMX start byte. This is NOT officially supported.")
		elif (channel > 512):
			print("ERROR: You tried setting channel " + str(channel) + ". This is out of range (0..512).")
			parse_ok = False
		if value < 0 or value > 255:
			print("ERROR: Value too high or too low")
			parse_ok = False

		if parse_ok:
			data[channel] = value


#data[0] = 0 #NEVER set data[0] to anything but 0 bc that's our DMX start byte. It would prevent your fixtures from reacting to the DMX stream
data.shm.close()
resource_tracker.unregister('/dmxdata', 'shared_memory') #unlinking resource_tracker to keep sharedmemory... else our dmx-server crashes


