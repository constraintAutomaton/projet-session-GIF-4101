import numpy as np
import pandas as pd
import torch
import os
from pytrends.request import TrendReq

#pour connection pytrend
pytrends = TrendReq(hl='en-US', tz=360)

Liste_electionR = ["2004R","2006R","2008R","2011R","2015R"]
# keywords
ENVF = ['ges','rechauffement climatique','pollution','changement climatique','problèmes environnementaux']
ENVE = ['global warming','pollution','climate change','sustainability','environmental issues']
SANF = ['assurance maladie','passeport santé','santé','ministre de la santé','info santé']
SANE = ['fitness','nutrition','healthcare','health insurance','healthy food']
EDUF = ['école','université','enseignement supérieur','école publique','diplôme']
EDUE = ['school','university','degree','higher education','ministry of education']
ECOF = ['économie','taxe','impôt progressif','impôt','gain en capital']
ECOE = ['tax','tax return','income tax','accountant','economy']
IMMF = ['immigration','immigration canada','citoyenneté','visa','test citoyenneté']
IMME = ['immigration','immigration canada','citizenship','visa','canadian citizenship']
POLF = ['élections','parti politique','débat','actualités','actualités france']
POLE = ['election','democracy','r politics','cnn politics','political spectrum']



#suivre annee par un "R" 
#Retourne nom du district, Affiliation du candidat et son pourcentage
def Loader_resultats(Annee):
    dir = os.getcwd() + '\Data\Results.xlsx'
    df = pd.read_excel(dir,sheet_name=Annee)
    df = df.drop(df.columns[[0, 2, 3, 5,6]], axis=1)
    df["Year"] = Annee
    return df

#obtenir les data en lien avec les keyword 
#parametre sont la liste de keyword et la periode d'interet sous la forme 'yyyy-mm-dd yyyy-mm-dd'
#alexandre : je vais cleaner le data dans la fonction
def Loader_Google_Trend(keyword,periode):
    pytrends.build_payload(keyword, cat=0, timeframe=periode, geo='CA')
    df = pytrends.interest_by_region(resolution = 'REGION', inc_low_vol=True, inc_geo_code=False)
    print(envifr)
    return df



