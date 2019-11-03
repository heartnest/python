import csv
import json
import sys
import pandas as pd

# ref. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html
# https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/


def selColum(df):
	ndf = df.filter(items=['Name', 'Salary'])
	print(ndf)
	return ndf
	

def selRow(df):
	ndf = df.iloc[2:4]
	print(ndf)
	return ndf
	

def selQuery(df):
	ndf = df.query('Salary>50000')
	print(ndf)
	return ndf


def loadData():
	stack = []
	df = pd.read_csv('filename.csv',header=0,encoding = 'unicode_escape',delimiter=';')

	# print(df)
	# selColum(df)
	# selRow(df)
	ndf = selQuery(df)

	# output
	ndf.to_csv('out.csv')

	counter = 0
	for index, row in df.iterrows():
		counter += 1
		stack.append([row['Name'],row['Hire Date']])
	return stack



def main(args):
	# do something
	data_stack = loadData()
	print(data_stack)



if __name__ == '__main__':
  main(sys.argv[1:])