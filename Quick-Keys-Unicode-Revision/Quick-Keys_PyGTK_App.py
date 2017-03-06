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
from text_prompt import getText

#importing gui components
import pygtk
pygtk.require('2.0')
import gtk

k = PyKeyboard()
ser = serial.Serial(None)

window_height = 300
window_width = 300

rows = 2       #6 button version
columns = 3

#rows = 3        #12 button version
#columns = 4

pref_file = 'Quick-Keys Preferences'

#dictionary of symbols corresponding to the arduino
symbols = {'1' : 'π',          #6 button version
           '2' : 'Σ',
           '3' : 'α',
           '4' : 'β',
           '5' : 'Δ',
           '6' : 'Ω'}
           
#symbols = {'1' : 'π',           #12 button version
           #'2' : 'Σ',
           #'3' : 'α',
           #'4' : 'β',
           #'5' : 'Δ',
           #'6' : 'Ω',
           #'7' : 'test',
           #'8' : 'another',
           #'9' : 'and again',
           #'10' : 'last one',
           #'11' : 'ayy',
           #'12' : 'lmao'}


#a dictionary to store the changed symbols
new_symbols = {}
for i in symbols:
    new_symbols[i] = symbols[i]

def main_script():
    while ser.port != None:
        try:
            ind = ser.readline().rstrip('\r\n')
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
            ser.close()
            ser.port = None
                
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
    f = open(pref_file, 'w+')                                           # open the preference file
    for i in symbols:                                                   # for every symbol
        f.write(symbols[i] + '\n')                                      # write them to the file
    if ser.port != None:                                                # if the current serial port is valid
        f.write(ser.port + '\n')                                        # write it to the file
    else:                                                               # otherwise
        f.write('\n')                                                   # write a newline character
    
def read_preferences():
    global ser                                                          # define the ser variable as global
    f = open(pref_file)                                                 # open the preference file
    for i in symbols:                                                   # for every symbol
        sym = f.readline().rstrip('\r\n')
        #symbols[i] = f.readline().rstrip('\r\n')                        # set the current symbols to the value from the file
        #new_symbols[i] = f.readline().rstrip('\r\n')
        symbols[i] = sym
        new_symbols[i] = sym
        
        
    new_port = f.readline().rstrip('\r\n')                              # read the new port from the file
    print new_port
    if new_port != '' and new_port in serial_ports():                   # if the new port is a valid port
        ser = serial.Serial(new_port)                                   # set the serial port to it
        print_serial_change()                                           # print the changes
    else:                                                               # otherwise
        print 'Error setting serial port. Try again later.'             # print a warning
        ser = serial.Serial(None)                                       # change the port to None

def print_serial_change():
    print 'Serial port has been set to ' + ser.port
    
def print_symbol_changes():
    print 'Symbols have been changed to: '
    for i in symbols:
        print symbols[i]

