#!/usr/bin/python
# -*- coding: UTF-8 -*-

def decode_chars(self, string): # DONE !
	print "decode_chars!"
	string = string.split("\n")
	i=0
	for st in string:
		string[i] = st.replace("&nl;", "\n")
		string[i] = st.replace("&and;", "&")
		i+=1
		print str(string)
	string = string[0:-1]
	print str(string)
	return string


def encode_chars(self, string): # DONE !
	print "encode_chars!"
	string = string.replace("&", "&and;")
	string = string.replace("\n", "&nl;")
	return string
