# Tkinter : interface graphique
import tkinter as tk
from tkinter import ttk

# Pandas : manipulation des données (CSV → DataFrame)
import pandas as pd

# Matplotlib : création des graphiques
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



# FONCTIONS DE DONNÉES


def charger_csv(chemin_csv):
    """
    Charge un fichier CSV et le convertit en DataFrame Pandas.
    Cette fonction joue le rôle de 'base de données'.
    """
    return pd.read_csv(chemin_csv)



# FONCTION DE CRÉATION DU GRAPHIQUE


def creer_graphique_tkinter(
    parent,
    df,
    colonne_x,
    colonne_y,
    type_graphique="line",
    titre="Graphique",
    xlabel="",
    ylabel=""
):
    """
    Crée et affiche un graphique Matplotlib dans une fenêtre Tkinter.

    parent        → Frame Tkinter qui contiendra le graphique
    df            → DataFrame Pandas (données)
    colonne_x/y   → Colonnes utilisées pour les axes
    type_graphique→ line / bar / scatter
    """

    # Supprime l'ancien graphique (permet la mise à jour)
    for widget in parent.winfo_children():
        widget.destroy()

    # Création de la figure Matplotlib
    fig = Figure(figsize=(7, 4), dpi=100)
    ax = fig.add_subplot(111)

    # Choix du type de graphique
    if type_graphique == "line":
        ax.plot(df[colonne_x], df[colonne_y])
    elif type_graphique == "bar":
        ax.bar(df[colonne_x], df[colonne_y])
    elif type_graphique == "scatter":
        ax.scatter(df[colonne_x], df[colonne_y])

    # Mise en forme du graphique
    ax.set_title(titre)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis='x', rotation=45)

    # Intégration du graphique dans Tkinter
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


# FONCTION LIÉE AU BOUTON


def afficher_graphique():
    """
    Fonction appelée quand l'utilisateur clique sur le bouton.
    Elle :
    1. Charge les données
    2. Appelle la fonction de création du graphique
    """

    df = charger_csv("donnees.csv")

    creer_graphique_tkinter(
        frame_graphique,
        df,
        colonne_x="date",
        colonne_y="ventes",
        type_graphique=type_graphique.get(),
        titre="Évolution des ventes",
        xlabel="Date",
        ylabel="Ventes"
    )


# INTERFACE GRAPHIQUE


# Création de la fenêtre principale
root = tk.Tk()
root.title("Visualisation de données CSV")
root.geometry("900x600")

# ----- Zone de contrôles -----
frame_controles = ttk.Frame(root)
frame_controles.pack(pady=10)

# Variable Tkinter pour stocker le type de graphique sélectionné
type_graphique = tk.StringVar(value="line")

ttk.Label(
    frame_controles,
    text="Type de graphique :"
).pack(side=tk.LEFT, padx=5)

ttk.Combobox(
    frame_controles,
    textvariable=type_graphique,
    values=["line", "bar", "scatter"],
    state="readonly",
    width=10
).pack(side=tk.LEFT, padx=5)

ttk.Button(
    frame_controles,
    text="Afficher le graphique",
    command=afficher_graphique
).pack(side=tk.LEFT, padx=10)

# ----- Zone d'affichage du graphique -----
frame_graphique = ttk.Frame(root)
frame_graphique.pack(fill=tk.BOTH, expand=True)

# Lancement de la boucle principale Tkinter
root.mainloop()