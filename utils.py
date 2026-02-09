import pandas as pd

def make_data_frame_from_csv(csv_file):
    df = pd.read_csv('data.csv') 
    return df

def get_code_departement(lycees, nom_etablissement):
    code_departement = lycees[nom_etablissement]
    return code_departement

def get_académie(lycees, nom_etablissement):
    academie = lycees[nom_etablissement]
    return academie

def get_rentree_scolaire(lycees, nom_etablissement):
    rentree_scolaire = lycees[nom_etablissement]
    return rentree_scolaire

def get_departement(lycees, nom_etablissement):
    departement = lycees[nom_etablissement]
    return departement

def get_code_INSEE_commune(lycees, nom_département):
    code_INSEE_commune = lycees[nom_etablissement]
    return code_INSEE_commune



