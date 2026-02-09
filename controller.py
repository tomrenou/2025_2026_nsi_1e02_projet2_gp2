import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ------------------ FONCTIONS ------------------

def charger_csv(chemin_csv):
    """Charge un CSV et nettoie les noms de colonnes"""
    try:
        df = pd.read_csv(chemin_csv, sep=';')
        df.columns = df.columns.str.strip()
        return df
    except FileNotFoundError:
        messagebox.showerror("Erreur", f"Le fichier {chemin_csv} est introuvable.")
        return pd.DataFrame()
    except pd.errors.ParserError:
        messagebox.showerror("Erreur", "Erreur lors de la lecture du CSV.")
        return pd.DataFrame()

def creer_graphique_tkinter(parent, df, colonne_x, colonne_y, type_graphique="line",
                             titre="Graphique", xlabel="", ylabel=""):
    """Crée et affiche un graphique Matplotlib dans Tkinter"""
    
    if colonne_x not in df.columns or colonne_y not in df.columns:
        messagebox.showerror("Erreur", f"Colonnes '{colonne_x}' ou '{colonne_y}' introuvables.")
        return
    
    for widget in parent.winfo_children():
        widget.destroy()
    
    fig = Figure(figsize=(7, 4), dpi=100)
    ax = fig.add_subplot(111)
    
    if type_graphique == "line":
        ax.plot(df[colonne_x], df[colonne_y], marker='o')
    elif type_graphique == "bar":
        ax.bar(df[colonne_x], df[colonne_y], color='skyblue')
    elif type_graphique == "scatter":
        ax.scatter(df[colonne_x], df[colonne_y], color='red')
    
    ax.set_title(titre)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis='x', rotation=45)
    
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def afficher_graphique():
    """Sélection du CSV et affichage du graphique"""
    
    chemin_csv = filedialog.askopenfilename(
        title="Sélectionner un fichier CSV",
        filetypes=[("Fichiers CSV", "*.csv")]
    )
    if not chemin_csv:
        return
    
    df = charger_csv(chemin_csv)
    if df.empty:
        return
    
    # Colonnes à tracer (adapté à votre CSV)
    colonne_x = "IPS_voie_GT"
    colonne_y = "IPS_voie_PRO"
    
    creer_graphique_tkinter(
        frame_graphique,
        df,
        colonne_x=colonne_x,
        colonne_y=colonne_y,
        type_graphique=type_graphique.get(),
        titre=f"{colonne_x} vs {colonne_y}",
        xlabel=colonne_x,
        ylabel=colonne_y
    )

# ------------------ INTERFACE ------------------

root = tk.Tk()
root.title("Visualisation de données lycées")
root.geometry("900x600")

frame_controles = ttk.Frame(root)
frame_controles.pack(pady=10)

type_graphique = tk.StringVar(value="line")

ttk.Label(frame_controles, text="Type de graphique :").pack(side=tk.LEFT, padx=5)
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

frame_graphique = ttk.Frame(root)
frame_graphique.pack(fill=tk.BOTH, expand=True)

root.mainloop()