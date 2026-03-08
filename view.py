import tkinter as tk
from tkinter import ttk
from controller import *

def lancer_interface():
    root = tk.Tk()
    root.title("Analyse des lycées")
    root.geometry("1000x600")

    frame_controles = ttk.Frame(root)
    frame_controles.pack(pady=10)

    # Variable X
    x_var = tk.StringVar()
    ttk.Label(frame_controles, text="Variable X :").pack(side=tk.LEFT, padx=5)
    combo_x = ttk.Combobox(frame_controles, textvariable=x_var, state="readonly", width=18)
    combo_x.pack(side=tk.LEFT, padx=5)
    combo_x["values"] = ["academie", "code_departement", "departement","nom_commune","secteur","type_lycee"]
    combo_x.current(0)

    ttk.Button(frame_controles, text="Filtrer X", command=lambda: ouvrir_filtre(root, x_var.get())).pack(side=tk.LEFT, padx=5)

    # Variable Y
    y_var = tk.StringVar()
    ttk.Label(frame_controles, text="Variable Y :").pack(side=tk.LEFT, padx=5)
    combo_y = ttk.Combobox(frame_controles, textvariable=y_var, state="readonly", width=18)
    combo_y.pack(side=tk.LEFT, padx=5)
    combo_y["values"] = ["IPS_voie_GT","IPS_voie_PRO","IPS_ensemble_GT-PRO"]
    combo_y.current(0)

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

    # Bouton afficher
    ttk.Button(frame_controles, text="Afficher graphique",
               command=lambda: afficher_graphique(frame_graphique, x_var.get(), y_var.get(), type_graphique.get())
               ).pack(side=tk.LEFT, padx=10)

    # Frame graphique
    frame_graphique = ttk.Frame(root)
    frame_graphique.pack(fill=tk.BOTH, expand=True)

    # Export CSV / Excel
    ttk.Button(frame_controles, text="Exporter graphique (.csv ou .xlsx)",
               command=lambda: exporter_donnees_graphique(x_var.get(), y_var.get())
               ).pack(side=tk.LEFT, padx=10)

    # Export image
    ttk.Button(frame_controles, text="Exporter graphique (image)",
               command=exporter_graphique
               ).pack(side=tk.LEFT, padx=10)

    # Fenêtre bienvenue (si tu l’as)
    try:
        from fenetre_bienvenue import fenetre_bienvenue
        fenetre_bienvenue(root)
    except:
        pass

    # Charger CSV
    charger_csv()

    root.mainloop()