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

def test():
    with open('feasures3.csv','rb')as csvfile_1:
        reader=csv.reader(csvfile_1)
        print reader
       
    

def readingfile():
    # Filename_1 is training set
    # Filename_2 is Festure set
    train_1=[]
    train_2=[]
    train_3=[]
    label_1=[]
    label_2=[]
    label_3=[]
    label=[]
    with open('train.csv','rb')as csvfile_1:
        reader=csv.reader(csvfile_1)
        for row in reader:
            train_1.append(row)
        label_1=train_1[0]
    with open('features.csv','rb')as csvfile_2:
        reader_2=csv.reader(csvfile_2)
        for row in reader_2:
            train_2.append(row)
        label_2=train_2[0]

  #  print train_1
  #  print train_2[0]
    label.extend(label_1)
   # print label[1]
    label.extend(label_2[i] for i in range(2,11))
    del train_1[0]
    del train_2[0]
    numfeature_1=len(train_1[0])-1
    numfeature_2=len(train_2[0])-1
    with open('Db_Intergration.csv','wb') as result:
        file_writer=csv.writer(result)
        file_writer.writerow([Temp for Temp in label])
        for testVec_1 in train_1:
            for testVec_2 in train_2:
                if (testVec_1[0]==testVec_2[0])&(testVec_1[2]==testVec_2[1]):
                    Integrate=[]
                    Integrate.extend(testVec_1)
                    Integrate.extend(testVec_2[i] for i in range(2,11))
                    file_writer.writerow([Temp_1 for Temp_1 in Integrate])

def integration():
    data_1=[]
    data_2=[]
    label_1=[]
    label_2=[]
    label=[]
    with open('Db_Intergration.csv','rb') as csvfile_2:
        reader_2=csv.reader(csvfile_2)
        for row in reader_2:
            data_2.append(row)
        label_2=data_2[0]
    with open('store.csv','rb') as csvfile_1:
        reader_1=csv.reader(csvfile_1)
        for row in reader_1:
            data_1.append(row)
        label_1=data_1[0]
    del data_1[0]
    del data_2[0]
    
    label.extend(label_2)
    label.append('Type')
    label.append('Size')
    label.append('Month')
    numfeature_1=len(data_1[0])-1
    numfeature_2=len(data_2[0])-1
    with open('integrateSize.csv','wb') as result:
        file_writer=csv.writer(result)
        file_writer.writerow([Temp for Temp in label])
        for testVec_1 in data_1:
            for testVec_2 in data_2:
                if (testVec_1[0]==testVec_2[0]):   
                    Integrate=[]
                    Month=testVec_2[2][testVec_2[2].find('/')+1:testVec_2[2].rfind('/')]

                    Integrate.extend(testVec_2)
                    Integrate.extend(testVec_1[i] for i in range(1,3))
                    Integrate.append(Month)
                    file_writer.writerow([Temp_1 for Temp_1 in Integrate])


def testIntegrate():
    # Filename_1 is training set
    # Filename_2 is Festure set
    test_1=[]
    test_2=[]
    train_3=[]
    label_1=[]
    label_2=[]
    label_3=[]
    label=[]
    with open('test.csv','rb')as csvfile_1:
        reader=csv.reader(csvfile_1)
        for row in reader:
            test_1.append(row)
        label_1=test_1[0]
    with open('features.csv','rb')as csvfile_2:
        reader_2=csv.reader(csvfile_2)
        for row in reader_2:
            test_2.append(row)
        label_2=test_2[0]

  #  print train_1
  #  print train_2[0]
    label.extend(label_1)
   # print label[1]
    label.extend(label_2[i] for i in range(2,11))
    del test_1[0]
    del test_2[0]
    with open('testIntegrate.csv','wb') as result:
        file_writer=csv.writer(result)
        file_writer.writerow([Temp for Temp in label])
        for testVec_1 in test_1:
            for testVec_2 in test_2:
                if (testVec_1[0]==testVec_2[0])&(testVec_1[2]==testVec_2[1]):
                    Integrate=[]
                    Integrate.extend(testVec_1)
                    Integrate.extend(testVec_2[i] for i in range(2,11))
                    file_writer.writerow([Temp_1 for Temp_1 in Integrate])

def integrationTest():
    data_1=[]
    data_2=[]
    label_1=[]
    label_2=[]
    label=[]
    with open('testIntegrate.csv','rb') as csvfile_2:
        reader_2=csv.reader(csvfile_2)
        for row in reader_2:
            data_2.append(row)
        label_2=data_2[0]
    with open('store.csv','rb') as csvfile_1:
        reader_1=csv.reader(csvfile_1)
        for row in reader_1:
            data_1.append(row)
        label_1=data_1[0]
    del data_1[0]
    del data_2[0]
    
    label.extend(label_2)
    label.append('Type')
    label.append('Size')
    label.append('Month')
    numfeature_1=len(data_1[0])-1
    numfeature_2=len(data_2[0])-1
    with open('integrateTest.csv','wb') as result:
        file_writer=csv.writer(result)
        file_writer.writerow([Temp for Temp in label])
        for testVec_1 in data_1:
            for testVec_2 in data_2:
                if (testVec_1[0]==testVec_2[0]):   
                    Integrate=[]
                    if testVec_2[2].find('/')!=0:
                        Month=testVec_2[2][testVec_2[2].find('/')+1:testVec_2[2].rfind('/')]
                    if testVec_2[2].find('-')!=0:
                        Month=testVec_2[2][testVec_2[2].find('-')+1:testVec_2[2].rfind('-')]
                        
                    Integrate.extend(testVec_2)
                    Integrate.extend(testVec_1[i] for i in range(1,3))
                    Integrate.append(Month)
                    file_writer.writerow([Temp_1 for Temp_1 in Integrate])

def NA():
    data_1=[]
    data_2=[]
    label_1=[]
    stat=[]
    mean=[]
    temp=[]
    with open('integrateTest.csv','rb') as csvfile_1:
        reader_1=csv.reader(csvfile_1)
        for row in reader_1:
            data_1.append(row)
        label_1=data_1[0]
    del data_1[0]
    numfeature=len(data_1[0])-1
    
    for i in range(0,numfeature+1):
        stat.append([0.1])
        mean.append(0.1)
        temp.append([0.1])
    for testVec in data_1:
        for i in range(0,numfeature+1):        
            stat[i].append([testVec[i]])
    for i in range(0,numfeature+1):
        for member in stat[i]:
            if isinstance(member,int):
                temp[i].append(member)
        mean[i]=numpy.mean(temp[i])
    for testVec in data_1:
        for i in range(0,numfeature+1):
            if testVec[i]=='NA':
                testVec[i]=mean[i]
        data_2.append(testVec)
    with open('withoutNA.csv','wb') as result:
        file_writer=csv.writer(result)
        file_writer.writerow([Temp for Temp in label_1])
        for testVec in data_2:
            file_writer.writerow([Temp_1 for Temp_1 in testVec])
        
        
    
        
    
            
            
        
    
    
                    

    



    
        
    
    
    
    

                
                
                
    
    
        
