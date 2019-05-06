# Maritime Disaster Survival Rate Analysis

Our project analyzes the crew and passenger lists from three different historical maritime disasters (The SS Norge, Golden Gate, and Titanic sinking), graphs the data on 3D plots, and tells you whether or not an individual will survive given a specific age, sex, and class.

## Instructions

- Run the main.py file to start the program. 
- When prompted, answer the questions regarding sex, age, and social class. 
- The file will take this information and ultimately return a predicted fate based on statistics from each of the maritime distasters we used. It will also graph the data. The graphs plot each datapoint and color-code: red if they didn't survive, green if they did. There is overlap that can make it difficult to see multiple points at one point in space, which we tried to improve a bit by lowering the opacity of each dot.
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
This chunk of code shows the Titanic as an example. It uses *calculateDistanceArray, nearestNeighborClassifier, kNearestNeighborClassifier, select, assign, update, iterate*, and a modified version of nearestNeighbor called *nearestNeighborTPC* (which also calls a modified version of calculateDistanceArray). As initial arguments, many of these functions take the **sex, age** and **class** of the test point (**tpsex, tpage, tpclass**), and the **sex, age, class**, and **survival** (fate of passenger) arrays of the members onboard for each ship (**tsurvival, nsurvival, gsurvival**, as examples). Eventually, **centroids** and **assignments** are created and updated through k-means clustering until getting to a point of higher accuracy. The end result is k **final_centroids** and an array of **final_assignments**, which are used to get the survival value for the test point in *nearestNeighborTPC*. 

## File List
Data files (all in the data folder):
- norge.csv
- titanic.csv
- goldengate.csv

Function file:
- Final_Project.py

Code demonstration file:
- main.py

## Features
We used techniques including importing and translating data from csv files, using nearest neighbor classification and 3D k-means clustering, graphing on a 3D plot, and analyzing the data. The main file imports all the functions listed in the functions file and runs them in a way that makes sense. The main file also plots the data from the CSV files, and tells the user whether they would survive a certain disaster or not.
## Useful Links
You can find some more information about the background and statistics of the historical maritime disasters we used for our datasets at the links below.

- [Golden Gate background](http://www.aquaticsportsadventures.com/Articles/Misc/SSGoldenGate/SSGoldenGate.html)
- [Titanic facts and statistics](https://www.ultimatetitanic.com/facts-statistics/)
- [Norge background](http://www.norwayheritage.com/articles/templates/great-disasters.asp?articleid=119&zoneid=1)
- [An article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3421183/) written based off of the datasets where we got our data

More information on the data we used: file:///C:/Users/User/Downloads/1207156109_sapp.pdf

