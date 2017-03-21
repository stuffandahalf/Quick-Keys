#!/usr/bin/env python
# -*- coding: utf-8 -*-
#source from https://ardoris.wordpress.com/2008/07/05/pygtk-text-entry-dialog/
#modified and ported to gtk 3.0 by Gregory Norton

#import gtk
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk

def responseToDialog(entry, dialog, response):
    dialog.response(response)
    
def getText(symbol):
    """
    creates a dialog box where a user enters a string
    and returns that string
    """
    dialog = gtk.MessageDialog()
    dialog.set_markup('Please enter the new symbol:')
    entry = gtk.Entry()
    entry.set_max_length(5)
    entry.connect("activate", responseToDialog, dialog, gtk.ResponseType.OK)
    hbox = gtk.HBox()
    hbox.pack_start(gtk.Label("Symbol:"), False, 5, 5)
    hbox.pack_end(entry, False, 5, 5)
    #dialog.format_secondary_markup('This will overwrite the previous symbol')
    dialog.vbox.pack_end(hbox, True, True, 0)
    dialog.show_all()
    dialog.run()
    text = entry.get_text()
    dialog.destroy()
    return text
    
#if __name__ == '__main__':
#    print "The name was %s" % getText('test')
#    gtk.main()
