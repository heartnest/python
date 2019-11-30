import glob
import sys




# STRING
# lower

s = 'heLlo'
print (s.lower())
print (s.upper())


# global var

a = "hallo"
b = "Jim"
def printStr():
	global a,b
	print a,' ^-^', b

printStr()

# check if str is a int (number)
str.isdigit()

# str contains
if "blah" not in "yaoooblah": 
    print ("contains")

# string interpolation format, string insert
print ("INSERT INTO words (word,creater) VALUES ('{}','{}')".format(var,"verb"))

# formastring
string_x =  "%s is %i, %.2f" % ('a', 12,12.2)
print (string_x)

# Split
text = "a, b, c"
words = text.split()  


# Substitution 
print ("string substitution")
testStr = "Hello"
print (testStr)
testStr = testStr.replace('T', 'S')
print (testStr)

#trim
testStr = ' Hello '.strip()
print ("trim string:'",testStr,'\'')
print (testStr)

# line break
query = "INSERT INTO words (word,sigf,creater,crtdate,type)\
VALUES ('{}','{}','{}',{},{})".format(idx,val,"verb",20180111,1)

# remove last character
st =  "abcdefghij"
st = st[:-1]

# join
seq = ['a','b','c']
','.join(seq)


