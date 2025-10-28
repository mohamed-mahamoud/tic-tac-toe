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
            break
    if tableau[0][0]==tableau[1][1]==tableau[2][2]==symbole or tableau[0][2]==tableau[1][1]==tableau[2][0]==symbole:
        w=True           
    return w 
def placement(table,tour):
    print(f"c'est le tour du joueur {tour} de joué")
    if tour==1:
        x,y=map(int,input(" placer les cordonné de la case que vous vouler cocher tel que par exemple 1 2: ").split())
        while (x<0 or x>2 ) or (y<0 or y>2 ):
            x,y=map(int,input(" les cordonné ne sont pas bons veiller rechoisir ").split())
        while table[x][y]!=" " :
            x,y=map(int,input("erreur cett case est déja jouer choisisez une autre ").split())
        table[x][y]="X"
    elif tour==2 :
        x,y=map(int,input(" placer les cordonné de la case que vous vouler cocher tel que par exemple 1 2:  ").split())
        while (x<0 or x>2) or (y<0 or y>2):
            x,y=map(int,input(" les cordonné ne sont pas bons veiller rechoisir ").split())
        while table[x][y]!=" " or (x<0 and x>2) or (y<0 and y>2)  :
            x,y=map(int,input("erreur cett case est déja jouer ou est est mauvaise choisisez une autre ").split())
        table[x][y]="O"        


def ia_p(tableau,tour):
    for i in range (3):
        for j in range (3):
            if tableau[i][j]==" ":
                tableau[i][j]="O"
                w=gagne_condition(tableau,2)
                if w:
                    tour=1
                    return
                else:
                    tableau[i][j]=" "
    for i in range (3):
        for j in range (3):
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
    while tableau[x][j]!=" ":
        x=random.randint(0,2)
        y=random.randint(0,2)
    tableau[x][y]="O"
    tour=2               
                                     
        

def jouer_contre_ia():
    joueur=1
    win=False
    tour=0
    tableau=[[" "," "," "],[" "," "," "],[" "," "," "]]
    print("bienvenue dans cette partie contre ia")
    affichage(tableau)  
    while not win and tour<9:
        placement(tableau,joueur)
        affichage(tableau)
        win=gagne_condition(tableau,joueur)
        print("c'est le tour de l'ia")
        ia_p(tableau,joueur)
        affichage(tableau)
        win=gagne_condition(tableau,2)
        if win:
            win_ia=gagne_condition(tableau,2)
            if win_ia: 
                print("perdu ordinateur à gagner ")
            else:
                print("bravo tu as gagner ")    
        else:
            tour+=1      
    if not win and tour==9:
        print("c'est une égalité")

def contre_joueur():
    joueur=1
    win=False
    tour=0
    tableau=[[" "," "," "],[" "," "," "],[" "," "," "]]   
    print("bienvenue dans cette partie de morpion en joueur contre joueur")
    affichage(tableau)  
    while not win and tour<9:
        placement(tableau,joueur)
        affichage(tableau)
        win=gagne_condition(tableau,joueur)
        if win:
            print(f"bravo jouer {joueur} à gagner ")
        else:
            tour+=1
        if joueur==1:
            joueur=2
        else:
            joueur=1        
    if not win and tour==9:
        print("c'est une égalité")            
jouer_contre_ia()