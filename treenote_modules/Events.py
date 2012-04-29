#!/usr/bin/python
# -*- coding: UTF-8 -*-

# DONE : Add an icon to the gtk.Menu (TrayIcon) if function is set to "copy" or "execute".
# Implications: Set an event to self.dropdown and modify a self.set_trayicon

def void(button):
	return None


import gtk
import os

def Add_tab(self, widget):
	print "Add_tab"
	self.i+=1
	self.noteLabel.append(gtk.Label("Tab "+str(self.i)))
	self.vbox.append(gtk.VBox())
	self.inner_hbox.append(gtk.HBox())
	self.entry.append(gtk.Entry())
	self.entry[self.i].connect("changed", self.changed)
	self.set_dropdown()
	self.textview.append(gtk.TextView()) 
	self.scroll.append(gtk.ScrolledWindow())
	self.scroll[self.i].add(self.textview[self.i])
	""" IMPORTANT:
	/usr/lib/python2.7/site-packages/treenote_modules/Events.py:23: GtkWarning: IA__gtk_range_get_adjustment: assertion `GTK_IS_RANGE (range)' failed """
	self.scroll[self.i].add(self.textview[self.i])

	self.inner_hbox[self.i].pack_start(self.entry[self.i])
	self.inner_hbox[self.i].pack_start(self.dropdown[self.i])
	self.vbox[self.i].pack_start(self.inner_hbox[self.i], False)
	self.vbox[self.i].pack_start(self.scroll[self.i])
	self.notebook.append_page(self.vbox[self.i],self.noteLabel[self.i])
	self.popupbutton.append(gtk.MenuItem("Tab "+str(self.i)))
	self.popupbutton[self.i].connect("activate", self.popup_action)
	self.popupmenu.append(self.popupbutton[self.i])
	self.popupmenu.show_all()
	self.win.show_all()

def Close_tab(self, widget):
	print "Close_tab"
	self.curr=self.notebook.get_current_page()
	if self.curr != -1:
		self.i-=1
		self.noteLabel.pop(self.curr)
		self.entry.pop(self.curr)
		self.dropdown.pop(self.curr)
		self.textview.pop(self.curr)
		self.inner_hbox.pop(self.curr)
		self.vbox.pop(self.curr)
		self.notebook.remove_page(self.curr)
		self.popupmenu.remove(self.popupbutton[self.curr])
		self.popupbutton.pop(self.curr)
	print "curr :"+str(self.curr)
	print "######"

def Tab_change(self, notebook, page, page_index):
	print "Tab_change"
	self.curr=self.notebook.get_current_page()

def changed(self, entry):
	print "changed"
	self.curr=self.notebook.get_current_page()
	text = entry.get_text()
	self.notebook.set_tab_label_text(self.vbox[self.curr], text)
	self.popupbutton[self.curr].set_label(text)

def destroy(self,widget): #DONE !
	print "destroy!"
	self.write_to_file()
	gtk.main_quit()


def tray_activate(self, tray):
	print "tray_activate"
	if self.win.isshown:
		self.win.hide()
		self.win.isshown = False
	elif not self.win.isshown:
		self.win.show()
		self.win.isshown = True
def tray_popup(self, one, two, three):
	print "tray_popup"
	self.popupmenu.popup(
	None, None,
	gtk.status_icon_position_menu, 1,
	gtk.get_current_event_time(), self.tray)

def popup_action(self,item):
	print "popup_action"
	self.write_to_file()
	clicked = self.popupbutton.index(item)
	text=str(self.textview[clicked].get_buffer().get_text(
	self.textview[clicked].get_buffer().get_start_iter()
	,self.textview[clicked].get_buffer().get_end_iter()))
	title=str(self.entry[clicked].get_text())
	{
		0: lambda: self.clipboard.set_text(text),
		1: lambda: os.system(str(self.cmd)+" '"+str(title)+"' -e "+os.path.expanduser('~')+"/.config/treenote/"+str(clicked)+".tab &"), #execute
		# TODO : Be able to set the terminal to be used
		#2: lambda: os.system("xdg-open '"+self.tabContent[clicked]+"' &")#open with
	}[self.dropdown[clicked].get_active()]()

def conf_open(self, item):
	print "conf_open"
	if self.conf_win.isshown:
		self.conf_win.hide()
		self.conf_win.isshown=False
	else:
		self.conf_win.show_all()
		self.conf_win.isshown=True



#DO NOT DECLARE ANYTHING UNDER THIS LINE: IT IS MEANT FOR DEBUGGING PURPOSE
def debuger(self, widget):
	#self.curr=self.notebook.get_current_page()
	print "debug"
	print "#####"
	print "i :"+str(self.i)
	print "#####"
	print "Notice: hbox Being single is a normal output \nhbox :"+str(self.hbox)
	print "#####"
	print "curr :"+str(self.curr)
	print "#####"
	print "vbox :"+str(self.vbox)
	print "#####"
	print "entry :"+str(self.entry)
	print "#####"
	print "textview :"+str(self.textview)
	print "#####"
	print "inner_hbox :"+str(self.inner_hbox)
	print "#####"
	print "dropdown :"+str(self.dropdown)
	print "#####"
	print "popupbutton :"+str(self.popupbutton)
