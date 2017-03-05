import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state
import json
import pandas as pd
import os
import re
import csv
print("#################################################################################")
print("Please Enter Data in the form of two columns, first column being String(e.g: Name), and the Second Column being Value (e.g: Integer)")
filename = raw_input("Enter Dataset File path: ")
predict_years = raw_input("Enter the number of years to predict: ")
Current_years = raw_input("Enter the Current number of years: ")
path = '/Users/tushar/Desktop/MobileApp/result.csv'

def convertToJson():
	with open(path) as f:
		reader = csv.DictReader(f)	
    	rows = list(reader)
	with open(path, 'w') as f:
		abc=json.dump(rows, f)
	return abc

def CountryPrediction(filename,predict_years,Current_years):
	#Create a dataframe holding the data fetched from file
	df = pd.read_csv(filename)
	columns=['year','nominee','country']
	dff = pd.DataFrame()
	# Delete file test2.txt
	if os.path.exists(path):
		os.remove(path)
	f = open(path,'w+')
    
	f.write("year,numeric,country")
	f.close()
	d2=[]
	#create an empty array and loop through each row of data.
	String = {}
	f = open(path,'w+')
	for row in df.values:
	    if row[0] in String:
	        String[row[0]] += [row]
	    else:
	        String[row[0]] = [row]

	for key, value in String.iteritems():
	    pass_var = False
	    for v in value:
	        if v[2] < 5:
	        	pass_var = True
	    if not pass_var:
	    	x = np.arange(int(Current_years))
	    	y = [v[2] for v in value]
	    	z = [v[0] for v in value]

	    	lr = LinearRegression()
	        lr.fit(x[:, np.newaxis], y)  # x needs to be 2d for LinearRegression

	        next_years = []
	        for nx in range(int(Current_years), int(Current_years)+int(predict_years)):
	            next_years.append(lr.predict(nx)[0])
	        x = np.concatenate( (x, np.arange(int(Current_years),int(Current_years)+int(predict_years))) )
	        y += next_years

	        for index,elem in enumerate(y):
	        	#f = open(path,'w')
	        	country=re.sub(',','',str(v[0]))
	        	f.write(str(x[index])+","+str(y[index])+","+country+ "\n")
	        	#f.close()
	        	data = {
	        	'year':x[index],
	        	'nominee':y[index],
	        	'country':v[0]
	        	}
	        	d2.append((x[index],y[index],v[0]))
	        json_str = json.dumps(data)
	        #dff.append(data,ignore_index=True)
	
	f.close()
	
    
	return d2
	        	#print x[index],',',y[index],',',v[0]
print CountryPrediction(filename,predict_years,Current_years)  
#print convertToJson()
#print json.dumps(CountryPrediction(filename,predict_years,Current_years))     	
#for index,val in enumerate(CountryPrediction(filename,predict_years,Current_years)):
	
#	print index,val
	#print json.dumps(data)
        
        	


