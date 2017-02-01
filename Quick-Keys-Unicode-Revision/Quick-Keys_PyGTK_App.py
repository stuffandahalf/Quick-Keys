#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Quick-Keys_PyGTK_App.py

#importing main program modules
import threading
import serial
import platform
import time
from pykeyboard import PyKeyboard

#importing gui components
import pygtk
pygtk.require('2.0')
import gtk

k = PyKeyboard()

#the port the arduino is connected to
#ser = serial.Serial('/dev/ttyACM0')
ser = serial.Serial('/dev/ttyUSB0')
#ser = serial.Serial('/dev/tty.usbmodem1A21')

#dictionary of symbols corresponding to the arduino
symbols = {'1' : u'π',
		   '2' : u'Σ',
		   '3' : ':^)',
		   '4' : 'sure kid',
		   '5' : 'me too thanks',
		   '6' : 'FeelsBindMan'}

def main_script():
    while True:
        while ser.readline().decode('utf-8')[:2]:
            try:
                ind = ser.read()
                #print ind
                hexval = symbols[ind].encode("unicode_escape")
                print hexval
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
                        
                    elif platform.system() == 'Windows':
                        pass
                        
                    elif platform.system() == 'Darwin':
                        pass
                    
                    else:
                        print 'Unsupported platform'
                        
                else:
                    k.type_string(hexval)
                
            except:
                pass

class Base:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.show()
    
    def main(self):
        gtk.main()

if __name__ == '__main__':
    t = threading.Thread(target = main_script)
    t.start()
    #main_window = Base()
    Base().main()
