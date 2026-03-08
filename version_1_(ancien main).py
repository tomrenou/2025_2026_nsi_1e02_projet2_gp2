#main(code principal)



texte_bienevnue = "Bienvenue chez Lycée & So, le site qui rend l'analyse des lycées beaucoup plus simple !"

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import controller  # fichier controller.py avec la fonction afficher_graphique


# Application Lycée & So
class AppLycee:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Lycée & So")
        self.fenetre.geometry("900x500")

        self.data = None  # ici on stockera le DataFrame Pandas

        # Zone de contrôle en haut
       
        zone_haut = tk.Frame(fenetre)
        zone_haut.pack(pady=10)

        # Bouton ouvrir CSV
        bouton_fichier = tk.Button(
            zone_haut,
            text="Ouvrir un fichier CSV",
            command=self.ouvrir_fichier
        )
        bouton_fichier.pack(side=tk.LEFT, padx=10)

        # Filtre région
        tk.Label(zone_haut, text="Région :").pack(side=tk.LEFT)
        self.choix_region = tk.StringVar()
        self.liste_regions = ttk.Combobox(
            zone_haut,
            textvariable=self.choix_region,
            state="readonly",
            width=20
        )
        self.liste_regions.pack(side=tk.LEFT, padx=5)
        self.liste_regions.bind(
            "<<ComboboxSelected>>",
            lambda e: self.filtrer()
        )

        # Boutons stats et graphique
        bouton_stats = tk.Button(
            zone_haut,
            text="Voir statistiques",
            command=self.stats
        )
        bouton_stats.pack(side=tk.LEFT, padx=10)

        bouton_graph = tk.Button(
            zone_haut,
            text="Voir graphique",
            command=self.graphique
        )
        bouton_graph.pack(side=tk.LEFT, padx=10)

        # Tableau affichage données
        
        self.table = ttk.Treeview(fenetre)
        self.table.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Ouvrir fichier CSV

    def ouvrir_fichier(self):
        fichier = filedialog.askopenfilename(
            title="Choisir un fichier CSV",
            filetypes=[("Fichier CSV", "*.csv")]
        )

        if not fichier:
            return

        try:
            self.data = pd.read_csv(fichier)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible d'ouvrir le fichier\n{e}")
            return

        # Nettoyage simple
        self.data = self.data.drop_duplicates()

        # Liste des régions
        if "region" in self.data.columns:
            regions = sorted(self.data["region"].dropna().unique())
            self.liste_regions["values"] = ["Toutes"] + list(regions)
            self.liste_regions.current(0)

        # Affichage dans le tableau
        self.afficher_table(self.data)

    # Filtrage par région
    
    def filtrer(self):
        if self.data is None:
            return

        region = self.choix_region.get()
        if region == "Toutes":
            data_filtre = self.data
        else:
            data_filtre = self.data[self.data["region"] == region]

        self.afficher_table(data_filtre)

    # Affichage du tableau

    def afficher_table(self, data):
        self.table.delete(*self.table.get_children())
        self.table["columns"] = list(data.columns)
        self.table["show"] = "headings"

        for col in data.columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=120)

        for _, ligne in data.iterrows():
            self.table.insert("", tk.END, values=list(ligne))

    # Statistiques

    def stats(self):
        if self.data is None:
            return

        if "taux_reussite" not in self.data.columns:
            messagebox.showwarning(
                "Attention",
                "Il n'y a pas de colonne 'taux_reussite'"
            )
            return

        moyenne = self.data["taux_reussite"].mean()
        messagebox.showinfo(
            "Statistiques",
            f"Taux de réussite moyen : {moyenne:.2f} %"
        )

    # Graphique
    
    def graphique(self):
        if self.data is None:
            messagebox.showwarning("Attention", "Aucune donnée à afficher")
            return

        if "region" not in self.data.columns or "taux_reussite" not in self.data.columns:
            messagebox.showwarning(
                "Attention",
                "Colonnes nécessaires : region, taux_reussite"
            )
            return

        # On envoie les données au contrôleur
        controller.afficher_graphique(self.fenetre, self.data)

# Lancement du programme

if __name__ == "__main__":
    fenetre = tk.Tk()
    app = AppLycee(fenetre)
    fenetre.mainloop()
