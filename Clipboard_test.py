# -*- coding: utf-8 -*-

import serial																		#imports the necessary modules
import platform
import time
from pykeyboard import PyKeyboard
import clipboard

k = PyKeyboard()																	#creates an instance of pykeyboard

symbols = [u'π', u'Σ', ':^)', 'sure kid', 'me too thanks', 'FeelsBindMan']									#the list of symbols that can be pasted

ser = serial.Serial('/dev/ttyACM0')													#the port the arduino is connected to

while True:
	while ser.readline().decode('utf-8')[:2]:
		board = clipboard.paste()
		#clipboard.copy(board + ' 1')
		#print clipboard.paste()
		clipboard.copy('meep')
		#clipboard.copy(symbols[int(ser.read())-1])
		clipboard.copy(board)
		#print symbols[int(ser.read())-1]
		#clipboard.copy(board + ' 1')
		print clipboard.paste()
