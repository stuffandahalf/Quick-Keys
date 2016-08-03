# -*- coding: utf-8 -*-

import serial																		#importing main program modules
import platform
import time
from pykeyboard import PyKeyboard
import clipboard



import kivy																			# importing kivy modules
kivy.require('1.9.1')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

k = PyKeyboard()																	#creates an instance of pykeyboard
																					#dictonary of symbols
symbols = {'1' : 'π',
		   '2' : 'Σ',
		   '3' : ':^)',
		   '4' : 'sure kid',
		   '5' : 'me too thanks',
		   '6' : 'FeelsBindMan'}

rows = 2
cols = 3
		   
btn = []

for i in range(len(symbols)):
	btn.append('')

ser = serial.Serial('/dev/ttyACM0')													#the port the arduino is connected to
	
def callback(instance):
    print('The button <%s> is being pressed' % instance.text)
	
def symprint(instance):
	print instance.text
	ind = '%s' % instance.text
	print symbols[ind]

class MyApp(App):
	def build(self):
		Window.size = (300, 300)
		parent = GridLayout(cols = 3, rows = 2)
		parent.size = Window.size
		for i in range(len(symbols)):
			btn[i] = Button(text = symbols[str(i+1)], pos_hint = {'x' : 0, 'y' : 0})
			#btn[i] = Button(text = str(i), 
			btn[i].bind(on_press = callback)
			parent.add_widget(btn[i])
		#btn = Button(text = 'Hello World', pos_hint = {'center_x' : .5, 'center_y' : .5})
		#btn.bind(on_press = callback)
		#parent.add_widget(btn)
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
	MyApp().run()
	symbolDecoder()
