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
        return 2
    elif tour==2 :
        x,y=map(int,input(" placer les cordonné de la case que vous vouler cocher ").split())
        while table[x][y]!=" ":
            x,y=map(int,input("erreur cett case est déja jouer choisisez une autre ").split())
        table[x][y]="O"
        return 1          
tour=2
affichage(tableau)
tour=placement(tableau,tour)
affichage(tableau)
print(tour)
