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

def get_code_INSEE_commune(lycees, nom_etablissement):
    code_INSEE_commune = lycees[nom_etablissement]
    return code_INSEE_commune

def get_nom_commune(lycees, nom_etablissement):
    nom_commune = lycees[nom_etablissement]
    return nom_commune

def get_secteur(lycees, nom_etablissement):
    secteur = lycees[nom_etablissement]
    return secteur

def get_type_lycee(lycees, nom_etablissement):
    type_lycee = lycees[nom_etablissement]
    return type_lycee

def get_IPS_voie_GT(lycees, nom_etablissement):
    IPS_voie_GT = lycees[nom_etablissement]
    return IPS_voie_GT

def get_IPS_voie_PRO(lycees, nom_etablissement):
    IPS_voie_PRO = lycees[nom_etablissement]
    return IPS_voie_PRO

def get_IPS_ensemble_GT_PRO(lycees, nom_etablissement):
    IPS_ensemble_GT_PRO = lycees[nom_etablissement]
    return IPS_ensemble_GT_PRO

def get_ecart_type_IPS_voie_GT(lycees, nom_etablissement):
    ecart_type_IPS_voie_GT = lycees[nom_etablissement]
    return ecart_type_IPS_voie_GT

def get_ecart_type_IPS_voie_PRO(lycees, nom_etablissement):
    ecart_type_IPS_voie_PRO = lycees[nom_etablissement]
    return ecart_type_IPS_voie_PRO



