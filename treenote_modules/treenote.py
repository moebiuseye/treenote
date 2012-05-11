#!/usr/bin/python
# -*- coding: UTF-8 -*-

def void():
	# Auteur : moebius_eye
	# treenote est un petit outil pour la note de petit elements.
	# ceci est une version 2.0
	# (postez vos idées à moebius.eye@gmail.com)
	#
	# License : GNU/GPL
	# date de creation du projet: Lundi 9 Mars 2011
	# Doit passer sous license IDFCWYDWI 
	print 'Nuts' # Hum... Hum... 

import pygtk
pygtk.require("2.0")
import gtk
import os
import sys
from subprocess import call

class treenote:
	def __init__(self):
		self.debug = False #set to False on release!!!!
		settings = gtk.settings_get_default()

		self.clipboard = gtk.clipboard_get()


		self.set_data()
		self.set_buttons()
		self.set_notebook()
		self.set_boxes()
		self.set_menubar()
		self.set_main_vbox()
		self.set_window()
		self.set_tray_icon()
		self.retreive_from_file()#Finaly, we can get the content from files and add elements to the UI
		self.get_config()

		gtk.main()#Let's loop it!!!

	def set_data(self):
		self.i=-1
		self.curr=-1
		self.Add_button=gtk.Button()
		self.Close_button=gtk.Button()
		self.debug_button=gtk.Button()
		self.notebook=gtk.Notebook()
		self.hbox=gtk.HBox()
		self.noteLabel=[]
		self.vbox=[] # WARNING : This vbox is to be used INSIDE the notebook
		self.inner_hbox=[] #WARNING : This HBox is to be used inside the first column of the previous VBox
		self.entry=[]
		self.dropdown = []
		self.popupbutton=[]
		self.scroll=[]#a gtk.ScrolledWindow()
		self.textview=[]
		self.main_vbox=gtk.VBox()
		self.win = gtk.Window()
		self.conf_win=gtk.Window()



	def set_state(self): #Is used to get the state of the interface and set informations to the variables. 
		self.curr=self.notebook.get_current_page()
		if self.curr==-1:
			self.curr=0
		print "self.curr == "+str(self.curr)


#~ import functions :
	#Events
	def Add_tab(self, widget):
		Add_tab(self, widget)
	def Close_tab(self, widget):
		Close_tab(self, widget)
	def destroy(self,widget):
		destroy(self, widget)
	def Tab_change(self, notebook, page, page_index):
		Tab_change(self, notebook, page, page_index)
	def changed(self,entry):
		changed(self,entry)
	def tray_activate(self, tray):
		tray_activate(self, tray)
	def tray_popup(self, one, two, three):
		tray_popup(self, one, two, three)
	def popup_action(self,item):
		popup_action(self,item)
	def conf_open(self, item):
		conf_open(self, item)

	def debuger(self, widget):
		debuger(self, widget)


	#mainUI
	def set_main_vbox(self):
		set_main_vbox(self)
	def set_menubar(self):
		set_menubar(self)
	def set_window(self):
		set_window(self)
	def set_buttons(self):
		set_buttons(self)
	def set_boxes(self):
		set_boxes(self)
	def set_notebook(self):
		set_notebook(self)
	def set_dropdown(self):
		set_dropdown(self)
	def set_tray_icon(self):
		set_tray_icon(self)
	def set_conf_window(self):
		set_conf_window(self)

	#Files
	def write_to_file(self):
		write_to_file(self)
	def retreive_from_file(self):
		retreive_from_file(self)
	def set_dropdown_from_file(self, int):
		set_dropdown_from_file(self, int)
	def set_homedir(self):
		set_homedir(self)
	def get_config(self):
		get_config(self)

#sys.path.append("./")
#from charcoder import *
from main_UI import *
from files import *
from Events import *

treenote()
