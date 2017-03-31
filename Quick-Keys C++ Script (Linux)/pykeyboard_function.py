# -*- coding: utf-8 -*-

from pykeyboard import PyKeyboard

def type_unicode(symbol):
    k = PyKeyboard()
    hexval = symbol.encode("unicode_escape")
    print hexval
    if hexval[:2] == '\u':                                  # if the value is a hex number
        k.press_key('Control_L')                            # press the control
        k.press_key('Shift_L')                              # the left shift
        k.tap_key('u')                                      # and the u key
        k.release_key('Control_L')                          # release the control
        k.release_key('Shift_L')                            # and shift keys
        hexval = hexval[2:]                                 # remove the unicode escape character
        k.type_string(hexval)                               # type the unicode string
        k.tap_key('Return')                                 # tap the return key
            
    else:                                                   # if the given string isnt a unicode character
        k.type_string(hexval)                               # just type the string

