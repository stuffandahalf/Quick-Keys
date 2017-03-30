#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Sources: Quick-Keys.py

import serial
import platform
from pykeyboard import PyKeyboard

ser = serial.Serial('/dev/ttyUSB0')
k = PyKeyboard()

symbols = {'1' : u'π',            #6 button version
           '2' : u'Σ',
           '3' : u'α',
           '4' : u'β',
           '5' : u'Δ',
           '6' : u'Ω'}

def main_script():
    while ser.port != None:                                             # while the selected serial port is valid
        try:                                                            # try
            ind = ser.readline().rstrip('\r\n')                         # read the index from the serial port
            hexval = symbols[ind].encode("unicode_escape")              # encode the index
            #hexval = repr(symbols[ind])
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

main_script()
