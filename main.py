from view import lancer_interface
"Importe la fonction qui crée et lance l'interface graphique complète depuis le fichier view.py."

if __name__ == "__main__":
<<<<<<< Updated upstream
    "Vérifie si ce fichier est exécuté directement et non importé par un autre module."

    lancer_interface()
    "Appelle la fonction qui démarre l'application Tkinter, affichant la fenêtre principale et tous les widgets."
=======
    fenetre = tk.Tk()
    app = AppLycee(fenetre)
    fenetre.mainloop()
>>>>>>> Stashed changes
