from math import log
from operator import itemgetter,attrgetter
import operator
import types
import csv
import numpy
import math
import sys
import copy
import re
import time
from datetime import date



def readingfile():
    store_1=[]
    label_1=[]
    with open('integrateSize_new.csv','rb') as csvfile_1:
        reader=csv.reader(csvfile_1)
        for row in reader:
            store_1.append(row)
        label_1=store_1[0]
    numfeature_1=len(store_1[0])-1
    with open('temperatureChange.csv','wb') as result:
        file_writer=csv.writer(result)
        for testVec in store_1:
            year=testVec[3][0:4]
            print year
            month=testVec[3][5:7]
            day=testVec[3][8:10]
            currDate=date(int(year),int(month),int(day))
            first=currDate-date(int(year),01,01)
            diff=currDate-first
            transfer=int(diff.total_seconds()/86400)
            Integrate=[]
            Integrate.extend(testVec[0])
            Integrate.extend(testVec[2])
            Integrate.extend(transfer)
            Integrate.extend(testVec[4])
            file_writer.writerow([Temp_1 for Temp_1 in Integrate])
        
            
            
