# Emma Whalen

#Please put your code for Step 2 and Step 3 in this file.
import numpy as np
import math
from scipy.stats import mode
# functions
import csv 
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
tpsex, tpage, tpclass = testpoint()

#Main Code 
gsex, geclass, gage, gsurvival= readDataFile1()
nsurvival, neclass, nage, nsex= readDataFile2()
tsurvival, teclass, tsex, tage= readDataFile3()

#3D Plot for Golden Gate
fig= plt.figure()
ax= plt.axes(projection='3d')

X= gsex[gsurvival==1]
Y= gage[gsurvival==1]
Z= geclass[gsurvival==1]
X1= gsex[gsurvival==0]
Y1= gage[gsurvival==0]
Z1= geclass[gsurvival==0]

ax.scatter(X,Y,Z, c='g', marker='o',alpha=.1)
ax.scatter(X1,Y1,Z1, c='r', marker='o', alpha=.1)
ax.set_xlabel('Sex')
ax.set_ylabel('Age')
ax.set_zlabel('Economic Class')
plt.title('SS Golden Gate Survival Analysis')
ax.mouse_init()
plt.show()

#3D Plot for Norge 
fig= plt.figure()
ax= plt.axes(projection='3d')

X= nsex[nsurvival==1]
Y= nage[nsurvival==1]
Z= neclass[nsurvival==1]
X1= nsex[nsurvival==0]
Y1= nage[nsurvival==0]
Z1= neclass[nsurvival==0]

ax.scatter(X,Y,Z, c='r', marker='o', alpha=.1)
ax.scatter(X1,Y1,Z1, c='b', marker='o', alpha=.1)
ax.set_xlabel('Sex')
ax.set_ylabel('Age')
ax.set_zlabel('Economic Class')
plt.title('SS Norge Survival Analysis')
plt.show()

#3D Plot for Titanic
fig= plt.figure()
ax= plt.axes(projection='3d')

X= tsex[tsurvival==1]
Y= tage[tsurvival==1]
Z= teclass[tsurvival==1]
X1= tsex[tsurvival==0]
Y1= tage[tsurvival==0]
Z1= teclass[tsurvival==0]

ax.scatter(X,Y,Z, c='b', marker='|')
ax.scatter(X1,Y1,Z1, c='g', marker = '_')
ax.set_xlabel('Sex')
ax.set_ylabel('Age')
ax.set_zlabel('Economic Class')
plt.title('RMS Titanic Survival Analysis')

plt.show() 

def calculateDistanceArray(tpsex, tpage, tpclass, tsex, tage, teclass):
    distance_array = np.zeros((1960)) # length of arrays = 159
    for i in range(0,1960):
        dist = math.sqrt((tage[i] - tpage)**2 + (tsex[i]-tpsex)**2 + (teclass[i] - tpclass)**2)
        distance_array[i] = dist
    return distance_array

distance_array = calculateDistanceArray(tpsex, tpage, tpclass, tsex, tage, teclass)

def nearestNeighborClassifier(tpsex, tpage, tpclass, tage, tsex, tclass, tsurvival):
    calculateDistanceArray(tpsex, tpage, tpclass, tage, tsex, tclass)
    min = np.argmin(distance_array)
    nearest_class = tsurvival[min]
    return nearest_class, min
        
nearest_class, min = nearestNeighborClassifier(tpsex, tpage, tpclass, tage, tsex, teclass, tsurvival)

def kNearestNeighborClassifier(k, tpsex, tpage, tpclass, tsex, tage, teclass, tsurvival):
    calculateDistanceArray(tpsex, tpage, tpclass, tsex, tage, teclass)
    sorted_indices = np.argsort(distance_array)
    k_indices = sorted_indices[:k]
    k_survival = tsurvival[k_indices]
    sortedk = mode(k_survival)
    return sortedk
