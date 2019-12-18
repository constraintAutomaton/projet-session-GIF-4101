import pandas as pd
import os
from pytrends.request import TrendReq
import pickle
import numpy as np
import matplotlib
matplotlib.rcParams['figure.figsize'] = (17.0, 35.0)
from matplotlib import pyplot


dataFile = outputFile = os.path.join("Data","data.p")
data = None
with open(dataFile, "rb") as input_file:
    data = pickle.load(input_file)
data = data.dropna()

pairs = [(3,4),(3,5),(3,6),(3,11),(3,12),(3,13),(3,14),(4,5),(4,6),(4,11),(4,12),(4,13),(4,14),(5,6),(5,11),(5,12),(5,13),(5,14)
        ,(6,11),(6,12),(6,13),(6,14),(11,12),(11,13),(11,14),(12,13),(12,14),(13,14)]
col = []

for i in range(len(data)):
    maxi = max(data.iloc[i,7],data.iloc[i,8],data.iloc[i,9],data.iloc[i,10])
    if maxi == data.iloc[i,7]:
        col.append(1)
    elif maxi == data.iloc[i,8]:
        col.append(2)
    elif maxi == data.iloc[i,9]:
        col.append(3)
    elif maxi == data.iloc[i,10]:
        col.append(4)

fig, subfigs = pyplot.subplots(7, 4, tight_layout=True)

for (f1, f2), subfig in zip(pairs, subfigs.reshape(-1)):
    X = data.iloc[:,[f1,f2]]
    subfig.scatter(X.iloc[:, 0], X.iloc[:, 1], c=col)
    subfig.set_xlabel(list(data)[f1])
    subfig.set_ylabel(list(data)[f2])
    pass
