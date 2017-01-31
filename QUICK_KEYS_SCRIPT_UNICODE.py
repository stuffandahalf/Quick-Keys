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
		   
#ser = serial.Serial('/dev/ttyACM0')													#the port the arduino is connected to
ser = serial.Serial('/dev/ttyUSB0')
#ser = serial.Serial('/dev/tty.usbmodem1A21')

while True:
    while ser.readline().decode('utf-8')[:2]:
        try:
            ind = ser.read()
            #print ind
            hexval = symbols[ind].encode("unicode_escape")
            #print hexval
            if hexval[:2] == '\u':
                if platform.system() == 'Linux':
                    k.press_key('Control_L')
                    k.press_key('Shift_L')
                    k.tap_key('u')
                    k.release_key('Control_L')
                    k.release_key('Shift_L')
                    hexval = hexval[2:]
                    k.type_string(hexval)
                    k.tap_key('Return')
            else:
                k.type_string(hexval)
            
        except:
            pass
