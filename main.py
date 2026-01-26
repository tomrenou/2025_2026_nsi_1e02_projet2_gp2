#main(code principal)

texte_bienevnue = "Bienvenue chez Lycée & So, le site qui rend l'analyse des lycées beaucoup plus simple !"

def search_number(val,v):
    gauche = 0
    droite = len(v) - 1
    milieu = (gauche + droite) //2
    if val == v[milieu]:
        return milieu
    elif val < v[milieu]:
        droite = milieu - 1
    else:
        gauche = milieu + 1
    return milieu

def accueil(a):
    