import QUICK_KEYS_SCRIPT.py

import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

#class MainWindow(GridLayout):
#	def __init__(self, **kwargs):
#		super(LoginScreen, self).__init__(**kwargs)
#		self.cols = 2
		
def callback(instance):
    print('The button <%s> is being pressed' % instance.text)



class MyApp(App):
	def build(self):
		parent = Widget()
		for i in range(len(symbols)-1):
			btn[i] = Button(text = i)
			btn[i].bind(on_press = callback)
			parent.add_widget(btn[i])
		#btn = Button(text = 'Hello World')
		#btn.bind(on_press = callback)
		#parent.add_widget(btn)
		return parent
		
if __name__ == '__main__':
	MyApp().run()
