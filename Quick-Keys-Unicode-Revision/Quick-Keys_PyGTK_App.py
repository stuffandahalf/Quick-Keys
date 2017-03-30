#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Source: Quick-Keys_PyGTK_App.py

#importing main program modules
import threading
import serial
import platform
#import time
import os.path
import io
from pykeyboard import PyKeyboard

from text_prompt import getText
from serial_scanner import serial_ports
from profile import Profile
from variables import *

#importing gui components
#import pygtk
#pygtk.require('2.0')
#import gtk

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
if platform.system() == 'Linux':
    gi.require_version('AppIndicator3', '0.1')
    from gi.repository import AppIndicator3 as appindicator
elif platform.system() == 'Darwin':
    import rumps


test_symbols = {'1' : 'a',            #6 button version
                '2' : 'b',
                '3' : 'c',
                '4' : 'd',
                '5' : 'e',
                '6' : 'f'}

profiles = [Profile('Default', symbols, ser.port),
            Profile('test', test_symbols, ser.port)]

#a dictionary to store the changed symbols
new_symbols = {}
for i in symbols:
    new_symbols[i] = symbols[i]

def main_script():
    while ser.port != None:                                             # while the selected serial port is valid
        try:                                                            # try
            ind = ser.readline().rstrip('\r\n')                         # read the index from the serial port
            hexval = symbols[ind].encode("unicode_escape")              # encode the index
            if hexval[:2] == '\u':                                      # if the value is a hex number
                if platform.system() == 'Linux':                        # for linux platforms
                    k.press_key('Control_L')                            # press the control
                    k.press_key('Shift_L')                              # the left shift
                    k.tap_key('u')                                      # and the u key
                    k.release_key('Control_L')                          # release the control
                    k.release_key('Shift_L')                            # and shift keys
                    hexval = hexval[2:]                                 # remove the unicode escape character
                    k.type_string(hexval)                               # type the unicode string
                    k.tap_key('Return')                                 # tap the return key
                    
                elif platform.system() == 'Windows':                    # for windows platforms
                    pass
                    
                elif platform.system() == 'Darwin':                     # for darwin platforms
                    pass
                
                else:                                                   # for all other platforms
                    print 'Unsupported platform'                        # print unsupported platform
                    
            else:                                                       # if the given string isnt a unicode character
                k.type_string(hexval)                                   # just type the string
        except:                                                         # except
            ser.close()                                                 # close the serial port
            ser.port = None                                             # set the port to None

def load_profile(profile, profile_index):
    global current_profile
    global new_symbols
    global ser
    current_profile = profile_index
    for i in new_symbols:
        new_symbols[i] = profile.symbols[i]
        symbols[i] = profile.symbols[i]
    try:
        ser.port = profile.port
        ser.open()
    except:
        ser.port == None
    save_preferences()

def save_preferences():
    global current_profile
    f = open(pref_file, 'w+')                                           # open the file for writing/creating
    f.write(str(len(profiles)) + '\n')                                  # write the number of profiles to the file
    f.write(str(current_profile) + '\n\n')
    for i in range(len(profiles)):                                      # for every profile
        f.write(profiles[i].name + '\n')                                # write the name + newline
        f.write(str(profiles[i].port) + '\n')                           # write the serial port
        for j in profiles[i].symbols:                                   # write every symbol
            f.write(str(profiles[i].symbols[j].encode("unicode_escape")) + '\n')
        f.write('\n\n')                                                 # write two newlines
    f.close()                                                           # close the file

def read_preferences():
    global current_profile
    profiles = []                                                       # clear the list of profiles
    f = open(pref_file, 'r')
    num = int(f.readline().rstrip('\r\n'))
    current_profile = int(f.readline().rstrip('\r\n'))
    f.readline()
    for i in range(num):
        profile_name = f.readline().rstrip('\r\n')
        print profile_name
        profile_port = f.readline().rstrip('\r\n')
        print profile_port
        profile_symbols = {}
        for j in symbols:
            profile_symbols[j] = f.readline().rstrip('\r\n').decode("unicode-escape")
        print profile_symbols
        new_profile = Profile(profile_name, profile_symbols, profile_port)
        profiles.append(new_profile)
        f.readline()
        f.readline()
        print ''
    load_profile(profiles[current_profile], current_profile)
    #print symbols
    f.close()

