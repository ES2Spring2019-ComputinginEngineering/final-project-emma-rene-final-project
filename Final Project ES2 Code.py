# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:43:12 2019

@author: renel
"""
#Maritime Disaster Survival Analysis 
#Functions File
#Creators: René L.J. and Emma W.

#Libraries 
import csv 
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#Functions 
def readDataFile1(): 
   csv_file= open('goldengate.csv')
   total_row = sum(1 for row in csv_file)-1

   csv_file.seek(0) 
   csv_reader = csv.reader(csv_file, delimiter=',')
    
   gsex= np.zeros((total_row,))
   geclass= np.zeros((total_row,))
   gage= np.zeros((total_row,))
   gsurvival= np.zeros((total_row,))
    
   index = 0 
    
   for row in csv_reader: 
       if index ==0: 
           print(row)
   else: 
       gsex[index-1] = (row[0])
       geclass[index-1] = (row[1])
       gage[index-1] = (row[2]) 
       gsurvival[index-1]= (row[3])
   index += 1
   return gsex, geclass, gage, gsurvival

def readDataFile2(): 
   csv_file= open('norge.csv')
   total_row = sum(1 for row in csv_file)-1

   csv_file.seek(0) 
   csv_reader = csv.reader(csv_file, delimiter=',')
    
   nsurvival= np.zeros((total_row,))
   neclass= np.zeros((total_row,))
   nage= np.zeros((total_row,))
   nsex= np.zeros((total_row,))
    
   index = 0 
    
   for row in csv_reader: 
         if index ==0: 
           print(row)
   else: 
       nsurvival[index-1] = (row[0])
       neclass[index-1] = (row[1])
       nage[index-1] = (row[2]) 
       nsex[index-1]= (row[3])
   index += 1
   return nsurvival, neclass, nage, nsex

def readDataFile3():
    csv_file= open('titanic.csv')
    total_row = sum(1 for row in csv_file)-1

    csv_file.seek(0) 
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    tsurvival= np.zeros((total_row,))
    teclass= np.zeros((total_row,))
    tsex= np.zeros((total_row,))
    tage= np.zeros((total_row,))
    
    index = 0 
 
    for row in csv_reader: 
          if index ==0: 
           print(row)
    else: 
      tsurvival[index-1] = (row[0])
      teclass[index-1] = (row[1])
      tsex[index-1] = (row[2]) 
      tage[index-1]= (row[3])
    index += 1
    return tsurvival, teclass, tsex, tage

#Main code 
gsex, geclass, gage, gsurvival= readDataFile1()
nsurvival, neclass, nage, nsex= readDataFile2()
tsurvival, teclass, tsex, tage= readDataFile3()

#3D Plot Creation for Golden Gate
#ADD OVERALL TITLE 
fig= plt.figure()
ax= plt.axes(projection='3d')

X= gsex
Y= gage
Z= geclass

ax.scatter(X,Y,Z, c='r', marker='o')
ax.set_xlabel('Sex')
ax.set_ylabel('Age')
ax.set_zlabel('Economic Class')

plt.show()
