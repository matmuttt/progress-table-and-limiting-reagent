# ///////////////////////////////////////////////////////
# create by Mathys Doucerain
# ///////////////////////////////////////////////////////


# le but --------> trouver le reactif limitant

# tableau d'avancement d'une equation ajustee a 2 reactifs et 1 produit

# reactif d'exemple: 2Al et 3S
# produit d'exemple: Al2S3


# nb d'atomes dans l'equation ajustee du tableau
nb_A=float(input("entrez nombre d'entitées chimique A:"))
nb_B=float(input("Entrez le nombre d'entitées chimique B:"))


# nombre de moles presentes pour chaque entitees chimique
mol_A=float(input("entrez le nombre de moles pour A:"))
mol_B=float(input("entrez le nombre de moles pour B:"))

# calcul pour connaitre le reactif limitant

X_max1=float(mol_A/nb_A)
X_max2=float(mol_B/nb_B)

if X_max1>X_max2:
    print("le reactif limitant est B")
else:
    print("Le reactif limitant est A")

# calcul pour connaitre le X_max

X_max=float()

if X_max1>X_max2:
    X_max=X_max2
else:
    X_max=X_max1

# nombre stoechiometrique pour calculer le nb de moles restante dans le reactif restant

nb_stoechiometrique=float()

if X_max1>X_max2:
    nb_stoechiometrique=nb_A
else:
    nb_stoechiometrique=nb_B

# reste de moles dans les reactifs

reste_A=float((mol_A-X_max)/nb_stoechiometrique)
reste_B=float(mol_B-X_max/nb_stoechiometrique)

# nombre de moles restantes dans le reactif restant

if X_max1>X_max2:
    print("le nombre de moles restantes du reactif A est de", reste_A, "moles")
else:
    print("le nombre de moles restantes du reactif A est de", reste_B, "moles")

# calculons maintenant le nombre de moles du produit

nb_moles_produit=float(X_max)

print("le nombre de moles du produit est de", nb_moles_produit, "mole")
