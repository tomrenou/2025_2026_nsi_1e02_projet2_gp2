import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog, messagebox , ttk

# Variables globales
df_global = None
fig_global = None
valeurs_filtre = None

# --- CSV ---
def charger_csv():
    global df_global
    chemin_csv = "fr-en-ips_lycees.csv"
    if not chemin_csv:
        return
    try:
        df = pd.read_csv(chemin_csv, sep=';')
        df.columns = df.columns.str.strip()
        df_global = df
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lecture CSV : {e}")

# --- Filtre ---
def ouvrir_filtre(root, colonne_x):
    global df_global, valeurs_filtre
    if df_global is None or not colonne_x:
        return

    fenetre = tk.Toplevel(root)
    fenetre.title("Filtrer les valeurs")

    valeurs = sorted(df_global[colonne_x].dropna().unique())
    liste = tk.Listbox(fenetre, selectmode="multiple", width=40, height=20)
    liste.pack(padx=10, pady=10)

    for v in valeurs:
        liste.insert(tk.END, v)

    def tout_selectionner():
        liste.select_set(0, tk.END)
    ttk.Button(fenetre, text="Tout sélectionner", command=tout_selectionner).pack(pady=5)

    def valider_filtre():
        global valeurs_filtre
        selection = liste.curselection()
        valeurs_filtre = [liste.get(i) for i in selection]
        fenetre.destroy()

    ttk.Button(fenetre, text="Valider", command=valider_filtre).pack(pady=10)

# --- Graphique ---
def afficher_graphique(frame_graphique, colonne_x, colonne_y, type_g):
    global df_global, fig_global, valeurs_filtre
    if df_global is None:
        messagebox.showwarning("Attention", "Chargez un fichier CSV d'abord.")
        return
    if not colonne_x or not colonne_y:
        messagebox.showwarning("Attention", "Sélectionnez les variables.")
        return

    df = df_global.copy()
    if valeurs_filtre:
        df = df[df[colonne_x].isin(valeurs_filtre)]
    df[colonne_y] = pd.to_numeric(df[colonne_y], errors="coerce")
    df = df.dropna(subset=[colonne_x, colonne_y])
    df_grouped = df.groupby(colonne_x)[colonne_y].mean().reset_index()

    for widget in frame_graphique.winfo_children():
        widget.destroy()

    fig = Figure(figsize=(8, 4), dpi=100)
    ax = fig.add_subplot(111)
    fig_global = fig

    if type_g == "line":
        ax.plot(df_grouped[colonne_x], df_grouped[colonne_y], marker="o")
    elif type_g == "bar":
        ax.bar(df_grouped[colonne_x], df_grouped[colonne_y], color="green")
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

# --- Export CSV / Excel ---
def exporter_donnees_graphique(colonne_x, colonne_y):
    global df_global
    if df_global is None:
        messagebox.showwarning("Attention", "Aucune donnée à exporter.")
        return
    if not colonne_x or not colonne_y:
        messagebox.showwarning("Attention", "Sélectionnez les variables X et Y avant d'exporter.")
        return

    df = df_global.copy()
    df[colonne_y] = pd.to_numeric(df[colonne_y], errors="coerce")
    df = df.dropna(subset=[colonne_x, colonne_y])
    df_grouped = df.groupby(colonne_x)[colonne_y].mean().reset_index()

    fichier = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")],
        title="Exporter les données filtrées"
    )
    if not fichier:
        return

    try:
        if fichier.endswith(".csv"):
            df_grouped.to_csv(fichier, index=False)
        elif fichier.endswith(".xlsx"):
            df_grouped.to_excel(fichier, index=False)
        messagebox.showinfo("Succès", f"Données exportées avec succès dans {fichier}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d'exporter : {e}")

# --- Export image ---
def exporter_graphique():
    global fig_global
    if fig_global is None:
        messagebox.showwarning("Attention", "Aucun graphique à exporter.")
        return
    fichier = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=[("JPG files", "*.jpg"), ("PNG files", "*.png")],
        title="Exporter le graphique"
    )
    if not fichier:
        return
    try:
        fig_global.savefig(fichier, dpi=300, bbox_inches="tight")
        messagebox.showinfo("Succès", f"Graphique exporté avec succès dans {fichier}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d'exporter le graphique : {e}")