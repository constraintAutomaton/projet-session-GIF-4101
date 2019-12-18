import pickle
import pandas as pd
import os
from Visualisation_data import *
dataFile = outputFile = os.path.join("Data","data.p")
data = None
with open(dataFile, "rb") as input_file:
    data = pickle.load(input_file)

visualisation()
#X,y = (data,)
