# Analyse des Lycées Français - Projet NSI 1ère

**Auteur : Tom Renou, Eliott Grougi et Esteban Gabilla**  
**Langage : Python**  
**Librairies : Pandas, Matplotlib, Tkinter**  
**Logiciels utilisés : Visual Studio Code, GitHub**  
**Date : 2025-2026**  
**Projet réalisé dans le cadre de la spécialité NSI 1ère**  

---

## Description du projet

Cette application permet de **visualiser, analyser et filtrer les données des lycées français** à partir d’un fichier CSV.  
Elle offre une interface graphique complète pour :

- Sélectionner les colonnes **X** (catégorielles) et **Y** (numériques).  
- Filtrer les données selon des critères spécifiques.  
- Générer des graphiques (**barres, lignes, scatter**).  
- Exporter les données filtrées (**CSV / Excel**).  
- Exporter les graphiques (**JPG / PNG**).  

L’objectif est de rendre l’analyse **simple, rapide et dynamique**, même pour de grands ensembles de données.

---

## Structure du projet

| Fichier | Description détaillée |
|---------|---------------------|
| `main.py` | Point d’entrée du programme. Initialise l’interface Tkinter, charge le CSV et connecte les boutons aux fonctions du controller. |
| `controller.py` | Contient toutes les fonctions de traitement des données : filtrage, groupement, conversion numérique, export CSV/Excel et génération de graphiques. |
| `view.py` | Interface graphique complète. Définit la disposition des widgets, boutons, combobox et la gestion de la fenêtre principale. |
| `fenetre_bienvenue.py` | Fenêtre d’introduction avant l’accès à l’interface principale. Permet à l’utilisateur de cliquer "Commencer". |
| `fr-en-ips_lycees.csv` | Fichier CSV contenant toutes les données des lycées : académies, départements, IPS, secteurs, etc. |
| `.gitignore` | Fichier pour ignorer les fichiers temporaires et caches (`__pycache__/`, exports CSV/Excel/images). |

---
