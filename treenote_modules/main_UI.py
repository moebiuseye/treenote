#!/usr/bin/python
# -*- coding: UTF-8 -*-

def void(button):
	return None

import gtk

def set_buttons(self):
	print "set_button"
	#set the add button

	self.Add_button.connect("clicked", self.Add_tab)
	addimg=gtk.Image()
	addimg.set_from_stock('gtk-add', gtk.ICON_SIZE_MENU)
	self.Add_button.set_image(addimg)
	#set the close button

	self.Close_button.connect("clicked", self.Close_tab)
	closeimg=gtk.Image()
	closeimg.set_from_stock('gtk-close', gtk.ICON_SIZE_MENU)
	self.Close_button.set_image(closeimg)


	if ( self.debug ):
		self.debug_button.connect("clicked", self.debuger)
		debugimg=gtk.Image()
		debugimg.set_from_stock(gtk.STOCK_REFRESH, gtk.ICON_SIZE_MENU)
		self.debug_button.set_image(debugimg)

def set_notebook(self):
	print "set_notebook"

	self.notebook.connect("switch-page",self.Tab_change)
	self.notebook.set_tab_pos(gtk.POS_TOP)
	self.notebook.set_scrollable(True)
	self.notebook.popup_enable()

def set_boxes(self):
	print "set_boxes"

	self.hbox.pack_start(self.Add_button, False)
	self.hbox.pack_start(gtk.Label())
	if ( self.debug ):
		self.hbox.pack_start(self.debug_button, False)
	self.hbox.pack_start(self.Close_button, False)


def set_menubar(self):
	print "set_menubar" # Ajouter des fonctionnalités
	self.mb = gtk.MenuBar()
	filemenu = gtk.Menu()
	filem = gtk.MenuItem("File")
	filem.set_submenu(filemenu)

	conf = gtk.MenuItem("Preferences")
	conf.connect("activate", self.conf_open)
	filemenu.append(conf)

	exit = gtk.MenuItem("Exit")
	exit.connect("activate", gtk.main_quit)
	filemenu.append(exit)
	self.mb.append(filem)

def set_main_vbox(self):
	self.main_vbox.pack_start(self.mb, False, False, 0)
	self.main_vbox.pack_start(self.hbox, False)
	self.main_vbox.pack_start(self.notebook)


def set_window(self):
	print "set_window"
	self.win.set_title("TreeNote")
	try:
		self.win.set_icon_from_file("/usr/share/pixmaps/treenote.png")
	except:
		print "File not found."
		pass
	self.win.connect("destroy", self.destroy)
	self.win.set_default_size(500, 500)
	self.win.add(self.main_vbox)
	self.win.show_all()
	self.win.isshown = True


def set_dropdown(self):
	self.dropdown.append(gtk.combo_box_new_text())
	self.dropdown[self.i].append_text("copy")
	self.dropdown[self.i].append_text("execute")
	self.dropdown[self.i].set_active(0)

def set_tray_icon(self):
	self.tray = gtk.StatusIcon()
	try:
		self.tray.set_from_file("/usr/share/pixmaps/treenote.png")
	except:
		print "file not found.\n"
		pass
	self.tray.connect('popup-menu', self.tray_popup)
	self.tray.connect('activate', self.tray_activate)
	self.tray.set_visible(True)
	self.quitbutton = gtk.MenuItem("Quit")
	self.quitbutton.connect("activate", self.destroy)
	self.popupmenu = gtk.Menu()
	self.popupmenu.append(self.quitbutton)
	self.popupmenu.show_all()
	self.set_conf_window()
	self.cmd = "xterm -hold -T "

def set_conf_window(self):
	print "set_conf_window"
	self.conf_win=gtk.Window()
	self.conf_win.set_title("Panneau de Configuration de TreeNote")
	self.conf_notebook=gtk.Notebook()
	self.conf_notebook.set_tab_pos(gtk.POS_LEFT)
	self.terminal_entry=gtk.Entry()
	self.conf_notebook.append_page(self.terminal_entry, gtk.Label("Terminal"))
	self.conf_win.connect("destroy", self.conf_open)
	self.conf_win.set_default_size(300, 250)
	self.conf_win.add(self.conf_notebook)
	self.conf_win.isshown=False
