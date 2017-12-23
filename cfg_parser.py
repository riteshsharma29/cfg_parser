#!/usr/bin/python
# coding: utf-8 -*-

import sys

def help():

	print ""
	print ""
	print ""
	print ""
	print ""
	print ""
	print "1st parameter / argument: path-to-the-configuration-file"
	print "2nd parameter / argument: String/Key to find in the file"
	print "3rd parameter / argument: Key:value seprator"
	print ""
	print ""

def check_param():

	if len(sys.argv) < 2:
		print ""
		print ""
		print "Error !!!"
		print "Filename not passed as 1st parameter / argument"
		print ""
		print ""
		help()
		sys.exit()
	elif len(sys.argv) < 3:
		print ""
		print ""
		print "Error !!!"
		print "Filename with path found but string to find not passed as 2nd parameter / argument"
		print ""
		print ""
		help()
		sys.exit()
	elif len(sys.argv) < 4:
		print ""
		print ""
		print "Error !!!"
		print "Filename with path found,string to find in the file found but value separator missing"
		print ""
		print ""
		help()
		sys.exit()

def parse_config(filename,sepr,xval):

	filename = sys.argv[1]
	xval = sys.argv[2]
	sepr = sys.argv[3]

	input_file = open(filename, 'r')

	for line in input_file:
		line1 = line.rstrip('\n')
		if sepr in line1:
			x1, y1 = line1.split(sepr, 1)
			x1 = x1.strip().replace("_","")
			xval = xval.strip().replace("_","")
			if x1.lower() == xval.lower():
				print line1


check_param()
parse_config(sys.argv[1],sys.argv[2],sys.argv[3])
