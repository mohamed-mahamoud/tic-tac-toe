import random

def affichage(tableau):
    for i in tableau:
        print(f"+{"-"*3}"*3+"+")
        print (f"|{" "}{i[0]}{" "}|{" "}{i[1]}{" "}|{" "}{i[2]}{" "}|")
    print(f"+{"-"*3}"*3+"+")

def gagne_condition(tableau,tour):
    if tour==1:
        symbole="X"
    else:
        symbole="O"    
    
    w=False
    for i in range(3):
        if tableau[i][0]==tableau[i][1]==tableau[i][2]==symbole or tableau[0][i]==tableau[1][i]==tableau[2][i]==symbole :
            w=True
            return w
    if tableau[0][0]==tableau[1][1]==tableau[2][2]==symbole or tableau[0][2]==tableau[1][1]==tableau[2][0]==symbole:
        w=True           
    return w 
def placement(table,tour):
    print(f"c'est le tour du joueur {tour} de joué")
    symbole = "X" if tour ==1 else "0"
    while True:
        valeur=input(" placer les cordonné de la case que vous vouler cocher tel que par exemple 1 2: ").split()
        if len(valeur)!=2 or not all(v.isdigit() for v in valeur):
            print("c'est une entré invalide veileur entré les cordooné separer par des espace")
            continue
        x, y=map(int,valeur)
        if not (0 <= x <=2 and 0<=y<=2):
            print("les coordonné sans fausse")
            continue
        if table[x][y]!=" ":
            print(" la case n'est pas vide choissisez une autre")
            continue
        table[x][y]=symbole
        break

def ia_p(tableau,tour):
    for i in tableau:
        for j in i:
            if tableau[i][j]==" ":
                tableau[i][j]="O"
                w=gagne_condition(tableau,2)
                if w:
                    tour=1
                    return
                else:
                    tableau[i][j]=" "
    for i in tableau:
        for j in i:
            if tableau[i][j]==" ":
                tableau[i][j]="X"
                w=gagne_condition(tableau,1)
                if w:
                    tableau[i][j]="O"
                    tour=2
                    return
                else:
                    tableau[i][j]=" "
    x=random.randint(0,2)
    y=random.randint(0,2)
    while tableau[x][y]!=" ":
        x=random.randint(0,2)
        y=random.randint(0,2)
    tableau[x][y]="O"
    tour=2               
                                     
def match_nul(tableau):
    for i in tableau:
        for j in i:
            if j==" ":
                return False
    return True            

def jouer_contre_ia():
    joueur=1
    winJ=False
    winI=False
    egalite=False
    tableau=[[" "," "," "],[" "," "," "],[" "," "," "]]
    print("bienvenue dans cette partie contre ia")
    affichage(tableau)  
    while (not winJ and not winI) and not egalite:
        placement(tableau,joueur)
        affichage(tableau)
        winJ=gagne_condition(tableau,joueur)
        if not winJ:
            print("c'est le tour de l'ia")
            ia_p(tableau,joueur)
            affichage(tableau)
            winI=gagne_condition(tableau,2)
            egalite=match_nul(tableau)
        if winJ:
              print("bravo tu as gagné")
        if winI:
            print("Perdu l'ia a gagné")      
    if (not winJ and not winI) and egalite:
        print("c'est une égalité")

def contre_joueur():
    joueur=1
    win=False
    egalite=False
    tableau=[[" "," "," "],[" "," "," "],[" "," "," "]]   
    print("bienvenue dans cette partie de morpion en joueur contre joueur")
    affichage(tableau)  
    while not win and not egalite:
        placement(tableau,joueur)
        affichage(tableau)
        win=gagne_condition(tableau,joueur)
        egalite=match_nul(tableau)
        if win:
            print(f"bravo jouer {joueur} à gagner ")
        if joueur==1:
            joueur=2
        else:
            joueur=1        
    if not win and egalite:
        print("c'est une égalité")            

choix=input("bienvenue dans cette partie de morpion \nveiller choisir si vous vouler jouer contre ia en choissiant 1 ou contre un joueur avec 2 ")
while (choix!=1 and choix!=2) and not choix.isdigit() :
    choix=input("veilleur choisir la difficulté ")
if choix==1:
    jouer_contre_ia()
else :
    contre_joueur()        