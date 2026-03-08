import tkinter as tk
from tkinter import ttk
from controller import *

def lancer_interface():
    "Crée la fenêtre principale, configure les widgets, les boutons et lance l'application Tkinter."
    "C’est le point d’entrée de l’interface graphique et permet à l’utilisateur d’interagir avec les données."
    root = tk.Tk()
    root.title("Analyse des lycées")
    root.geometry("1000x600")
    "Initialise la fenêtre principale avec un titre et une taille fixe."

    frame_controles = ttk.Frame(root)
    frame_controles.pack(pady=10)
    "Contient tous les widgets de contrôle (combobox, boutons, type de graphique) en haut de la fenêtre."

    # Variable X
    x_var = tk.StringVar()
    ttk.Label(frame_controles, text="Variable X :").pack(side=tk.LEFT, padx=5)
    combo_x = ttk.Combobox(frame_controles, textvariable=x_var, state="readonly", width=18)
    combo_x.pack(side=tk.LEFT, padx=5)
    combo_x["values"] = ["academie", "code_departement", "departement","nom_commune","secteur","type_lycee"]
    combo_x.current(0)
    "Permet à l’utilisateur de choisir la colonne X (catégorielle) pour le graphique."

    ttk.Button(frame_controles, text="Filtrer X", command=lambda: ouvrir_filtre(root, x_var.get())).pack(side=tk.LEFT, padx=5)
    "Bouton qui ouvre la fenêtre de filtre pour la colonne X sélectionnée."

    # Variable Y
    y_var = tk.StringVar()
    ttk.Label(frame_controles, text="Variable Y :").pack(side=tk.LEFT, padx=5)
    combo_y = ttk.Combobox(frame_controles, textvariable=y_var, state="readonly", width=18)
    combo_y.pack(side=tk.LEFT, padx=5)
    combo_y["values"] = ["IPS_voie_GT","IPS_voie_PRO","IPS_ensemble_GT-PRO"]
    combo_y.current(0)
    "Permet à l’utilisateur de choisir la colonne Y (numérique) pour le graphique."

    # Type graphique
    type_graphique = tk.StringVar(value="bar")
    ttk.Label(frame_controles, text="Type :").pack(side=tk.LEFT, padx=5)
    ttk.Combobox(
        frame_controles,
        textvariable=type_graphique,
        values=["bar", "line", "scatter"],
        state="readonly",
        width=10
    ).pack(side=tk.LEFT, padx=5)
    "Permet de choisir le type de graphique (barres, ligne, scatter)."
    
    # Bouton afficher
    ttk.Button(frame_controles, text="Afficher graphique",
               command=lambda: afficher_graphique(frame_graphique, x_var.get(), y_var.get(), type_graphique.get())
               ).pack(side=tk.LEFT, padx=10)
    "Bouton qui génère et affiche le graphique selon les variables et le type choisis."

    # Frame graphique
    frame_graphique = ttk.Frame(root)
    frame_graphique.pack(fill=tk.BOTH, expand=True)
    "Zone où le graphique sera affiché et mis à jour dynamiquement."

    # Export CSV / Excel
    ttk.Button(frame_controles, text="Exporter graphique (.csv ou .xlsx)",
               command=lambda: exporter_donnees_graphique(x_var.get(), y_var.get())
               ).pack(side=tk.LEFT, padx=10)
    "Permet d’exporter les données filtrées et groupées utilisées pour le graphique."

    # Export image
    ttk.Button(frame_controles, text="Exporter graphique (image)",
               command=exporter_graphique
               ).pack(side=tk.LEFT, padx=10)
    "Permet de sauvegarder le graphique affiché au format JPG ou PNG."

    # Fenêtre bienvenue (si tu l’as)
    try:
        from fenetre_bienvenue import fenetre_bienvenue
        fenetre_bienvenue(root)
    except:
        pass
    "Affiche la fenêtre de bienvenue avant l’accès à l’interface principale si le fichier existe."

    # Charger CSV
    charger_csv()
    "Charge le fichier CSV des lycées et prépare les listes pour les combobox X et Y."

    root.mainloop()
    "Démarre la boucle principale Tkinter pour rendre l'interface interactive."