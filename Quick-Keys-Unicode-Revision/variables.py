#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


from pykeyboard import PyKeyboard
import serial
import os

k = PyKeyboard()
ser = serial.Serial(None)

window_height = 300
window_width = 300

symbols = {'1' : u'π',            #6 button version
           '2' : u'Σ',
           '3' : u'α',
           '4' : u'β',
           '5' : u'Δ',
           '6' : u'Ω'}
           
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

rows = 2         #6 button version
columns = 3

#rows = 3        #12 button version
#columns = 4

current_profile = 0

pref_file = os.path.abspath('Quick-Keys Preferences')
icon_file = os.path.abspath('icon.png')
