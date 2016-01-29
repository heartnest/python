import glob
import sys

testFile = "test.txt"

with open(testFile) as ff:
	for line in ff:
		if 'special' in line.lower():
		  print 'got specal'
		else:
			print line

with open(testFile, 'w+') as outfile:
	out = "output"
	outfile.write(out)