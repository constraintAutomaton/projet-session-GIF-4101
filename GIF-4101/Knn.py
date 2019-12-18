import pandas as pd
import os
from pytrends.request import TrendReq
import pickle
import numpy as np
import matplotlib
matplotlib.rcParams['figure.figsize'] = (5.0, 5.0)
from matplotlib import pyplot
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing





dataFile = outputFile = os.path.join("Data","data.p")
data = None
with open(dataFile, "rb") as input_file:
    data = pickle.load(input_file)
data = data.dropna()

for i in range(len(data)):
    maxi = max(data.iloc[i,7],data.iloc[i,8],data.iloc[i,9],data.iloc[i,10])
    if maxi == data.iloc[i,7]:
        col.append("Black")
    elif maxi == data.iloc[i,8]:
        col.append("Red")
    elif maxi == data.iloc[i,9]:
        col.append("Blue")
    elif maxi == data.iloc[i,10]:
        col.append("Green")

  
X = data.iloc[:,[3,4,5,6,11,12,13,14]]  

X = preprocessing.minmax_scale(X)


y = np.zeros(np.shape(X)[0])

scoresUniformWeights = []
scoresDistanceWeights = []
for i in range(len(data)):
    maxi = max(data.iloc[i,7],data.iloc[i,8],data.iloc[i,9],data.iloc[i,10])
    if maxi == data.iloc[i,7]:
        y[i] = 1
    elif maxi == data.iloc[i,8]:
        y[i] = 2
    elif maxi == data.iloc[i,9]:
        y[i] = 3
    elif maxi == data.iloc[i,10]:
        y[i] = 4

    
k = [1,3,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
N =np.shape(X)[0]
for i in k:
    Avs = 0
    RPK = KFold(n_splits=N)
    for train,test in RPK.split(y):
        Data_train,target_train = X[train,:],y[train]
        Data_test,target_test = X[test,:],y[test]
        knn = KNeighborsClassifier(n_neighbors=i, weights="uniform")
        knn.fit(Data_train,target_train)
        Avs +=knn.score(Data_test,target_test)
    scoresUniformWeights.append(Avs/N)

    


for i in k:
    Avs=0
    RPK = KFold(n_splits=N)
    for train,test in RPK.split(y):
        Data_train,target_train = X[train,:],y[train]
        Data_test,target_test = X[test,:],y[test]
        knn = KNeighborsClassifier(n_neighbors=i, weights="distance")
        knn.fit(Data_train,target_train)
        Avs +=knn.score(Data_test,target_test)
    scoresDistanceWeights.append(Avs/N) 
print(scoresUniformWeights)
print(scoresDistanceWeights)

pyplot.plot(np.array(k),np.array(scoresUniformWeights),label= "Uniform")
pyplot.plot(np.array(k),np.array(scoresDistanceWeights),label = "Distance")
pyplot.legend()
pyplot.show()
