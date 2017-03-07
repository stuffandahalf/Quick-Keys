#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  button_test.py

import pygtk
pygtk.require('2.0')
import gtk

import sys
import glob
import serial
import threading

window_height = 300
window_width = 300

rows = 2
columns = 3

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

class Base:
    drop = gtk.combo_box_new_text()
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_default_size(window_width, window_height)
        self.window.set_size_request(window_width, window_height)
        self.window.show()
        layout = gtk.Layout()
        self.window.add(layout)
        layout.show()
        
        button = gtk.Button()
        button.connect('clicked', self.get_text, self.drop.get_active_text())
        layout.put(button, 50, 50)
        button.show()
        
        self.set_drop(layout)
        #print drop.get_active_text()
        
        mb = gtk.MenuBar()
        
        filemenu = gtk.Menu()
        filemenu.show()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)
        filem.show()
        exit = gtk.MenuItem("Exit")
        exit.show()
        filemenu.append(exit)
        
        testmenu = gtk.Menu()
        testmenu.show()
        testm = gtk.MenuItem("test")
        testm.set_submenu(testmenu)
        testm.show()
        
        mb.append(filem)
        mb.append(testm)
        layout.add(mb)

    
    def set_drop(self, layout):
        drop_size = (window_width/3*2, window_height/(rows+1)/2)
        self.drop.set_size_request(drop_size[0], drop_size[1])
        self.drop.set_title('Serial Ports')
        ports = serial_ports()
        for i in ports:
            self.drop.append_text(i)
        drop_coords = (0, window_height/(rows+1)*rows)
        layout.put(self.drop, drop_coords[0], drop_coords[1])
        self.drop.show()
    
    def get_text(self, widget, data = None):
        print data
    
    def text(self):
        while True:
            print self.drop.get_active_text()
    
    def main(self):
        gtk.main()
        
if __name__ == '__main__':
    gtk.threads_init()
    main_window = Base()
    t1 = threading.Thread(target = main_window.text)
    #t1.start()
    main_window.main()
