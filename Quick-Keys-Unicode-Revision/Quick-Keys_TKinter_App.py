#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Source: Quick-Keys_TKinter_App.py

#importing main program modules
import threading
import serial
import platform
import time
import os.path
from pykeyboard import PyKeyboard

from text_prompt import getText
from serial_scanner import serial_ports

#importing gui components


k = PyKeyboard()
ser = serial.Serial(None)

window_height = 300
window_width = 300

rows = 2         #6 button version
columns = 3

#rows = 3        #12 button version
#columns = 4

pref_file = 'Quick-Keys Preferences'
profile_file = 'Quick-Keys Profiles'

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
           
profiles = [pref_file]

new_symbols = {}
for i in symbols:
    new_symbols[i] = symbols[i]
    
def main_script():
    while ser.port != None:                                             # while the selected serial port is valid
        try:                                                            # try
            ind = ser.readline().rstrip('\r\n')                         # read the index from the serial port
            hexval = symbols[ind].encode("unicode_escape")              # encode the index
            print hexval
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

def save_profiles():
    f = open(profile_file, 'w+')
    f.write(pref_file + '\n')
    for i in profiles:
        f.write(i + '\n')
    f.close()
    
def read_profiles():
    f = open(profile_file)
    pref_file = f.readline().rstrip('\r\n')
    for line in f:
        profiles.append(line.rstrip('\r\n'))
    f.close()
    
def save_preferences():
    f = open(pref_file, 'w+')                                           # open the preference file
    for i in symbols:                                                   # for every symbol
        f.write(symbols[i] + '\n')                                      # write them to the file
    if ser.port != None:                                                # if the current serial port is valid
        f.write(ser.port + '\n')                                        # write it to the file
    else:                                                               # otherwise
        f.write('\n')                                                   # write a newline character
    f.close()
    
def read_preferences():
    global ser                                                          # define the ser variable as global
    f = open(pref_file)                                                 # open the preference file
    for i in symbols:                                                   # for every symbol
        sym = f.readline().rstrip('\r\n')                               # read the symbol from the file
        symbols[i] = sym                                                # assign the symbol to the dictionary of symbols
        new_symbols[i] = sym                                            # and the new one
        print sym
        
    new_port = f.readline().rstrip('\r\n')                              # read the new port from the file
    print new_port
    if new_port != '' and new_port in serial_ports():                   # if the new port is a valid port
        ser = serial.Serial(new_port)                                   # set the serial port to it
        print_serial_change()                                           # print the changes
    else:                                                               # otherwise
        print 'Error setting serial port. Try again later.'             # print a warning
        ser = serial.Serial(None)                                       # change the port to None
    f.close()

def print_serial_change():
    print 'Serial port has been set to ' + ser.port
    
def print_symbol_changes():
    print 'Symbols have been changed to: '
    for i in symbols:
        print symbols[i]

