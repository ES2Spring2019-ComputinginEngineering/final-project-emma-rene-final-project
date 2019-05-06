# Emma Whalen and René L.J.
# ES 2 FINAL PROJECT
# Maritime Disaster Survival Rate Analysis 
# Main file


# IMPORT STATEMENTS
from Final_Project import *
import matplotlib.pyplot as plt


# MAIN CODE
tpsex, tpage, tpclass = testpoint()
gsex, geclass, gage, gsurvival= readDataFile1()
nsurvival, neclass, nage, nsex= readDataFile2()
tsurvival, teclass, tsex, tage= readDataFile3()

#Titanic Analysis 
tdistance_array = calculateDistanceArray(tpsex, tpage, tpclass, tsex, tage, teclass)
tnearest_class, min = nearestNeighborClassifier(tpsex, tpage, tpclass, tage, tsex, teclass, tsurvival)
tsortedk = kNearestNeighborClassifier(3, tpsex, tpage, tpclass, tsex, tage, teclass, tsurvival)
tcentroids = select(2)
tassignments =assign(2, tage, tsex, teclass, tcentroids)
tcentroids = update(2, tage, tsex, teclass, tassignments)
tfinal_centroids, tfinal_assignments = iterate(2, tage, tsex, teclass)
t2nearest_class, tmin2 = nearestNeighborTPC(tpsex, tpage, tpclass, tfinal_centroids, tsurvival)

# gives results for Titanic
if t2nearest_class == 1.0:
    print("""Congratulations! You are statistically likely to have survived
          the Titanic sinking.""")
else:
    print("""According to your sex, age, and class, you did not survive the Titanic sinking.""")
#3D Plot for Titanic
fig= plt.figure()
ax= plt.axes(projection='3d')

X= tsex[tsurvival==1]
Y= tage[tsurvival==1]
Z= teclass[tsurvival==1]
X1= tsex[tsurvival==0]
Y1= tage[tsurvival==0]
Z1= teclass[tsurvival==0]

ax.scatter(X,Y,Z, c='g', marker='o', alpha = .1) # plots survival = 1 (survived)
ax.scatter(X1,Y1,Z1, c='r', marker = 'o', alpha = .1) # plots survival = 0
ax.set_xlabel('Sex')
ax.set_ylabel('Age')
ax.set_zlabel('Economic Class')
plt.title('RMS Titanic Survival Analysis')
plt.show()

#GoldenGate Analysis 
gdistance_array = calculateDistanceArray(tpsex, tpage, tpclass, gsex, gage, geclass)
gnearest_class, min = nearestNeighborClassifier(tpsex, tpage, tpclass, gage, gsex, geclass, gsurvival)
gsortedk = kNearestNeighborClassifier(3, tpsex, tpage, tpclass, gsex, gage, geclass, gsurvival)
gcentroids = select(2)
gassignments =assign(2, gage, gsex, geclass, gcentroids)
gcentroids = update(2, gage, gsex, geclass, gassignments)
gfinal_centroids, gfinal_assignments = iterate(2, gage, gsex, geclass)
g2nearest_class, gmin2 = nearestNeighborTPC(tpsex, tpage, tpclass, gfinal_centroids, gsurvival)

# gives results for Golden Gate
if g2nearest_class == 1.0:
    print("""Congratulations! You are statistically likely to have survived
          the Golden Gate sinking.""")
else:
    print("""According to your sex, age, and class, you did not survive the Golden Gate sinking.""")
    
#3D Plot for Golden Gate
fig= plt.figure()
ax= plt.axes(projection='3d')

X= gsex[gsurvival==1]
Y= gage[gsurvival==1]
Z= geclass[gsurvival==1]
X1= gsex[gsurvival==0]
Y1= gage[gsurvival==0]
Z1= geclass[gsurvival==0]

ax.scatter(X,Y,Z, c='g', marker='o',alpha=.1) # plots survival=1 (survived)
ax.scatter(X1,Y1,Z1, c='r', marker='o', alpha=.1) # plots survival=0
ax.set_xlabel('Sex')
ax.set_ylabel('Age')
ax.set_zlabel('Economic Class')
plt.title('SS Golden Gate Survival Analysis')
plt.show()

#Norge Analysis 
ndistance_array = calculateDistanceArray(tpsex, tpage, tpclass, nsex, nage, neclass)
nnearest_class, min = nearestNeighborClassifier(tpsex, tpage, tpclass, nage, nsex, neclass, nsurvival)
nsortedk = kNearestNeighborClassifier(3, tpsex, tpage, tpclass, nsex, nage, neclass, nsurvival)
ncentroids = select(2)
nassignments =assign(2, nage, nsex, neclass, ncentroids)
ncentroids = update(2, nage, nsex, neclass, nassignments)
nfinal_centroids, nfinal_assignments = iterate(2, nage, nsex, neclass)
n2nearest_class, nmin2 = nearestNeighborTPC(tpsex, tpage, tpclass, nfinal_centroids, nsurvival)

# gives Norge results 
if n2nearest_class == 1.0:
    print("""Congratulations! You are statistically likely to have survived
          the SS Norge sinking.""")
else:
    print("""According to your sex, age, and class, you did not survive the SS Norge sinking.""")
    
#3D Plot for Norge 
fig= plt.figure()
ax= plt.axes(projection='3d')

X= nsex[nsurvival==1]
Y= nage[nsurvival==1]
Z= neclass[nsurvival==1]
X1= nsex[nsurvival==0]
Y1= nage[nsurvival==0]
Z1= neclass[nsurvival==0]

ax.scatter(X,Y,Z, c='g', marker='o', alpha=.1) # plots survival = 1 (survived)
ax.scatter(X1,Y1,Z1, c='r', marker='o', alpha=.1) # plots survival = 0
ax.set_xlabel('Sex')
ax.set_ylabel('Age')
ax.set_zlabel('Economic Class')
plt.title('SS Norge Survival Analysis')
plt.show()
