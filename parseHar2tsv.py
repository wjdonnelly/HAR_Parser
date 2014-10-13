import sys
import re
import csv
import fileinput
from collections import Counter
import os
from datetime import datetime


#set the constants
platform = "odyssey"
server = "browser" #can IT add server name to log entries?

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
        
        # open the extract file for p:rocessing
        inputFile = open(filepath + fname, 'r')
        outputFilename = filepath + fname + "_parsed.txt"
        outputFile = open(outputFilename, 'w')
        #sys.stdout.write(fname + '\n')
        for line in inputFile:
            
            if "\"url\"" in line and "https://api.serviceceo.net/api/" in line: #check if the line is a valid execution
                if "https://api.serviceceo.net/api/token" not in line:
            #temp code for just getting calls
                    line = line.split()[1]
                    line = line.strip('\"')
                    line = line.strip('\,\"')
                    output = line + '\n'
                    outputFile.write(output)
        sys.stdout.write(fname)
                    
    

        #close the input and output files
        inputFile.close()   
        outputFile.close()
