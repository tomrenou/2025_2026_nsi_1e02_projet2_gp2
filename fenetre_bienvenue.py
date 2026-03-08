import tkinter as tk
from tkinter import ttk

def fenetre_bienvenue(root):

    fenetre = tk.Toplevel(root)
    fenetre.grab_set()
    fenetre.title("Bienvenue")
    fenetre.geometry("500x300")

    frame = ttk.Frame(fenetre, padding=20)
    frame.pack(fill=tk.BOTH, expand=True)

    titre = ttk.Label(
        frame,
        text="Bienvenue dans l'application d'analyse des lycées",
        font=("Arial", 14, "bold")
    )
    titre.pack(pady=10)

    texte = """
1. Choisissez une variable X
2. Choisissez une variable Y
3. Sélectionnez un type de graphique
4. Cliquez sur 'Afficher graphique'
5. Puis cliquez sur 'Exporter données'
"""

    ttk.Label(frame, text=texte).pack(pady=10)

    ttk.Button(frame, text="Commencer", command=fenetre.destroy).pack(pady=10)

    root.wait_window(fenetre)