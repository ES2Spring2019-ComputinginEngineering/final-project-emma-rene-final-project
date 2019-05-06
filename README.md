# Maritime Disaster Survival Rate Analysis

Our project analyzes the crew and passenger lists from three different historical maritime disasters (The SS Norge, Golden Gate, and Titanic sinking), graphs the data on 3D plots, and tells you whether or not an individual will survive given a specific age, sex, and class.

## Instructions

- Run the main.py file to start the program. 
- When prompted, answer the questions regarding sex, age, and social class. 
- The file will take this information and ultimately return a predicted fate based on statistics from each of the maritime distasters we used. It will also graph the data.
Each result is claculated given a test point and the data from a specific file using the code design below in the main demonstration file.
```
#Titanic Analysis 
tdistance_array = calculateDistanceArray(tpsex, tpage, tpclass, tsex, tage, teclass)
tnearest_class, min = nearestNeighborClassifier(tpsex, tpage, tpclass, tage, tsex, teclass, tsurvival)
tsortedk = kNearestNeighborClassifier(3, tpsex, tpage, tpclass, tsex, tage, teclass, tsurvival)
tcentroids = select(2)
tassignments =assign(2, tage, tsex, teclass, tcentroids)
tcentroids = update(2, tage, tsex, teclass, tassignments)
tfinal_centroids, tfinal_assignments = iterate(2, tage, tsex, teclass)
t2nearest_class, tmin2 = nearestNeighborTPC(tpsex, tpage, tpclass, tfinal_centroids, tsurvival)
```
This chunk of code shows the Titanic as an example. It uses **calculateDistanceArray, nearestNeighborClassifier, kNearestNeighborClassifier, select, assign, update, iterate**, and a modified version of nearestNeighbor called **nearestNeighborTPC** (which also calls a modified version of calculateDistanceArray). As initial arguments, many of these functions take the sex, age and class of the test point (tpsex, tpage, tpclass), and the sex, age, class, and survival(fate of passenger) arrays of the members onboard for each ship (tsurvival, nsurvival, gsurvival, as examples). Eventually, centroids and assignments are created and updated through k-means clustering until getting to a point of higher accuracy. The end result is k final centroids and an array of final assignments, which are used to get the survival value for the test point in **nearestNeighborTPC**. 

## File List
Data files (all in the data folder):
- norge.csv
- titanic.csv
- goldengate.csv
- lusitania.csv

Function file:
- Final_Project.py

Main code:
- main.py

## Features
We used techniques including importing and translating data from csv files, using nearest neighbor classification and 3D k-means clustering, graphing on a 3D plot, and analyzing the data. 
## Useful Links
You can find more information about the background and statistics of the historical maritime disasters we used for our datasets at the links below.

- [Golden Gate background](http://www.aquaticsportsadventures.com/Articles/Misc/SSGoldenGate/SSGoldenGate.html)
- [Titanic facts and statistics](https://www.ultimatetitanic.com/facts-statistics/)
- [Norge background](http://www.norwayheritage.com/articles/templates/great-disasters.asp?articleid=119&zoneid=1)

