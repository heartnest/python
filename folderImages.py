'''
This script navigates folders and moves all the image files to the result folder in the base directory
'''

import os
import shutil

def visit(path):
	for o in os.listdir(path):
		newpath = os.path.join(path, o)
		if os.path.isdir(newpath):
			print(newpath)
			visit(newpath)
		elif "JPG" in newpath or "PNG" in newpath or "jpg" in newpath or "png" in newpath:
			print(">>>",newpath)
			name = newpath.split("/")[-2]
			shutil.move(newpath,result+"/"+name+".JPG")


result = "result"
d = '2019'
xex = [os.path.join(d, o) for o in os.listdir(d) 
                    if os.path.isdir(os.path.join(d,o))]

for x in xex:
	visit(x)