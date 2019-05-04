"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!""

# This files should not contain any function defitions"""


# IMPORT STATEMENTS
from Final_Project import *
import matplotlib.pyplot as plt


# DEMONSTRATION CODE


#Main Code 
tpsex, tpage, tpclass = testpoint()
gsex, geclass, gage, gsurvival= readDataFile1()
nsurvival, neclass, nage, nsex= readDataFile2()
tsurvival, teclass, tsex, tage= readDataFile3()

#Titanic Analysis 
distance_array = calculateDistanceArray(tpsex, tpage, tpclass, tsex, tage, teclass)
nearest_class, min = nearestNeighborClassifier(tpsex, tpage, tpclass, tage, tsex, teclass, tsurvival)
sortedk = kNearestNeighborClassifier(3, tpsex, tpage, tpclass, tsex, tage, teclass, tsurvival)
centroids = select(2)
assignments =assign(2, tage, tsex, teclass, centroids)
centroids = update(2, tage, tsex, teclass, assignments)
final_centroids, final_assignments = iterate(2, tage, tsex, teclass)

#3D Plot for Titanic
fig= plt.figure()
ax= plt.axes(projection='3d')

X= tsex[tsurvival==1]
Y= tage[tsurvival==1]
Z= teclass[tsurvival==1]
X1= tsex[tsurvival==0]
Y1= tage[tsurvival==0]
Z1= teclass[tsurvival==0]

ax.scatter(X,Y,Z, c='b', marker='o', alpha = .1)
ax.scatter(X1,Y1,Z1, c='g', marker = 'o', alpha = .1)
ax.set_xlabel('Sex')
ax.set_ylabel('Age')
ax.set_zlabel('Economic Class')
plt.title('RMS Titanic Survival Analysis')
plt.show()

#GoldenGate Analysis 
distance_array = calculateDistanceArray(tpsex, tpage, tpclass, gsex, gage, geclass)
nearest_class, min = nearestNeighborClassifier(tpsex, tpage, tpclass, gage, gsex, geclass, gsurvival)
sortedk = kNearestNeighborClassifier(3, tpsex, tpage, tpclass, gsex, gage, geclass, gsurvival)
centroids = select(2)
assignments =assign(2, gage, gsex, geclass, centroids)
centroids = update(2, gage, gsex, geclass, assignments)
final_centroids, final_assignments = iterate(2, gage, gsex, geclass)

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
plt.show()

#Norge Analysis 
distance_array = calculateDistanceArray(tpsex, tpage, tpclass, nsex, nage, neclass)
nearest_class, min = nearestNeighborClassifier(tpsex, tpage, tpclass, nage, nsex, neclass, nsurvival)
sortedk = kNearestNeighborClassifier(3, tpsex, tpage, tpclass, nsex, nage, neclass, nsurvival)
centroids = select(2)
assignments =assign(2, nage, nsex, neclass, centroids)
centroids = update(2, nage, nsex, neclass, assignments)
final_centroids, final_assignments = iterate(2, nage, nsex, neclass)

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
