#!/usr/bin/python
# -*- coding: UTF-8 -*-

from distutils.core import setup
import os


#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = ["src/*"]


setup(name = "treenote",
	version = "2.2.1",
	description = "yadda yadda",
	author = "moebius_eye",
	author_email = "moebius.eye@gmail.com",
	url = "http://moebiuseye.co.de/",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
	packages = ['treenote_modules'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
	package_data = {'treenote' : files },
    #'runner' is in the root.
	scripts = ["treenote"],
	long_description = "Really long text here.",
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []
	data_files=[("share/treenote/", ["data/content.conf", "data/action.conf", "data/0.tab"]), ("share/pixmaps/", ["data/treenote.png"])]
    )#TODO : Include configuration files.

#os.chmod("/usr/tmp/treenote_exec", 0776)
#os.chown("/usr/tmp/treenote_exec", 'users', 'users')
