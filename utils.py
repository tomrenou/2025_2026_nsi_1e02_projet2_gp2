import pandas as pd

def make_data_frame_from_csv(csv_file):
    df = pd.read_csv('data.csv') 
    return df

def get_code_departement(lycees,nom_etablissment):
    code_departement = lycees[nom_etablissment]
    return code_departement

def get_académie(lycees,Nom de l'etablissment):
    ...
    return academie

def get_année_scolaire(lycees,Nom de l'etablissment):
    ...
    return Code du departement
