print ('pybank_challenge')
# Create file paths across operating systems
import os
# module for reading csv files
import csv
# pass individual sub components 
csvpath = os.path.join('Resources', 'budget_data.csv')
#../resources/budget_data.csv

#open path and store file as variable "csvfile"
with open (csvpath) as csvfile:
#call csv reader
csvreader = csv.reader(csvfile, delimiter=',')
