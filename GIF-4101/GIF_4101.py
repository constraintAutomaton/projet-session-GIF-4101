import numpy as np
import pandas as pd
import torch
import os


Liste_electionR = ["2004R","2006R","2008R","2011R","2015R"]
#suivre annee par un "R" 
#Retourne nom du district, Affiliation du candidat et son pourcentage
def Loader_resultats(Annee):
    dir = os.getcwd() + '\Data\Results.xlsx'
    df = pd.read_excel(dir,sheet_name=Annee)
    df = df.drop(df.columns[[0, 2, 3, 5,6]], axis=1)
    df["Year"] = Annee
    return df
dir  = Loader_resultats("2015R")
dir = dir.append(Loader_resultats("2011R"),sort=True,ignore_index=True)
print(dir.describe(include=['object', 'bool']))
print(dir.head())