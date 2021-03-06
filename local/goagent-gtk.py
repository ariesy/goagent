#!/usr/bin/env python
# coding:utf-8
# Contributor:
#      Phus Lu        <phus.lu@gmail.com>

__version__ = '1.0'

import sys
import os
import re
import time

import pygtk
pygtk.require('2.0')
import gtk
import appindicator

try:
    import vte
except ImportError:
    sys.exit(gtk.MessageDialog (None, gtk.DIALOG_MODAL, gtk.MESSAGE_ERROR, gtk.BUTTONS_OK, u'\u8bf7\u5b89\u88c5 python-vte').run())

class GoAgentAppIndicator:

    def __init__(self, window):
        self.window = window

        self.ind = appindicator.Indicator("GoAgent", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("indicator-messages-new")
        self.ind.set_icon(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logo.png'))

        self.menu = gtk.Menu()

        item = gtk.MenuItem(u'\u663e\u793a')
        item.connect("activate", self.show)
        item.show()
        self.menu.append(item)

        item = gtk.MenuItem(u'\u9690\u85cf')
        item.connect("activate", self.hide)
        item.show()
        self.menu.append(item)

        item = gtk.MenuItem(u'\u9000\u51fa')
        item.connect("activate", self.quit)
        item.show()
        self.menu.append(item)

        self.menu.show()

        self.ind.set_menu(self.menu)

    def show(self, widget, data=None):
        self.window.show_all()
        self.window.present()

    def hide(self, widget, data=None):
        self.window.hide_all()

    def quit(self, widget, data=None):
        gtk.main_quit()


def main():
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    os.system('chmod +x proxy.py')
    v = vte.Terminal ()
    v.connect ("child-exited", lambda term: gtk.main_quit())
    v.fork_command('./proxy.py')
    window = gtk.Window()
    window.add(v)
    window.connect('delete-event', lambda window, event: gtk.main_quit())
    window.show_all()
    indicator = GoAgentAppIndicator(window)
    gtk.main()

if __name__ == "__main__":
    main()
