import sys
import re
import csv
import fileinput
from collections import Counter
import os
from datetime import datetime
import json

#refactor this code

#set the constants
platform = "odyssey"
server = "browser" #can IT add server name to log entries?
method = "GET"
#get a list of the files in the directory
filepath = 'c:/users/bdonnelly/my documents/odsy_har_files/'
 
#get the list of files in filepath
listofFiles = os.listdir(filepath)


#if the file is unparsed:

#parse it and rename it
#write the parsed file


for fname in listofFiles:
    pathParts = os.path.splitext(fname)
    ext = pathParts[1]
    rep_file = pathParts[0]
    if ext == '.har':
        inputFile = open(filepath + fname, 'r')
        har = json.loads(open(filepath + fname).read())
        
        # open the extract file for p:rocessing
        #inputFile = open(filepath + fname, 'r')
        outputFilename = filepath + rep_file + "_" + method.lower() + ".txt"
        outputFile = open(outputFilename, 'w')
        #sys.stdout.write(fname + '\n')
        for i in range(len(har["log"]["entries"])):
            if har["log"]["entries"][i]["request"]["method"] == method:
               
                line = har["log"]["entries"][i]["request"]["url"]
                if "https://api.serviceceo.net/api/" in line: #check if the line is a valid execution
                    if "https://api.serviceceo.net/api/token" not in line:
            #temp code for just getting calls
                        #line = line.split()[1]
                        line = line.strip('\"')
                        line = line.strip('\,\"')

                        if method == "POST":
                            posttext = har["log"]["entries"][i]["request"]["postData"]["text"]
                            line = line + " " + posttext
                        output = line + '\n'
                        outputFile.write(output)
                        #sys.stdout.write(output)
                    
            

        #close the input and output files
        inputFile.close()   
        outputFile.close()
