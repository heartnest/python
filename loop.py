import glob
import sys

def print_tmp(content,count):
    print 'array content ',count,' :', content


print '\n========================================================================='
print 'I will print a list of colors and i\'m particularlly interested in the third one '
print '=========================================================================\n'

colors = ["lightgray", "cyan", "magenta", "yellow", "blue", "green", "red"]
count = 1
for color in colors:
   print_tmp(color,count)

   if count == 3:
   	print 'I love', color,' very much!'

   count = count + 1

