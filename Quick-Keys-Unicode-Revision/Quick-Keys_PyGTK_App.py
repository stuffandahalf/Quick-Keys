#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Source: Quick-Keys_PyGTK_App.py

#importing main program modules
import threading
import serial
import platform
import time
import sys
import glob
from pykeyboard import PyKeyboard

#importing gui components
import pygtk
pygtk.require('2.0')
import gtk

k = PyKeyboard()

window_height = 300
window_width = 313

pref_file = 'Quick-Keys Preferences'

rows = 2
columns = 3

#dictionary of symbols corresponding to the arduino
symbols = {'1' : 'π',
           '2' : 'Σ',
           '3' : 'α',
           '4' : 'β',
           '5' : 'Δ',
           '6' : 'Ω'}

coords = []
for x in range(rows):
    for y in range(columns):
        coords.append([(window_height/rows+1)*x+1, (window_width/columns)*y+1])
        
print coords

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
                
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
    
def save_preferences():
    f = open(pref_file, 'w+')
    for i in symbols:
        f.write(symbols[i] + '\n')
    f.write(ser + '\n')
    
def read_preferences():
    f = open(pref_file)
    for i in symbols:
        symbols[i] = f.readline()[:2]
    ser = f.readline()[:2]



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
            layout.put(entry, coords[int(i)-1][0], coords[int(i)-1][1]) # place the text box on the layout
            entry.show()                                                # 
    
        drop = gtk.combo_box_new_text()
        layout.put(drop, 250, 50)
    
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
    
    ports = serial_ports()
    print ports
    main_window = Base()                                                # create a window object
    main_window.main()                                                  # run the object
