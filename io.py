import glob
import sys


with open("test.txt") as ff:
	for line in ff:
		if 'special' in line.lower():
		  print 'got specal'
		else:
			print line
