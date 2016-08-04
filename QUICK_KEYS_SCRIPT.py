# -*- coding: utf-8 -*-

from __future__ import division
import serial																		#importing main program modules
import platform
import time
from pykeyboard import PyKeyboard
import clipboard
import threading
import subprocess
import sys
import glob

import kivy																			# importing kivy modules
kivy.require('1.9.1')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

k = PyKeyboard()																	#creates an instance of pykeyboard
																					#dictonary of symbols

symbols = {'1' : 'π',
		   '2' : 'Σ',
		   '3' : 'α',
		   '4' : 'β',
		   '5' : 'Δ',
		   '6' : 'Ω'}

rows = 2
cols = 3
winheight = 200
winwidth = 200

widspacey = 1/(rows+1)
widspacex = 1/cols
		   
btn = []																			#create a list for button variables
for i in range(len(symbols)):														#and fill it with blank spaces
	btn.append('')
	
widspaces = []																		#create list for pos_hints
for y in range(rows, 0, -1):														#and fill it realtive to
	for x in range(cols):															#amount of buttons
		widspaces.append({'x' : widspacex*x, 'y' : widspacey*y})
#print widspaces[5]

ser = serial.Serial('/dev/ttyACM0')													#the port the arduino is connected to
serports = []
	
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

def callback(instance):
    print('The button <%s> is being pressed' % instance.text)
	
def symprint(instance):
	print instance.text
	ind = '%s' % instance.text
	print symbols[ind]

def addbutton(text, size_hint, pos_hint, bind, parent):
	button = Button(text = text, size_hint = size_hint, pos_hint = pos_hint)
	button.bind(on_press = bind)
	parent.add_widget(button)
	return button

class MainWindow(App):
	def build(self):
		Window.size = (winheight, winwidth)
		parent = FloatLayout()
		parent.size = Window.size
		for i in range(len(symbols)):
			#btn[i] = Button(text = symbols[str(i+1)], size_hint = (widspacex, widspacey), pos_hint = widspaces[i])
			#btn[i].bind(on_press = callback)
			#parent.add_widget(btn[i])
			btn[i] = addbutton(symbols[str(i+1)], (widspacex, widspacey), widspaces[i], callback, parent)
		
		serports = serial_ports()
		print len(serports)
		port = DropDown()
		for i in range(len(serports)):
			dropbtn = Button(text = serports[i], size_hint_y = None, height = 44)
			dropbtn.bind(on_release = lambda dropbtn: port.select(dropbtn.text))
			port.add_widget(dropbtn)
		portbtn = Button(text = 'port', size_hint = (2/3, widspacey), pos_hint = {'x' : 0, 'y' : 0})
		portbtn.bind(on_release = port.open)
		port.bind(on_select=lambda instance, x: setattr(portbtn, 'text', x))
		parent.add_widget(portbtn)
		#port = addbutton('port', (2/3, widspacey), {'x' : 0, 'y' : 0}, callback, parent)
		#port = Button(text = 'port', size_hint = (2/3, widspacey), pos_hint = {'x' : 0, 'y' : 0})
		#port.bind(on_press = callback)
		#parent.add_widget(port)
		applybtn = addbutton('apply', (1/3, widspacey), {'x' : 2/3, 'y' : 0}, callback, parent)
		#applybtn = Button(text = 'apply', size_hint = (1/3, widspacey), pos_hint = {'x' : 2/3, 'y' : 0})
		#applybtn.bind(on_press = callback)
		#parent.add_widget(applybtn)
		return parent

def symbolDecoder():
	while True:																			#main loop
		while ser.readline().decode('utf-8')[:2]:										#when there is a relevant serial value
			try:																		#try to run the main script
				ind = ser.read()
				board = clipboard.paste()												#store the clipboard contents in the variable
				clipboard.copy(symbols[ind])
				if platform.system() == 'Linux' or platform.system() == 'Windows' :		#for windows and linux
					k.press_key('Control_L')											#paste the clipboard
					k.tap_key('v')
					k.release_key('Control_L')
					#k.tap_key('Return')
				elif platform.system() == 'Darwin':
					pass
				time.sleep(.1)															#pause for .1 seconds
				clipboard.copy(board)													#restore the clipboard contents
							
			except:																		#if there is an error
				pass																	#do not do anything



if __name__ == '__main__':
	print serports
	t = threading.Thread(target = symbolDecoder)
	t.start()
	MainWindow().run()
