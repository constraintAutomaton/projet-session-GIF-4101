
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

ENVF = ['ges', 'rechauffement climatique', 'pollution',
        'changement climatique', 'problèmes environnementaux']
ENVE = ['global warming', 'pollution', 'climate change',
        'sustainability', 'environmental issues']
SANF = ['assurance maladie', 'passeport santé',
        'santé', 'ministre de la santé', 'info santé']
SANE = ['fitness', 'nutrition', 'healthcare',
        'health insurance', 'healthy food']
EDUF = ['école', 'université', 'enseignement supérieur',
        'école publique', 'diplôme']
EDUE = ['school', 'university', 'degree',
        'higher education', 'ministry of education']
ECOF = ['économie', 'taxe', 'impôt progressif', 'impôt', 'gain en capital']
ECOE = ['tax', 'tax return', 'income tax', 'accountant', 'economy']
IMMF = ['immigration', 'immigration canada',
        'citoyenneté', 'visa', 'test citoyenneté']
IMME = ['immigration', 'immigration canada',
        'citizenship', 'visa', 'canadian citizenship']
POLF = ['élections', 'parti politique',
        'débat', 'actualités', 'actualités france']
POLE = ['election', 'democracy', 'r politics',
        'cnn politics', 'political spectrum']
Liste_trend = [ENVF,ENVE,POLF,POLE,ECOF,ECOE,EDUF,EDUE,SANF,SANE,IMMF,IMME]

def get_Google_T(data,liste,periode):
    final = np.zeros()
    data['env'] = 0
    data['san'] = 0
    data['pol'] = 0
    data['eco'] = 0
    data['edu'] = 0
    liste1 = [liste[0][0],liste[2][0],liste[4][0],liste[6][0],liste[8][0]]
    liste2 = [liste[0][1],liste[2][1],liste[4][1],liste[6][1],liste[8][1]]
    liste3 = [liste[1][0],liste[3][0],liste[5][0],liste[7][0],liste[9][0]]
    liste4 = [liste[1][1],liste[3][1],liste[5][1],liste[7][1],liste[9][1]]
    listeGroupe = [liste1,liste2,liste3,liste4]
    for year in periode:
        total = np.zeros((13,5))
        for itt in listeGroupe:
            data1 = Loader_Google_Trend(itt, year)
            dtt = data1.to_numpy()
            total = np.add(dtt,total)
            total
        final = np.appre
    print(data.describe)
    return data
#X,y = (data,)