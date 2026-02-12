import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ------------------ VARIABLES GLOBALES ------------------

df_global = None  # Stocke le DataFrame chargé


# ------------------ FONCTIONS ------------------

def charger_csv():
    global df_global

    chemin_csv = filedialog.askopenfilename(
        title="Sélectionner un fichier CSV",
        filetypes=[("Fichiers CSV", "*.csv")]
    )

    if not chemin_csv:
        return

    try:
        df = pd.read_csv(chemin_csv, sep=';')
        df.columns = df.columns.str.strip()
        df_global = df
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lecture CSV : {e}")
        return

    initialiser_listes_variables()


def initialiser_listes_variables():
    """
    Initialise les menus déroulants après chargement du CSV
    """

    global df_global

    if df_global is None:
        return

    # 🔹 Colonnes catégorielles (pour X)
    colonnes_categorielles = []

    # 🔹 Colonnes numériques (pour Y)
    colonnes_numeriques = []

    combo_x["values"] = colonnes_categorielles
    combo_y["values"] = colonnes_numeriques

    if colonnes_categorielles:
        combo_x.current(0)

    if colonnes_numeriques:
        combo_y.current(0)


def afficher_graphique():
    global df_global

    if df_global is None:
        messagebox.showwarning("Attention", "Chargez un fichier CSV d'abord.")
        return

    colonne_x = x_var.get()
    colonne_y = y_var.get()

    if not colonne_x or not colonne_y:
        messagebox.showwarning("Attention", "Sélectionnez les variables.")
        return

    df = df_global.copy()

    # Conversion numérique sécurisée
    df[colonne_y] = pd.to_numeric(df[colonne_y], errors="coerce")
    df = df.dropna(subset=[colonne_x, colonne_y])

    # Groupby (moyenne par défaut)
    df_grouped = df.groupby(colonne_x)[colonne_y].mean().reset_index()

    # Nettoyage ancien graphique
    for widget in frame_graphique.winfo_children():
        widget.destroy()

    # Création figure
    fig = Figure(figsize=(8, 4), dpi=100)
    ax = fig.add_subplot(111)

    type_g = type_graphique.get()

    if type_g == "line":
        ax.plot(df_grouped[colonne_x], df_grouped[colonne_y], marker="o")
    elif type_g == "bar":
        ax.bar(df_grouped[colonne_x], df_grouped[colonne_y], color="skyblue")
    elif type_g == "scatter":
        ax.scatter(df_grouped[colonne_x], df_grouped[colonne_y], color="red")

    ax.set_title(f"Moyenne {colonne_y} par {colonne_x}")
    ax.set_xlabel(colonne_x)
    ax.set_ylabel(f"Moyenne {colonne_y}")
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)

    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=frame_graphique)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


# ------------------ INTERFACE ------------------

root = tk.Tk()
root.title("Analyse des lycées")
root.geometry("1000x600")

frame_controles = ttk.Frame(root)
frame_controles.pack(pady=10)

# Bouton charger CSV
ttk.Button(
    frame_controles,
    text="Charger un CSV",
    command=charger_csv
).pack(side=tk.LEFT, padx=10)


# Variable X
x_var = tk.StringVar()
ttk.Label(frame_controles, text="Variable X :").pack(side=tk.LEFT, padx=5)
combo_x = ttk.Combobox(frame_controles, textvariable=x_var, state="readonly", width=18)
combo_x.pack(side=tk.LEFT, padx=5)

# Variable Y
y_var = tk.StringVar()
ttk.Label(frame_controles, text="Variable Y :").pack(side=tk.LEFT, padx=5)
combo_y = ttk.Combobox(frame_controles, textvariable=y_var, state="readonly", width=18)
combo_y.pack(side=tk.LEFT, padx=5)

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
ttk.Button(
    frame_controles,
    text="Afficher graphique",
    command=afficher_graphique
).pack(side=tk.LEFT, padx=10)


# Frame graphique
frame_graphique = ttk.Frame(root)
frame_graphique.pack(fill=tk.BOTH, expand=True)

root.mainloop()