class Unplugged:
    '''
    class for window to prompt user to reconnect
    '''
    def __init__(self):
        pass

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
        self.add_refresh_load_buttons(layout)
    
    def add_primary_buttons(self, layout):
        button_size = (window_width/columns, window_height/(rows+1))    # calculate the size of the buttons
        button_coords = []                                              # a list of coordinates for the buttons
        for y in range(rows):                                           # for every row
            for x in range(columns):                                    # for every column
                button_coords.append((button_size[0]*x, button_size[1]*y))  # add the coordinates of that button to the list
        
        self.button = []                                                # list of buttons
        for i in range(len(symbols)):                                   # for every symbol
            self.button.append(gtk.Button(label = symbols[str(i+1)]))   # make a new button object
            self.button[i].set_size_request(button_size[0], button_size[1])     # set the size of the button
            self.button[i].connect('clicked', self.button_symbols, i)            # bind the button to the test function
            layout.put(self.button[i], button_coords[i][0], button_coords[i][1])    # place the button on the layout
            self.button[i].show()                                       # show the button

    def add_serial_port_dropdown(self, layout):
        self.drop = gtk.combo_box_new_text()                            # create a new combo box object
        drop_size = (window_width/3*2, window_height/(rows+1)/2)        # the size of the drop down box
        self.drop.set_size_request(drop_size[0], drop_size[1])          # set the size of the drop down
        self.drop.set_title('Serial Ports')                             # set the title (wip)
        self.ports = serial_ports()                                     # create a list of available ports
        print self.ports
        #try:
            #self.drop.set_active(self.ports.index(ser.port))
        #except:
            #pass
        for i in self.ports:                                            # for every port
            self.drop.append_text(i)                                    # add it to the dropdown
        drop_coords = (0, window_height/(rows+1)*rows)                  # the coordinates of the drop
        layout.put(self.drop, drop_coords[0], drop_coords[1])           # place it on the layout
        self.drop.show()                                                # show the drop
    
    def refresh_serial_dropdown(self, widget, data = None):
        for i in range(len(self.ports)):                                # for every port in the current list
            self.drop.remove_text(0)                                    # remove the values from the dropdown
        self.ports = serial_ports()                                     # refresh the list of ports
        for i in self.ports:                                            # for every new port
            self.drop.append_text(i)                                    # add it to the dropdown
        self.clear_symbol_changes()
        #print self.ports
        
    def button_symbols(self, widget, data = None):
        data += 1
        new_symbols[str(data)] = getText(symbols[str(data)])
        print data
        #self.drop.append_text('test')
        #self.ports.append('test')
        #print self.ports
        self.refresh_symbols()
        #print self.drop.get_row_span_column()  
    
    def refresh_symbols(self):
        for i in range(len(new_symbols)):
            self.button[i].set_label(new_symbols[str(i+1)])
            
    def clear_symbol_changes(self):
        for i in range(len(new_symbols)):
            self.button[i].set_label(symbols[str(i+1)])
    
    def add_apply_button(self, layout):
        button_size = (window_width/3, window_height/(rows+1))          # tuple holding the size of the button
        button = gtk.Button(label = 'apply')                            # creating another button object
        button.set_size_request(button_size[0], button_size[1])         # set the size of the button
        button_coord = (window_width-button_size[0], button_size[1]*(rows))     # tuple holding the location of the button
        button.connect('clicked', self.apply_changes, self.get_drop_text())     # bind the button to apply_changes()
        layout.put(button, button_coord[0], button_coord[1])            # place the button on the layout
        button.show()                                                   # show the button
    
    def add_refresh_load_buttons(self, layout):
        button_size = (window_width/3, window_height/(rows+1)/2)        # tuple to store dimension of buttons
        refresh = gtk.Button(label = 'refresh')                             # create button object
        refresh.set_size_request(button_size[0], button_size[1])          # set the size of the button to the tuple
        button_coord = (0, button_size[1]*(rows*2+1))                   # tuple containing the top left coordinates of the button
        refresh.connect('clicked', self.refresh_serial_dropdown, '')       # bind the button to redraw the serial drop down
        layout.put(refresh, button_coord[0], window_height-button_size[1])# place the button on the layout
        refresh.show()                                                    # show the button
        
        load = gtk.Button(label = 'load')                               # create another button object with label load
        load.set_size_request(button_size[0], button_size[1])           # set the size to the size tuple
        button_coord = (window_width/3, window_height-button_size[1])   # tupe containing the coordinates of the top left corner
        load.connect('clicked', self.read_preferences_bind, '')              # bind the button to read_preferences()
        layout.put(load, button_coord[0], button_coord[1])              # place the load button on the layout
        load.show()                                                     # show the button
     
    def get_drop_text(self):
        return self.drop.get_active_text()
           
    def read_preferences_bind(self, widget, data = None):
        read_preferences()                                                  # a method to bind read_preferences() to a widget
        self.refresh_symbols()  
    
    def apply_changes(self, widget, data = None):
        print 'function to apply changes'
        new_port = self.get_drop_text()                                 # get new serial port from drop down
        if new_port != None and new_port in serial_ports():             # if port is valid
            ser.close()                                                 # close the current one
            ser.port = None                                             # set serial port to None to close current thread
            print new_port                                              
            ser.port = new_port                                         # set the serial port to the new port
            ser.open()                                                  # reopen the serial port
            threading.Thread(target = main_script).start()              # start a new script thread
            print_serial_change()                                       # print the changes made
        else:
            print 'invalid Serial port selected, port not changed'      # if invalid port selected, print message and proceed
            
        for i in new_symbols:                                           # for every symbol
            symbols[i] = new_symbols[i]                                 # update the value
        self.refresh_symbols()
        print_symbol_changes()                                          # print the changes
        save_preferences()                                              # write the changes to the preferences file
    
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
        #t1.start()                                                     # start the new thread
        #print 'Serial port set to ' + ser.port
        
    ##if none found, dont start thread
    #except:
        #ser = ''
        #print 'Serial port not found, please set later'
    
    #check if preferences file exists
    if os.path.isfile(pref_file):                                       # if the preferences file exists
        read_preferences()                                              # read the symbols and port from it
        
    else:                                                               # if it doesnt
        save_preferences()                                              # create it using default values
        print 'Preference file saved'
    
    if ser.port in serial_ports():                                      # if the serial port read from the file is valid
        t1.start()                                                      # start the script thread
    else:
        print 'Please set port to launch script'                        # otherwise warn the user
    
    main_window = Base()                                                # create a window object
    main_window.main()                                                  # run the object
