class tableau:
    def __init__(self):
        self.dessin=[[" "," "," "],[" "," "," "],[" "," "," "]]
    def affichage(self):
        for i in self.dessin:
            print(f"+{"-"*3}"*3+"+")
            print (f"|{" "}{i[0]}{" "}|{" "}{i[1]}{" "}|{" "}{i[2]}{" "}|")
        print(f"+{"-"*3}"*3+"+")

def gagne_condition(tableau,symbole):
    w=False
    for i in range(3):
        if tableau[i][0]==tableau[i][1]==tableau[i][2]==symbole or tableau[0][i]==tableau[1][i]==tableau[2][i]==symbole :
            w=True
            break
    if tableau[0][0]==tableau[1][1]==tableau[2][2]==symbole or tableau[0][2]==tableau[1][1]==tableau[2][0]==symbole:
        w=True           
    return w 
def placement(tableau,tour):
    print(f"c'est le tour du joueur {tour} de joué")
    if tour==1:
        cord=[int(nb) for nb in  input(" placer les cordonné de la case que vous vouler cocher").split(" ")]
        while tableau[cord[0]][cord[1]]!=" ":
            cord=[int(nb) for nb in  input("erreur cett case est déja jouer choisisez une autre ").split(" ")]
board=tableau()
board.affichage()
board.dessin[0][0]