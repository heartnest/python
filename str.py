import glob
import sys




# STRING
# lower

s = 'heLlo'
print s.lower()
print s.upper()


# global var

a = "hallo"
b = "Jim"
def printStr():
	global a,b
	print a,' ^-^', b

printStr()


# str contains
if "blah" not in "yaoooblah": 
    print "contains"


# Split
text = "a, b, c"
words = text.split()  


# Substitution 
print "string substitution"
testStr = "Hello"
print testStr
testStr = testStr.replace('H', 'Y')
print testStr

#trim
testStr = ' Hello '.strip()
print "trim string:'",testStr,'\''
print testStr
