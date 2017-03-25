#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Source: profile.py

import serial
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from variables import *

class Profile(object):
    def __init__(self, name, symbols, port):
        self.name = name
        self.port = port
        self.symbols = {}
        for i in symbols:
            self.symbols[i] = symbols[i]
        
    def load(self):
        try:
            ser = serial.Serial(self.port)
        except:
            ser = serial.Serial(None)
        for i in self.symbols:
            symbols[i] == self.symbols[i]
            
    def get_menu_item(self):
        #def load_profile_bind(widget):
        #    self.load()
        #    Editor_Window.update_symbols()
        menu_item = gtk.MenuItem(self.name)
        #menu_item.connect('activate', load_profile_bind)
        menu_item.show()
        return menu_item

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
