tableau=[[" "," "," "],[" "," "," "],[" "," "," "]]

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
        x,y=map(int,input(" placer les cordonné de la case que vous vouler cocher ").split())
        while table[x][y]!=" ":
            x,y=map(int,input("erreur cett case est déja jouer choisisez une autre ").split())
        tableau[x][y]="X"
    elif tour==2 :
        x,y=map(int,input(" placer les cordonné de la case que vous vouler cocher ").split())
        while table[x][y]!=" ":
            x,y=map(int,input("erreur cett case est déja jouer choisisez une autre ").split())
        table[x][y]="O"        
joueur=1
win=False
tour=0
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
    
#il me reste a poser la securité pour avoir les bonne cordonné et faire le message de début 