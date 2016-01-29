import glob
import sys
import math


# join

''' this file compares harmonic(调和函数) function and log '''

maxidx = 1000000
harmse = 0.0

for x in xrange(1,maxidx):
	harmse = harmse + round(float(1)/float(x),10)
	# print round(float(1)/float(x),10)


print harmse,' ',math.log(maxidx, 10)