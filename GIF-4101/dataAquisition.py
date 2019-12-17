
# coding=utf-8

import pandas as pd
import os
from pytrends.request import TrendReq
import pickle
from circonscription import listCirconscription as lc

# pour connection pytrend
pytrends = TrendReq(hl='en-US', tz=360)

Liste_electionR = ["2004R", "2006R", "2008R", "2011R", "2015R"]
# keywords
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

# [Libéral, Conservateur, NPD, Bloc Québécois]
Chef2004 = ['Paul Martin', 'Stephen Harper', 'Jack Layton', 'Gilles Duceppe']
Chef2006 = ['Paul Martin', 'Stephen Harper', 'Jack Layton', 'Gilles Duceppe']
Chef2008 = ['Stéphane Dion', 'Stephen Harper', 'Jack Layton', 'Gilles Duceppe']
Chef2011 = ['Michael Ignatieff', 'Stephen Harper',
            'Jack Layton', 'Gilles Duceppe']
Chef2015 = ['Justin Trudeau', 'Stephen Harper',
            'Thomas Mulcair', 'Gilles Duceppe']
Chefs = [Chef2004, Chef2006, Chef2008, Chef2011, Chef2015]

# période de la date des élections à 1 mois avant
Periodes = ['2004-05-28 2004-06-28', '2005-12-23 2006-01-23',
            '2008-09-14 2008-10-14', '2011-04-11 2011-05-11', '2015-09-19 2015-10-19']


Province_data_to_trend = {
    "Newfoundland and Labrador/Terre-Neuve-et-Labrador": "Newfoundland and Labrador",
    "Prince Edward Island/Île-du-Prince-Édouard": "Prince Edward Island",
    "Nova Scotia/Nouvelle-Écosse": "Nova Scotia",
    "New Brunswick/Nouveau-Brunswick": "New Brunswick",
    "Quebec/Québec": "Québec",
    "Ontario": "Ontario",
    "Manitoba": "Manitoba",
    "Saskatchewan": "Saskatchewan",
    "Alberta": "Alberta",
    "British Columbia/Colombie-Britannique": "British Columbia",
    "Yukon": "Yukon Territory",
    "Northwest Territories/Territoires du Nord-Ouest": "Northwest Territories",
    "Nunavut": "Nunavut"}


# suivre annee par un "R"
# Retourne nom du district, Affiliation du candidat et son pourcentage
    
def Loader_resultats(Annee):
    dir = os.path.join("Data", "Resultats_uniformes.xlsx")
    df = pd.read_excel(dir, sheet_name=Annee)
    df = df.drop(df.columns[[3]], axis=1)
    df["Year"] = Annee
    return df

# obtenir les data en lien avec les keyword
# parametre sont la liste de keyword et la periode d'interet sous la forme 'yyyy-mm-dd yyyy-mm-dd'
# alexandre : je vais cleaner le data dans la fonction


def Loader_Google_Trend(keyword, periode):
    pytrends.build_payload(keyword, cat=0, timeframe=periode, geo='CA')
    df = pytrends.interest_by_region(
        resolution='REGION', inc_low_vol=True, inc_geo_code=False)
    return df


def get_info(annees, chefs, periodes):
    listProvince = ['Newfoundland and Labrador/Terre-Neuve-et-Labrador',
                    'Prince Edward Island/Île-du-Prince-Édouard',
                    'Nova Scotia/Nouvelle-Écosse', 'New Brunswick/Nouveau-Brunswick',
                    'Quebec/Québec', 'Ontario', 'Manitoba', 'Saskatchewan', 'Alberta',
                    'British Columbia/Colombie-Britannique', 'Yukon',
                    'Northwest Territories/Territoires du Nord-Ouest', 'Nunavut'
                    ]
    listCirconscription = lc

    data = pd.DataFrame(columns=["Annee", "Province", "Circonscription", "Trend chef parti libéral",
                                 "Trend chef parti conservateur", "Trend chef parti npd", "Trend chef parti bloc quebecois",
                                 "Pourcentage vote parti liberal", "Pourcentage vote parti conservateur",
                                 "Pourcentage vote parti npd", "Pourcentage vote parti bloc quebecois"])
    compteur = 0

    for i in range(len(annees)):
        resultats = Loader_resultats(annees[i])
        annee = annees[i]

        trend_chefs_parti = Loader_Google_Trend(chefs[i], periodes[i])

        vote_npd = 0
        vote_bloc = 0
        vote_liberal = 0
        vote_conservateur = 0
        circonscription_precedente = ""

        allo = 0

        for j in range(len(resultats)):
            try:
                circonscription = listCirconscription.index(resultats.iloc[j]["Electoral District Name/Nom de circonscription"])
            except ValueError:
                circonscription = -1


            if circonscription != circonscription_precedente and isinstance(circonscription, str):

                if j != 0:
                    allo += 1
                    province = listProvince.index(
                        resultats.iloc[j-1]["Province"])

                    trend_province_value = Province_data_to_trend[resultats.iloc[j-1]["Province"]]
                    trend_chef_liberal = trend_chefs_parti.loc[trend_province_value][chefs[i][0]]
                    trend_chef_conservateur = trend_chefs_parti.loc[trend_province_value][chefs[i][1]]
                    trend_chef_npd = trend_chefs_parti.loc[trend_province_value][chefs[i][2]]
                    trend_chef_bloc = trend_chefs_parti.loc[trend_province_value][chefs[i][3]]

                    data.loc[compteur] = [annee, province, circonscription_precedente, trend_chef_liberal, trend_chef_conservateur,
                                          trend_chef_npd, trend_chef_bloc, vote_liberal, vote_conservateur, vote_npd, vote_bloc]

                    compteur += 1

            if resultats.iloc[j]["Affiliation"] == "Libéral":
                vote_liberal = resultats.iloc[j]["Percentage of Votes Obtained /Pourcentage des votes obtenus"]
            elif resultats.iloc[j]["Affiliation"] == "conservateur":
                vote_conservateur = resultats.iloc[j]["Percentage of Votes Obtained /Pourcentage des votes obtenus"]
            elif resultats.iloc[j]["Affiliation"] == "N.P.D." or resultats.iloc[j]["Affiliation"] == "NPD-Nouveau Parti démocratique":
                vote_npd = resultats.iloc[j]["Percentage of Votes Obtained /Pourcentage des votes obtenus"]
            elif resultats.iloc[j]["Affiliation"] == "Bloc Québécois":
                vote_bloc = resultats.iloc[j]["Percentage of Votes Obtained /Pourcentage des votes obtenus"]

            circonscription_precedente = circonscription

            if j == len(resultats) - 1 and isinstance(circonscription, int):
                allo += 1
                province = resultats.iloc[j]["Province"]

                trend_province_value = Province_data_to_trend[province]
                trend_chef_liberal = trend_chefs_parti.loc[trend_province_value][chefs[i][0]]
                trend_chef_conservateur = trend_chefs_parti.loc[trend_province_value][chefs[i][1]]
                trend_chef_npd = trend_chefs_parti.loc[trend_province_value][chefs[i][2]]
                trend_chef_bloc = trend_chefs_parti.loc[trend_province_value][chefs[i][3]]

                data.loc[compteur] = [annee, province, circonscription_precedente, trend_chef_liberal, trend_chef_conservateur,
                                      trend_chef_npd, trend_chef_bloc, vote_liberal, vote_conservateur, vote_npd, vote_bloc]

                compteur += 1
    return data


data = get_info(Liste_electionR, Chefs, Periodes)
outputFile = os.path.join("Data", "data.p")
with open(outputFile, 'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
