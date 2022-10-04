# Topic 02: Lab - Trains.py
# This program reads in xml from the irish rail API
# Author: Ross Downey
# Data Representation; Lecturer: Andrew Beatty

'''Get required modules'''
import requests
import csv
from xml.dom.minidom import parseString


url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML" # Website for data
page = requests.get(url) # variable for the requested data
doc = parseString(page.content) # parse the data from the page variable


# check it works
# print (doc.toprettyxml())
'''
# if I want to store the xml in a file. You can comment this out later
with open("trainxml.xml","w") as xmlfp:
doc.writexml(xmlfp)
'''

# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
# Using with function to write the csv file
with open('Topic-02_train.csv', mode='w', newline='') as train_file: # newline = '' removes blank lines, see link above
    # csv file properties
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# For loop must be within "with Open..." indentations or else it sees it as closed
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions") # new var taking elements from tag names
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0) # first element in train positions node is 0
        traincode = traincodenode.firstChild.nodeValue.strip() # strip all extra spaces if they are there for presentation
# New array called datalist created append the traincode details to
        dataList = []
        dataList.append(traincode)
        train_writer.writerow(dataList)

