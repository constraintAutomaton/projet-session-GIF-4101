
import pickle
import pandas as pd
import os
def visualisation():
    dataFile = outputFile = os.path.join("Data","data.p")
    data = None
    with open(dataFile, "rb") as input_file:
        data = pickle.load(input_file)
    print(data)
    dt = data.iloc[:,[1,2,3,8,9,10,11]]
    result = data.iloc[:,[1,2,3,8,9,10,11]]
    for col in data.columns:
        print(col)
    for i in data.dtypes:
        print(i)
    return 0

