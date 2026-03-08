````markdown
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
---

## Utilisation de l’interface

### Fenêtre de bienvenue

* Une fenêtre s’ouvre avant l’interface principale.
* L’utilisateur doit cliquer **Commencer** pour accéder à l’application.

---

### Sélection des variables

| Axe   | Type         | Exemples                                                                              |
| ----- | ------------ | ------------------------------------------------------------------------------------- |
| **X** | Catégorielle | `academie`, `code_departement`, `departement`, `nom_commune`, `secteur`, `type_lycee` |
| **Y** | Numérique    | `IPS_voie_GT`, `IPS_voie_PRO`, `IPS_ensemble_GT-PRO`                                  |

* Les colonnes X sont affichées dans une **combobox**.
* Les colonnes Y dans une autre combobox.
* Certaines colonnes X peuvent être **filtrées dynamiquement** via un bouton dédié.

---

### Filtrage des données

1. Sélectionner une colonne X filtrable (ex. `academie`).
2. Cliquer sur **Filtrer X**.
3. Une fenêtre s’ouvre avec toutes les valeurs uniques de la colonne.
4. Options disponibles :

   * **Tout sélectionner** → coche toutes les valeurs.
   * **Sélection individuelle** → permet de choisir seulement certaines valeurs.
5. Cliquer sur **Valider** pour appliquer le filtre.

---

### Affichage des graphiques

1. Sélectionner le **type de graphique** :

| Type      | Description                   |
| --------- | ----------------------------- |
| `bar`     | Histogramme par catégorie     |
| `line`    | Courbe par catégorie          |
| `scatter` | Nuage de points par catégorie |

2. Cliquer sur **Afficher graphique**.
3. Le graphique s’affiche dans la zone principale de l’interface.
4. Les axes sont automatiquement configurés avec le nom de la colonne X et la moyenne de Y.
5. L’axe X peut être **pivoté** pour une meilleure lisibilité.

---

### Exportation

#### Export des données

* Cliquer sur **Exporter graphique (.csv ou .xlsx)**.
* Le fichier exporté contient les **données filtrées et groupées** exactement comme affiché sur le graphique.
* Formats disponibles : `.csv` ou `.xlsx`.

#### Export du graphique

* Cliquer sur **Exporter graphique (image)**.
* Le graphique est sauvegardé au format **JPG ou PNG**.
* La résolution est automatiquement configurée (`dpi=300`).

---

## Détails techniques

* Architecture :

  * **Controller** → traitement des données, calcul des moyennes, filtrage et export.
  * **View** → interface graphique Tkinter et widgets.
  * **Main** → point d’entrée, initialisation des variables globales et liaison avec les fichiers controller et view.

* **Export des données et graphiques** :

  * Données : via Pandas (`to_csv()` / `to_excel()`).
  * Graphiques : via Matplotlib (`savefig()`).

---

## Exemple d’utilisation

1. Sélection X = `academie`, Y = `IPS_voie_GT`.
2. Filtrer uniquement certaines académies.
3. Choisir **graphique barre**.
4. Cliquer sur **Afficher graphique** → le graphique apparaît.
5. Exporter le graphique ou les données via les boutons dédiés.

---

## Bonnes pratiques

* Toujours **valider le filtre** avant d’afficher le graphique.
* Utiliser la fonction **Tout sélectionner** pour réinitialiser rapidement les filtres.

---
```

