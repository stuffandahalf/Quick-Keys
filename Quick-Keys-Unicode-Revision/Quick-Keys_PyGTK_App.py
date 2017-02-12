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
import os.path
from pykeyboard import PyKeyboard

#importing gui components
import pygtk
pygtk.require('2.0')
import gtk

k = PyKeyboard()
ser = ''

window_height = 300
window_width = 300

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

#a dictionary to store the changed symbols
new_symbols = {}
for i in symbols:
    new_symbols[i] = symbols[i]

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
    try:
        f.write(ser.port + '\n')
    except:
        f.write(ser + '\n')
    
def read_preferences():
    f = open(pref_file)
    for i in symbols:
        symbols[i] = f.readline().rstrip('\r\n')
    port = f.readline().rstrip('\r\n')
    try:
        ser = serial.Serial(port)
        print ser.port
    except:
        print 'Error setting serial port. Try again later.'
        ser = ''
    

def apply_changes(widget, data = None):
    print 'function to apply changes'
    read_preferences()

class Base:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_default_size(window_width, window_height)
        self.window.set_size_request(window_width, window_height)
        self.window.show()
        self.window.set_title('Quick-Keys')
        self.window.set_icon_from_file('icon.png')
        
        layout = gtk.Layout()
        self.window.add(layout)
        layout.show()
        
        self.add_primary_buttons(layout)
        self.add_serial_port_dropdown(layout)
        self.add_apply_button(layout)
    
    def add_primary_buttons(self, layout):
        button_size = (window_width/columns, window_height/(rows+1))
        button_coords = []
        for x in range(columns):
            for y in range(rows):
                button_coords.append((button_size[0]*x, button_size[1]*y))
        
        for i in range(len(symbols)):
            button = gtk.Button(label = symbols[str(i+1)])
            button.set_size_request(button_size[0], button_size[1])
            
            layout.put(button, button_coords[i][0], button_coords[i][1])
            button.show()

    def add_serial_port_dropdown(self, layout):
        drop = gtk.combo_box_new_text()
        drop_size = (window_width/columns*2, window_height/(rows+1))
        drop.set_size_request(drop_size[0], drop_size[1])
        ports = serial_ports()
        for i in ports:
            drop.append_text(i)
        drop_coords = (0, window_height/(rows+1)*rows)
        layout.put(drop, drop_coords[0], drop_coords[1])
        drop.show()
    
    def add_apply_button(self, layout):
        button_size = (window_width/columns, window_height/(rows+1))
        button = gtk.Button(label = 'apply')
        button.set_size_request(button_size[0], button_size[1])
        button_coord = (button_size[0]*(columns-1), button_size[1]*(rows))
        button.connect('clicked', apply_changes, '')
        
        layout.put(button, button_coord[0], button_coord[1])
        button.show()
    
    def main(self):
        gtk.main()

if __name__ == '__main__':
    
    gtk.threads_init()                                                  # initialize threads in gtk
    t1 = threading.Thread(target = main_script)                         # create a new thread for the main script
    
    #try to set the port of the arduino
    #try:
        ##ser = serial.Serial('/dev/ttyACM0')
        #ser = serial.Serial('/dev/ttyUSB0')
        ##ser = serial.Serial('/dev/tty.usbmodem1A21')
        #t1.start()                                                      # start the new thread
        #print 'Serial port set to ' + ser.port
        
    ##if none found, dont start thread
    #except:
        #ser = ''
        #print 'Serial port not found, please set later'
    
    #check if preferences file exists
    print symbols
    print ser
    if os.path.isfile(pref_file):
        read_preferences()
        
    else:
        save_preferences()
        print 'Preference file saved'
        
    #print symbols
    print ser.port
        
    main_window = Base()                                                # create a window object
    main_window.main()                                                  # run the object
