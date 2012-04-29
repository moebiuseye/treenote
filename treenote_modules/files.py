#!/usr/bin/python
# -*- coding: UTF-8 -*-


import gtk
import os
import shutil

def encode(text):
	print "code"
	text=text.replace("\\", "\\\\")
	print text
	return text

def decode(text):
	print "decode"
	text=text.replace("\\\\", "\\")
	print text
	return text

def write_to_file(self):
	print "write_to_file"
	content=""
	action=""
	home = os.path.expanduser('~')
	i=0
	try: os.mkdir(home+"/.config/treenote", 0775)
	except: print "Le dossier existe"
	for entry in self.entry:
		jesusthesavior=open(home+"/.config/treenote/"+str(i)+".tab", "w",0)
		os.chmod(home+"/.config/treenote/"+str(i)+".tab", 0744)
		data=str(self.textview[i].get_buffer().get_text(self.textview[i].get_buffer().get_start_iter()
		,self.textview[i].get_buffer().get_end_iter()))
		jesusthesavior.write(data)
		content+=encode(str(self.entry[i].get_text()))+"\n"
		print "content :"+content
		action+=encode(str(self.dropdown[i].get_active()))+"\n"
		print "action :"+action
		i+=1
	jesusthesavior=open(home+"/.config/treenote/content.conf", "w",0)
	jesusthesavior.write(content)
	jesusthesavior=open(home+"/.config/treenote/action.conf", "w",0)
	jesusthesavior.write(action)

def retreive_from_file(self):
	print "retreive_from_file"
	home = os.path.expanduser('~')
	if not os.path.isdir( home+"/.config/treenote" ) :
		try: 
			shutil.copytree("/usr/local/share/treenote", home+"/.config/treenote")
		except :
			print "Files couldn't be copied ! "
			pass
	if os.path.isfile(home+"/.config/treenote/content.conf"):
		jesusthecanopener=file(home+"/.config/treenote/content.conf", "r+w",0)
		raw_content=jesusthecanopener.read()
		raw_content=decode(raw_content)
		titles=raw_content.split("\n")
		titles.pop(len(titles)-1)
		if os.path.isfile(home+"/.config/treenote/action.conf"):
			jesusthecanopener=file(home+"/.config/treenote/action.conf", "r+w",0)
			raw_content=jesusthecanopener.read()
			act=raw_content.split("\n")
			act.pop(act.index(""))
			for title in titles:
				print title+"\n"
				self.i+=1
				if os.path.isfile(home+"/.config/treenote/"+str(self.i)+".tab"):
					jesusthecanopener=file(home+"/.config/treenote/"+str(self.i)+".tab", "r+w",0)
					content=str(jesusthecanopener.read())
					buffer=gtk.TextBuffer()
					buffer.set_text(content)
					self.noteLabel.append(gtk.Label(title))
					self.vbox.append(gtk.VBox())
					self.inner_hbox.append(gtk.HBox())
					self.entry.append(gtk.Entry())
					self.entry[self.i].set_text(title)
					self.entry[self.i].connect("changed", self.changed)
					self.set_dropdown_from_file(int(act[self.i]))
					self.textview.append(gtk.TextView())
					self.textview[self.i].set_buffer(buffer)
					self.scroll.append(gtk.ScrolledWindow())
					self.scroll[self.i].add(self.textview[self.i])
					self.inner_hbox[self.i].pack_start(self.entry[self.i])
					self.inner_hbox[self.i].pack_start(self.dropdown[self.i])
					self.vbox[self.i].pack_start(self.inner_hbox[self.i], False)
					self.vbox[self.i].pack_start(self.scroll[self.i])
					self.notebook.append_page(self.vbox[self.i],self.noteLabel[self.i])
					self.popupbutton.append(gtk.MenuItem(title))
					self.popupbutton[self.i].connect("activate", self.popup_action)
					self.popupmenu.append(self.popupbutton[self.i])
					self.popupmenu.show_all()
					self.win.show_all()

def set_dropdown_from_file(self, var):
	print "set_dropdown_from_file"
	self.dropdown.append(gtk.combo_box_new_text())
	self.dropdown[self.i].append_text("copy")
	self.dropdown[self.i].append_text("execute")
	self.dropdown[self.i].set_active(var)


def get_config(self):
	print "TODO : get_config"
	print str(self.terminal_entry.get_text())