def print_serial_change():
    print 'Serial port has been set to ' + ser.port
    
def print_symbol_changes():
    print 'Symbols have been changed to: '
    for i in symbols:
        print symbols[i]
        
class Tray_Indicator(object):
    def __init__(self):
        self.icon_menu = None
        
    def open_window(self, data):
        global opened
        if opened == False:
            opened = not opened
            window = Editor_Window()
            
    def quit_app(self, data):
        exit()
        #gtk.main_quit()
        
    def make_icon_menu(self):
        icon_menu = gtk.Menu()
        
        open_item = gtk.MenuItem('Open Editor')
        open_item.connect_object('activate', self.open_window, None)
        icon_menu.append(open_item)
        
        quit_item = gtk.MenuItem('Quit')
        quit_item.connect_object('activate', self.quit_app, None)
        icon_menu.append(quit_item)
        
        icon_menu.show_all()
        return icon_menu

class Linux_Tray_Indicator(Tray_Indicator):
    def __init__(self):
        self.APPINDICATOR_ID = 'Quick-Keys'
        super(Linux_Tray_Indicator)
        self.status_icon = appindicator.Indicator.new(self.APPINDICATOR_ID,
                                                      icon_file,
                                                      appindicator.IndicatorCategory.SYSTEM_SERVICES)
        self.status_icon.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.right_click_menu()
        
    def right_click_menu(self):
        self.icon_menu = self.make_icon_menu()
        self.status_icon.set_menu(self.icon_menu)

class Windows_Tray_Indicator(Tray_Indicator):
    def __init__(self):
        super(Windows_Tray_Indicator)
        self.status_icon = gtk.StatusIcon()
        self.status_icon.set_from_file(icon_file)
        self.status_icon.set_has_tooltip(True)
        self.status_icon.set_tooltip_text('Quick-Keys')
        self.status_icon.connect('popup-menu', self.right_click_menu)
    
    def right_click_menu(self, icon, button, activate_time):
        self.icon_menu = self.make_icon_menu()
        self.icon_menu.popup(None, None, None, self.status_icon, button, activate_time)

if platform.system() == 'Darwin':
    class Mac_Tray_Indicator(rumps.App):
        def __init__(self):
            super(Mac_Tray_Indicator, self).__init__('Quick-Keys', icon_file)
            self.menu = ['Open Editor', 'Quit App']
            
        @rumps.clicked('Open Editor')
        def open_editor(self, _):
            global opened
            if opened == False:
                opened = not opened
                window = Editor_Window()
            
        @rumps.clicked('Quit_App')
        def quit_app(self, _):
            exit()
    
#class Mac_Tray_Indicator(Windows_Tray_Indicator):
#    def __init__(self):
#        super(Mac_Tray_Indicator)

