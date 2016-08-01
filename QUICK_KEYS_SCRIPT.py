# -*- coding: utf-8 -*-

import serial																		#imports the necessary modules
import platform
import time
from pykeyboard import PyKeyboard
import clipboard

k = PyKeyboard()																	#creates an instance of pykeyboard

symbols = [u'π', u'Σ', ':^)', 'sure kid', 'E', 'F']											#the list of symbols that can be pasted

ser = serial.Serial('/dev/ttyACM0')													#the port the arduino is connected to
	

while True:																			#main loop
	if ser.readline().decode('utf-8')[:2]:									#when there is a relevant serial value
		try:																		#try to run the main script
			board = clipboard.paste()												#store the clipboard contents in the variable
			#print board
			clipboard.copy(symbols[int(ser.read())-1])								#copy the symbol to the clipboard
			if platform.system() == 'Linux' or platform.system() == 'Windows' :		#for windows and linux
				k.press_key('Control_L')											#paste the clipboard
				k.tap_key('v')
				k.release_key('Control_L')
				#k.tap_key('Return')
			elif platform.system() == 'Darwin' :
				pass
			time.sleep(.1)															#pause for .1 seconds
			clipboard.copy(board)													#restore the clipboard contents
			
		except:																		#if there is an error
			pass																#do not print anything

