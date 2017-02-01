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

window_height = 300
window_width = 300

#dictionary of symbols corresponding to the arduino
symbols = {'1' : 'π',
           '2' : 'Σ',
           '3' : 'α',
           '4' : 'β',
           '5' : 'Δ',
           '6' : 'Ω'}

for x in rows:
    for y in columns:
        coords[x+1*y+1] = 

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
        self.window.set_default_size(window_width, window_height)
        self.window.show()
        
        layout = gtk.Layout()
        self.window.add(layout)
        layout.show()
        
        for i in symbols:                                               # for every symbol
            entry = gtk.Entry()                                         # make a text box
            entry.set_max_length(10)                                    # set the max length a symbol can be to 10
            entry.set_text(symbols[str(i)])                             # set the default text in the box to the current symbol
            layout.put(entry, 300/6*int(i)+1, 300/6*int(i)+1)           # place the text box on the layout
            entry.show()                                                # 
    
    def main(self):
        gtk.main()

if __name__ == '__main__':
    gtk.threads_init()                                                  # initialize threads in gtk
    t1 = threading.Thread(target = main_script)                         # create a new thread for the main script
    
    #try to set the port of the arduino
    try:
        #ser = serial.Serial('/dev/ttyACM0')
        ser = serial.Serial('/dev/ttyUSB0')
        #ser = serial.Serial('/dev/tty.usbmodem1A21')
        t1.start()                                                      # start the new thread
        print 'Serial port set to ' + ser.port
        
    #if none found, dont start thread
    except:
        ser = ''
        print 'Serial port not found, please set later'
    
    main_window = Base()                                                # create a window object
    main_window.main()                                                  # run the object