class Editor_Window:
    def __init__(self):                                                 # constructor for the Editor_Window class
        self.window = gtk.Window()                                      # make a new window object
        self.window.set_default_size(window_width, window_height)       # set the default and
        self.window.set_size_request(window_width, window_height)       # minimum size of the window
        self.window.show()                                              # show the window
        self.window.set_title('Quick-Keys')                             # set the title of the window
        if not platform.system() == 'Darwin':
            self.window.set_icon_from_file(icon_file)                       # set the icon for the window
        
        layout = gtk.Layout()                                           # create a new gtk layout object
        self.window.add(layout)                                         # add the layout to the window
        layout.show()                                                   # show the layout
        
        self.add_primary_buttons(layout)                                # add the main symbol buttons
        self.add_serial_port_dropdown(layout)                           # add the serial port dropdown
        self.add_apply_button(layout)                                   # add the apply button
        self.add_refresh_load_buttons(layout)                           # add the refresh and load buttons
        self.add_menu_bar(layout)
        
        self.window.connect('delete-event', self.close_window)
    
    def add_primary_buttons(self, layout):
        button_size = (window_width/columns, window_height/(rows+1))        # calculate the size of the buttons
        button_coords = []                                                  # a list of coordinates for the buttons
        for y in range(rows):                                               # for every row
            for x in range(columns):                                        # for every column
                button_coords.append((button_size[0]*x, button_size[1]*y))  # add the coordinates of that button to the list
        
        self.button = []                                                    # list of buttons
        for i in range(len(symbols)):                                       # for every symbol
            self.button.append(gtk.Button(label = symbols[str(i+1)]))       # make a new button object
            self.button[i].set_size_request(button_size[0], button_size[1])     # set the size of the button
            self.button[i].connect('clicked', self.change_button_symbols, i)            # bind the button to the test function
            layout.put(self.button[i], button_coords[i][0], button_coords[i][1])    # place the button on the layout
            self.button[i].show()                                           # show the button

    def add_serial_port_dropdown(self, layout):
        #self.drop = gtk.combo_box_new_text()                            # create a new combo box object
        self.drop = gtk.ComboBoxText()
        drop_size = (window_width/3*2, window_height/(rows+1)/2)        # the size of the drop down box
        self.drop.set_size_request(drop_size[0], drop_size[1])          # set the size of the drop down
        #self.drop.set_title('Serial Ports')                             # set the title (wip)
        self.ports = serial_ports()                                     # create a list of available ports
        #print self.ports
        #try:
            #self.drop.set_active(self.ports.index(ser.port))
        #except:
            #pass
        for i in self.ports:                                            # for every port
            self.drop.append_text(i)                                    # add it to the dropdown
        if ser.port in self.ports:
            self.drop.set_active(self.ports.index(ser.port))
        drop_coords = (0, window_height/(rows+1)*rows)                  # the coordinates of the drop
        layout.put(self.drop, drop_coords[0], drop_coords[1])           # place it on the layout
        self.drop.show()                                                # show the drop
    
    def refresh_serial_dropdown(self, widget, data = None):
        for i in range(len(self.ports)):                                # for every port in the current list
            self.drop.remove(0)                                    # remove the values from the dropdown
        self.ports = serial_ports()                                     # refresh the list of ports
        for i in self.ports:                                            # for every new port
            self.drop.append_text(i)                                    # add it to the dropdown
        if ser.port in self.ports:
            self.drop.set_active(self.ports.index(ser.port))
        self.clear_symbol_changes()                                     # clear any symbol changes that might've been made
        #print self.ports
        
    def change_button_symbols(self, widget, data = None):
        data += 1                                                       # increment the index data by 1
        new_symbols[str(data)] = getText(symbols[str(data)])            # set the new symbol to the value retrieved from the popup
        #print data
        #self.drop.append_text('test')
        #self.ports.append('test')
        #print self.ports
        self.update_symbols()                                          # update the symbol button labels
        #print self.drop.get_row_span_column()  
    
    def update_symbols(self):
        #for i in range(len(new_symbols)):                               # for every button
        #    self.button[i].set_label(new_symbols[str(i+1)])             # set the label of the button to the new symbol
        for i in new_symbols:
            self.button[int(i)-1].set_label(new_symbols[i])
        
    def clear_symbol_changes(self):
        for i in range(len(new_symbols)):                               # for every symbol/button
            self.button[i].set_label(symbols[str(i+1)])                 # set the button label to the old symbol
    
    def add_apply_button(self, layout):
        button_size = (window_width/3, window_height/(rows+1))                  # tuple holding the size of the button
        button = gtk.Button(label = 'apply')                                    # creating another button object
        button.set_size_request(button_size[0], button_size[1])                 # set the size of the button
        button_coord = (window_width-button_size[0], button_size[1]*(rows))     # tuple holding the location of the button
        button.connect('clicked', self.apply_changes, self.get_drop_text())     # bind the button to apply_changes()
        layout.put(button, button_coord[0], button_coord[1])                    # place the button on the layout
        button.show()                                                           # show the button
    
    def add_refresh_load_buttons(self, layout):
        button_size = (window_width/3, window_height/(rows+1)/2)            # tuple to store dimension of buttons
        refresh = gtk.Button(label = 'refresh')                             # create button object
        refresh.set_size_request(button_size[0], button_size[1])            # set the size of the button to the tuple
        button_coord = (0, button_size[1]*(rows*2+1))                       # tuple containing the top left coordinates of the button
        refresh.connect('clicked', self.refresh_serial_dropdown, '')        # bind the button to redraw the serial drop down
        layout.put(refresh, button_coord[0], window_height-button_size[1])  # place the button on the layout
        refresh.show()                                                      # show the button
        
        load = gtk.Button(label = 'load')                               # create another button object with label load
        load.set_size_request(button_size[0], button_size[1])           # set the size to the size tuple
        button_coord = (window_width/3, window_height-button_size[1])   # tupe containing the coordinates of the top left corner
        load.connect('clicked', self.read_preferences_bind, '')         # bind the button to read_preferences()
        layout.put(load, button_coord[0], button_coord[1])              # place the load button on the layout
        load.show()                                                     # show the button
     
    def add_menu_bar(self, layout):
        menu_bar = gtk.MenuBar()
        
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)
        filem.show()
        
        profilemenu = gtk.Menu()
        profilem = gtk.MenuItem("Profiles")
        profilem.set_submenu(profilemenu)
        
        def load_profile_bind(widget, i):
            load_profile(profiles[i], i)
            self.update_symbols()
            self.apply_changes(None)
            
        for i in range(len(profiles)):
            menu_item = profiles[i].get_menu_item()
            menu_item.connect("activate", load_profile_bind, i)
            profilemenu.append(menu_item)
        
        filem.show()
        profilem.show()
        
        menu_bar.append(filem)
        menu_bar.append(profilem)
        
        layout.add(menu_bar)
    
    def get_drop_text(self):
        return self.drop.get_active_text()
           
    def read_preferences_bind(self, widget, data = None):
        read_preferences()                                              # a method to bind read_preferences() to a widget
        self.update_symbols()                                           # a update the button labels
    
    def apply_changes(self, widget, data = None):
        print 'function to apply changes'
        new_port = self.get_drop_text()                                 # get new serial port from drop down
        #print new_port
        if new_port != None and new_port in serial_ports():             # if port is valid
            ser.close()                                                 # close the current one
            ser.port = None                                             # set serial port to None to close current thread
            ser.port = new_port                                         # set the serial port to the new port
            ser.open()                                                  # reopen the serial port
            threading.Thread(target = main_script).start()              # start a new script thread
            profiles[current_profile].port = new_port
            print_serial_change()                                       # print the changes made
        else:
            print 'invalid Serial port selected, port not changed'      # if invalid port selected, print message and proceed
        print ser.port    
        for i in new_symbols:                                           # for every symbol
            symbols[i] = new_symbols[i]                                 # update the value
        self.update_symbols()
        print_symbol_changes()                                          # print the changes
        save_preferences()                                              # write the changes to the preferences file
    
    def close_window(self, widget, e):
        global opened
        self.window.destroy
        opened = not opened

def main(args):
    #gtk.threads_init()                                                  # initialize threads in gtk
    t1 = threading.Thread(target = main_script)                         # create a new thread for the main script
    
    #check if preferences file exists
    if os.path.isfile(pref_file):                                       # if the preferences file exists
        read_preferences()                                              # read the symbols and port from it
        print 'Preference file read'
        
    else:                                                               # if it doesnt
        save_preferences()                                              # create it using default values
        print 'Preference file saved'
    
    if ser.port in serial_ports():                                      # if the serial port read from the file is valid
        t1.start()                                                      # start the script thread
    else:
        print 'Please set port to launch script'                        # otherwise warn the user
    
    if platform.system() == 'Linux':
        tray_icon = Linux_Tray_Indicator()
    elif platform.system() == 'Windows':
        tray_icon = Windows_Tray_Indicator()
    elif platform.system() == 'Darwin':
        tray_icon = Mac_Tray_Indicator()

    #main_window = Editor_Window()                                       # create a window object
    Editor_Window()
    gtk.main()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
