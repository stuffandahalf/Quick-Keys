from gi.repository import Gtk as gtk
#import pygtk
#import gtk
#import os

window = gtk.Window()
icon = gtk.StatusIcon()
icon.set_from_file('icon.png')
window.show_all()
print icon.is_embedded()
gtk.main()
