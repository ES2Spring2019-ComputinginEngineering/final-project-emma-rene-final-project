# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:43:12 2019
@author: renel
"""
#Maritime Disaster Survival Analysis 
#Functions File
#Creators: René L.J. and Emma W.

#Libraries 

import numpy as np
import math
from scipy.stats import mode
import csv 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# functions

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

def testpoint():
    instructions = """For age, enter a number between 0 (meaning somewhere 
    between 1 month and  a year) and 100. For social class, enter 1 for first
    class, 2 for second class, and 3 for third class, or enter 0 for crew. For 
    sex, enter M for male or F for female."""
    print(instructions)
    agenum = int(input("Enter age: "))
    if agenum <= 16:
        tpage = 1
    else:
        tpage = 0
    tpclass = int(input("Enter social class: "))
    sexnum = input("Enter sex: ")
    if sexnum == 'M' or sexnum == 'm':
        tpsex = 0
    else:
        tpsex = 1
    return tpsex, tpage, tpclass

def calculateDistanceArray(tpsex, tpage, tpclass, sex, age, eclass):
    distance_array = np.zeros((len(sex)))
    for i in range(0,len(sex)):
        dist = math.sqrt((age[i] - tpage)**2 + (sex[i]-tpsex)**2 + (eclass[i] - tpclass)**2)
        distance_array[i] = dist
    return distance_array

def nearestNeighborClassifier(tpsex, tpage, tpclass, age, sex, eclass, survival):
    distance_array = calculateDistanceArray(tpsex, tpage, tpclass, age, sex, eclass)
    min = np.argmin(distance_array)
    nearest_class = survival[min]
    return nearest_class, min

def kNearestNeighborClassifier(k, tpsex, tpage, tpclass, sex, age, eclass, survival):
    distance_array = calculateDistanceArray(tpsex, tpage, tpclass, sex, age, eclass)
    sorted_indices = np.argsort(distance_array)
    k_indices = sorted_indices[:k]
    k_survival = survival[k_indices]
    sortedk = mode(k_survival)
    return sortedk

# k means clustering

def select(k):
    centroid1 =np.random.randint(0,1,(k,1))
    centroid2 = np.random.randint(0,1,(k,1))
    centroid3 = np.random.randint(0,3,(k,1))
    centroids = np.concatenate((centroid1,centroid2,centroid3), axis=1)
    return centroids

def assign(k, age, sex, eclass, centroids): 
    k = centroids.shape[0]
    distances = np.zeros((k, len(sex)))
    for i in range(k):
        s = centroids[i,0]
        a = centroids[i,1]
        c = centroids[i,2]
        distances[i] = np.sqrt((sex-s)**2 + (age-a)**2 + (eclass-c)**2)
    assignments = np.argmin(distances, axis = 0)
    return assignments

def update(k, age, sex, eclass, assignments):
    newassignments = np.array(assignments)
    centroids = select(k)
    maximum = np.amax(newassignments)
    for i in range(maximum+1):
        centroids[i][1] = np.mean(age[newassignments==i])
        centroids[i][0] = np.mean(sex[newassignments==i])
        centroids[i][2] = np.mean(eclass[newassignments==i])
    return centroids

def iterate(k, age, sex, eclass): 
    iteration = 0
    max_iteration = 5000
    while iteration <= max_iteration:
        final_assignments = assign(k, age, sex, eclass, centroids)
        final_centroids = update(k, age, sex, eclass, assignments)
        iteration +=1
    return final_centroids, final_assignments

"""def calculateDistanceArrayTPC(tpsex, tpage, tpclass, final_centroids):
    distance_array = np.zeros((len(sex)))
    X= 
    Y= 
    Z= 
    for i in range(0,len(sex)):
        dist = math.sqrt((age[i] - tpage)**2 + (sex[i]-tpsex)**2 + (eclass[i] - tpclass)**2)
        distance_array[i] = dist
    return distance_array
"""