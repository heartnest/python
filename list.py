import glob
import sys

#range with increment, e.g. 4,6,8
for i in range(4, 10, 2):
	print(i)

# join

days = {'monday':1,'tuesday':2,'wednesday':3} #dic
colors = ["lightgray", "cyan", "magenta", "yellow", "blue", "green", "red"] #array
print ', '.join(colors)


# sort dic by val
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1),reverse=True)

# itemgetter supports multiple args
# itemgetter(1,1,1,1)

# sort dic by key
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))


# sort a list of lists according to its number of elements
testlist = [
		[2,4,7],
		[4,4,6,7,8,2,3],
		[1]
	]
testlist.sort(key=lambda x: len(x))
print testlist

#zip, dot product
xvec = [10, 20, 30]
yvec = [7, 5, 3]
print sum(x*y for x,y in zip(xvec, yvec))         # dot product

# split

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );
print str.split(' ', 1 );


# copy a dictionary
import copy
my_dict2 = copy.deepcopy(my_dict1)

# array for 1

for color in colors:
	print color


# array for 2

for idx, val in enumerate(colors):
	print 'num id:', idx, ' val:',val

#array append

lst = ["la"]
lst.append("lo")
print len(lst)

# dic creation
dic = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
dic['Age'] = 8; # update existing entry
dic['School'] = "DPS School"; # Add new entry



# dic for

for (idx,val) in days.iteritems():
	print 'text id:', idx, ' val:',val


for (a,b) in dit.items():
	print a,b

# dic key

if "sunday" in days:
	print 'sunday is in list'
elif 'monday' in days:
	print 'sunday is not in list, but monday is'


# merge list

listone = [1,3,5]
listtwo = [2,1,5,9]
mergedlist = listone + listtwo


# list duplicate elements

mergedlist = list(set(mergedlist))

# Converting Python Dictionary to List [duplicate]
dictx.items()


# list operation

t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
s = [1, 2, 3]
difflist = list(set(t) - set(s))
print difflist


# intersection

b1 = [1,2,3,4,5,9,11,15]
b2 = [4,5,6,7,8]
set(b1).intersection(b2)
# set([4, 5])

# list comprehension
list_of_int = [int(x) for x in list_of_str] # element conversion
new_list_ele = [idx for idx, val in enumerate(list_of_elements) if val != 0] # list index and value with filters

# continue
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter

# delete dictionary item
del d[key]


# print formatted matrix
# print ', '.join('\n{}'.format( i) for v, i in enumerate(domain_costs))
# print ', '.join('\n{}'.format( i) for v, i in enumerate(link_weights))
# print ', '.join('\n{}'.format( i) for v, i in enumerate(vnfs))