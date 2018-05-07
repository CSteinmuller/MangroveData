#Script for data extraction
import os
from os import walk
filelist = []
peaks = []
#get current directory
mypath = os.path.dirname(os.path.realpath(__file__))
#find all the files
for (dirpath, dirnames, filenames) in walk (mypath):
    filelist.extend(filenames)
    break
totalfiles = len(filelist); # get number of files
j = 0
#this works, I just need more test files
while (j < totalfiles):
    datafile = open(filelist[j])
    if filelist[j] != "dataextract.py":
        #reset these
        cutdata = []
        rawdata = []
        rawdata.append(datafile.read())
        k = 0
        while (k < len(rawdata)):
            cutdata = (rawdata[k].split()) #slice based on whitespace
    #        print cutdata
        #    print len(cutdata)
            x = 0
            while (x < len(cutdata)):
                # given the way these files are structured this was the first way to do this that came to mind
                if cutdata[x] == 'Area':
                    peaks.append(filelist[j])
                    peaks.append(cutdata[x+27]) #file seems to be fixed
                    peaks.append(cutdata[x+45]) # ditto
                    print peaks
                    x = len(cutdata)
                x += 1
            k+=1
    datafile.close()
    j += 1
j = 0
outfile = open("data.csv", "wb")
outfile.write("File name, area 1, area 2 \n")
while (j < len(peaks)):
    outfile.write(peaks[j]+", "+peaks[j+1]+", "+peaks[j+2]+"\n")
    j = j + 3
