import glob
import sys


# join

days = {'monday':1,'tuesday':2,'wednesday':3} #dic
colors = ["lightgray", "cyan", "magenta", "yellow", "blue", "green", "red"] #array
print ', '.join(colors)


# split

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );
print str.split(' ', 1 );


# array for 1

for color in colors:
	print color


# array for 2

for idx, val in enumerate(colors):
	print 'num id:', idx, ' val:',val


# dic for

for (idx,val) in days.iteritems():
	print 'text id:', idx, ' val:',val


# merge list

listone = [1,3,5]
listtwo = [2,1,5,9]
mergedlist = listone + listtwo


# list duplicate elements

mergedlist = list(set(mergedlist))


# list operation

t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
s = [1, 2, 3]
difflist = list(set(t) - set(s))
print difflist

