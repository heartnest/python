#! /usr/bin/env python

'''
This script transforms the schedule for each train to schedule for each station.

Run with the command:
python run.py

Results would be saved in the file result.txt
'''

import glob
import sys

def getTrainTextWithStation(trainDic, stationKey):
	trains = getListOfTrainsTroughStation(trainDic,stationKey)
	formatted_text = ""
	for idx, train in enumerate(trains):
		totalleng = 8
		offset = totalleng - len(train['id'])
		space = ""
		for x in xrange(1,offset):
			space = space + " "
		print "'",space,"'"
		formatted_text = formatted_text + train['id'] + space + train['dep_txt'] + "\n"
	return formatted_text

def getListOfTrainsTroughStation( trainDic,stationKey ):
   "get a list of train ids that cover a specific station"
   
   selectTrains = []
   for (trainID,schedule) in trainDic.iteritems():
	for idx, station in enumerate(schedule):
		pieces = station.split() 
		stationName = pieces[0].strip()

		departure_txt=""
		#get departure
		if len(pieces) == 2:
			departure_txt = pieces[1].strip()
		elif len(pieces) == 3:
			departure_txt = pieces[2].strip()

		departure = convertTime(departure_txt)
		train = {"id":trainID,"dep":departure,"dep_txt":departure_txt}
		if stationKey == stationName:
			selectTrains.append(train)
	
	selectTrains = sorted(selectTrains, key=lambda k: k['dep']) 	
   return selectTrains


def loadDataFromFile(filepath):
	trainID = "";
	trainDic= {}
	stations = []
	with open(testFile) as ff:
		for line in ff:
			if "*" in line: 
				pieces = line.split()  
				trainID = pieces[0]
				trainID = trainID.replace("*","")
				trainDic[trainID] = []
			else:
				trainDic[trainID].append(line)
				pieces = line.split() 
				stationName = pieces[0].strip()
				if stationName not in stations:
					stations.append(stationName)

	return trainDic,stations

def convertTime(timesep):
	pieces = timesep.split(":")
	a = float(pieces[0])
	b = float(pieces[1])/100
	return a+b
#==================================
# Main
#==================================

# program parameters
testFile = "data.txt"
rltFile = "result.txt"




# get the station id from input if assigned
if len(sys.argv) == 2:
	stationKey = sys.argv[1]

# load data
trainDic,stations = loadDataFromFile(testFile)
		
output = ""
for idx, stationKey in enumerate(stations):
	output = output +"\nTrain NO.   "+stationKey+"\n" +getTrainTextWithStation(trainDic, stationKey)+"\n"


# output result in a file
with open(rltFile, 'w+') as outfile:
	outfile.write(output)

# print convertTime(timestr)

print "Done, data produced for",len(stations),"stations"
