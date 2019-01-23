import glob
import sys

testFile = "test.txt"

with open(testFile) as ff:
	for line in ff:
		if 'special' in line.lower():
		  print 'got specal'
		else:
			print line

# read first line
with open(smart_conf, 'r') as f:
      first_line = f.readline()


      
# over write, create if not exist
with open(testFile, 'w+') as outfile:
	out = "output"
	outfile.write(out)

# append
with open(testFile, 'a+') as outfile:
	out = "output"
	outfile.write(out)

with open(testFile, 'r') as content_file:
    content = content_file.read()

# json

with open('../../generator/data/types.json') as filejson:
	raw = json.load(filejson)
	rawarr = raw['filmCnv']

with open(preferenjson, 'w') as outfile:
    json.dump(arr, outfile)


if len(sys.argv) == 1:
	print __doc__
	sys.exit(0)
else: 
	year = sys.argv[1]


# make directory

if not os.path.exists(kb_dir):
    os.makedirs(kb_dir)

# file exist
if not os.path.exists(jsonpath):
	pass

# read dir files:
for subdir in os.listdir(path + '/cv_' + scenario):
      if 'train_' in subdir and 'kb_' not in subdir:
        subdir = path + '/cv_' + scenario+"/"+subdir
        print 'Training',subdir

# abs path
root_arr = os.path.realpath(__file__).split('/')[:-1]
print root_arr,'as file directory path'


    