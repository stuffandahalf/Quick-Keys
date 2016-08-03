# -*- coding: utf-8 -*-

import serial																		#importing main program modules
import platform
import time
from pykeyboard import PyKeyboard
import clipboard

k = PyKeyboard()																	#creates an instance of pykeyboard
																					#dictonary of symbols
symbols = {'1' : u'π',
		   '2' : u'Σ',
		   '3' : ':^)',
		   '4' : 'sure kid',
		   '5' : 'me too thanks',
		   '6' : 'FeelsBindMan'}
		   
ser = serial.Serial('/dev/ttyACM0')													#the port the arduino is connected to

while True:																			#main loop
	#print ser.read()
	while ser.readline().decode('utf-8')[:2]:										#when there is a relevant serial value
		try:																		#try to run the main script
			ind = ser.read()
			#print ind
			board = clipboard.paste()												#store the clipboard contents in the variable
			clipboard.copy(symbols[ind])
			#print symbols[ind]
			#print clipboard.paste()
			if platform.system() == 'Linux' or platform.system() == 'Windows' :		#for windows and linux
				k.press_key('Control_L')											#paste the clipboard
				k.tap_key('v')
				k.release_key('Control_L')
				#k.tap_key('Return')
			elif platform.system() == 'Darwin':
				pass
			time.sleep(.1)															#pause for .1 seconds
			clipboard.copy(board)													#restore the clipboard contents
						
		except:																		#if there is an error
			pass	
