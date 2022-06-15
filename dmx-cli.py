#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import shared_memory
from multiprocessing import resource_tracker


try:
	data = shared_memory.ShareableList(sequence=None, name='dmxdata')
except:
	print("It seems like the server application isn't running :(")
	exit()
print(data)
data[1] = 255 #NEVER modify data[0] bc that's our DMX start byte. It would prevent your fixtures from reacting to the DMX stream
data.shm.close()
resource_tracker.unregister('/dmxdata', 'shared_memory') #unlinking resource_tracker to keep sharedmemory... else our dmx-server crashes

