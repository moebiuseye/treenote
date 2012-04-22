import gtk, os, sys


textview=gtk.TextView()

scroll=gtk.ScrolledWindow()
scroll.show()
scroll.add(textview)

win=gtk.Window()
win.add(scroll)
win.show_all()

gtk.main()
