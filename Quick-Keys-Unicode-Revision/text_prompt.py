#!/usr/bin/env python
# -*- coding: utf-8 -*-
#source from https://ardoris.wordpress.com/2008/07/05/pygtk-text-entry-dialog/
#modified by Gregory Norton

import gtk
def responseToDialog(entry, dialog, response):
    dialog.response(response)
    
def getText(symbol):
    #base this on a message dialog
    dialog = gtk.MessageDialog(
        None,
        gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
        gtk.MESSAGE_QUESTION,
        gtk.BUTTONS_OK,
        None)
    dialog.set_markup('Please enter the new symbol:')
    #create the text input field
    entry = gtk.Entry(max=5)
    entry.set_text(symbol)
    #allow the user to press enter to do ok
    entry.connect("activate", responseToDialog, dialog, gtk.RESPONSE_OK)
    #create a horizontal box to pack the entry and a label
    hbox = gtk.HBox()
    hbox.pack_start(gtk.Label("Symbol:"), False, 5, 5)
    hbox.pack_end(entry)
    #some secondary text
    dialog.format_secondary_markup("This will overwrite the previous symbol")
    #add it and show it
    dialog.vbox.pack_end(hbox, True, True, 0)
    dialog.show_all()
    #go go go
    dialog.run()
    text = entry.get_text()
    dialog.destroy()
    return text
    
#if __name__ == '__main__':
#    print "The name was %s" % getText()
#    gtk.main()
