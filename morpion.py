import random
import pygame
from pygame.locals import*
import sys
import os
pygame.init()
run = True
largeur=400
longeur=400
blanc=(255,255,255)
ligne_couleur=(0,0,0)
police=pygame.font.SysFont(None,40)
egalite=None
gagnant=None
tour="X"
tableau=[[" "," "," "],[" "," "," "],[" "," "," "]]
choix_continue=True
screen=pygame.display.set_mode((largeur,longeur+100),0,32)
pygame.display.set_caption("jeu du morpion")
fichier_base=os.path.dirname(__file__)
x_img=pygame.image.load(os.path.join(fichier_base,"image","marque-x.png"))
o_img=pygame.image.load(os.path.join(fichier_base,"image","marque-O.png"))
x_img=pygame.transform.scale(x_img,(80,80))
o_img=pygame.transform.scale(o_img,(80,80))


def gagne_condition():
    global gagnant,egalite,tableau,tour
    symbole = tour     
    #verifie les ligne et colonne
    for i in range(3):
        #verifie les ligne
        if tableau[i][0]==tableau[i][1]==tableau[i][2] and tableau[i][0]!=" " :
            gagnant=tableau[i][0]
            break
        #verifie les colonne
        if tableau[0][i]==tableau[1][i]==tableau[2][i] and tableau[0][i]!=" ":
            gagnant=tableau[0][i]
            break
    #verifie les diagonale
    if tableau[0][0]==tableau[1][1]==tableau[2][2] and tableau[0][0]!=" ":
        gagnant=tableau[0][0]          
    if tableau[0][2]==tableau[1][1]==tableau[2][0] and tableau[0][2]!=" ":
        gagnant=tableau[0][2]
    #verifie l'égalité
    if gagnant is None:
        egalite=match_nul(tableau)
     

def ia_facil():
    global tableau
    #choisie une case aléatoirement
    x=random.randint(0,2)
    y=random.randint(0,2)
    #verifi que la case soit bien vide
    while tableau[x][y]!=" ":
        x=random.randint(0,2)
        y=random.randint(0,2)
    tableau[x][y]="O"
    dessiner_XO(x+1,y+1)
    gagne_condition()
    affiche_statue()

def ia_p():
    global tableau,gagnant,tour,egalite
    #cherche de gagner
    for i in range(3):
        for j in range (3):
            if tableau[i][j]==" ":
                tableau[i][j]="O"
                gagne_condition()
                if gagnant=="O":
                    dessiner_XO(i+1,j+1)
                    affiche_statue() 
                    return
                else:
                    tableau[i][j]=" "
    #bloque l'adversaire
    for i in range (3):
        for j in range (3):
            if tableau[i][j]==" ":
                tableau[i][j]="X"
                gagne_condition()
                if gagnant=="X":
                    tableau[i][j]="O"
                    dessiner_XO(i+1,j+1)
                    gagnant=None
                    affiche_statue() 
                    return
                else:
                    tableau[i][j]=" "
    x=random.randint(0,2)
    y=random.randint(0,2)
    while tableau[x][y]!=" ":
        x=random.randint(0,2)
        y=random.randint(0,2)
    tableau[x][y]="O"
    dessiner_XO(x+1,y+1)
    gagne_condition()
    affiche_statue() 
             
def match_nul(tableau):
    #regarde que tout le tableau soit remplie
    for i in tableau:
        for j in i:
            if j==" ":
                return False
    return True     
            

def choix_de_mode():
    bouton_jcj=pygame.Rect(100,150,200,60)
    bouton_vs_ia=pygame.Rect(100,250,200,60)
    mode=None
    run=True
    while run:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if bouton_jcj.collidepoint(event.pos):
                    mode="JcJ"
                    run=False
                elif bouton_vs_ia.collidepoint(event.pos):
                   mode="cIa"
                   run=False
        pygame.draw.rect(screen,(46,204,113),bouton_jcj,border_radius=10)
        pygame.draw.rect(screen,(0,162,232),bouton_vs_ia,border_radius=10)
        texte_JcJ=police.render("JcJ",True,blanc)
        texte_vs_ia=police.render("VS ia",True,blanc)
        screen.blit(texte_JcJ,(bouton_jcj.centerx - texte_JcJ.get_width()//2,
                               bouton_jcj.centery - texte_JcJ.get_height()//2)) 
        screen.blit(texte_vs_ia,(bouton_vs_ia.centerx - texte_vs_ia.get_width()//2,
                                bouton_vs_ia.centery - texte_vs_ia.get_height()//2))
        pygame.display.flip()
    return mode

def affiche_statue():
    global egalite, gagnant
    if gagnant is not None:
        message=gagnant.upper()+" à gagner"
    elif egalite:
        message="c'est une égalité"
    else:
        message=tour.upper()+" joue"    
    texte=police.render(message,1,(255,255,255))
    screen.fill((0,0,0),(0,longeur,largeur,100))
    texte_rect=texte.get_rect(center=(largeur/2,longeur+50))
    screen.blit(texte,texte_rect)
    pygame.display.update()       

def commencement_du_jeu():
    pygame.display.update()
    screen.fill(blanc)
    #trace les ligne vertical
    pygame.draw.line(screen,ligne_couleur,(largeur/3,0),(largeur/3,longeur),7)
    pygame.draw.line(screen,ligne_couleur,(largeur/3*2,0),(largeur/3*2,longeur),7)
    #trace les ligne horizontaux
    pygame.draw.line(screen,ligne_couleur,(0,longeur/3),(largeur,longeur/3),7)
    pygame.draw.line(screen,ligne_couleur,(0,longeur/3*2),(largeur,longeur/3*2),7)
    affiche_statue()
    
def dessiner_XO(ligne,colonne):    
    global tableau,tour
    #avoir les coordooné au x sera placer
    posx = (colonne-1) * (largeur/3) + 30
    posy = (ligne-1) * (longeur/3) + 30
    #place le symbole dans les coordooné
    tableau[ligne-1][colonne-1] = tour

    if tour == "X":
        screen.blit(x_img, (posx, posy))
        tour = "O"
    else:
        screen.blit(o_img, (posx, posy))
        tour = "X"
    pygame.display.update()

#défini le clique du joueur
def click_utilisateur_jeu():
    global tour,tableau
    #met dans deux varibales les coordonné du curseur
    x,y=pygame.mouse.get_pos()
    if (x<largeur/3):
        colonne=1
    elif(x<largeur/3*2):
        colonne=2
    elif(x<largeur):
        colonne=3
    else:
        colonne=None    
    
    if(y<longeur/3):
        ligne=1
    elif(y<longeur/3*2):
        ligne=2
    elif(y<longeur):
        ligne=3
    else:
        ligne=None
    
    #verifie que tu coup la case soit bien vide 
    if ligne and colonne and tableau[ligne-1][colonne-1]==" " :
        dessiner_XO(ligne,colonne)
        gagne_condition()
        affiche_statue()

#va demander si il veux continuer de jouer ou quitté        
def continuer_ou_quitter():        
    global choix_continue,tableau,egalite,tour,gagnant
    #création de rectangle pour les bonton
    bouton_continuer=pygame.Rect(100,150,200,60)
    bouton_quitter=pygame.Rect(100,250,200,60)
    #met dans des variable la posion du curseur
    x,y=pygame.mouse.get_pos()
    #verifie que le curseur soit sur le bonton continuer
    if pygame.Rect.collidepoint(bouton_continuer,(x,y)):
        choix_continue=True
        tableau=[[" "," "," "],[" "," "," "],[" "," "," "]]
        egalite=None
        gagnant=None
        tour="X"
        tout_debut() 
    #verifie que le curseur soir sur le bonton quitter
    elif pygame.Rect.collidepoint(bouton_quitter,(x,y)):
            choix_continue=False
    pygame.draw.rect(screen,(46,204,113),bouton_continuer,border_radius=10)
    pygame.draw.rect(screen,(0,162,232),bouton_quitter,border_radius=10)
    texte_continuer=police.render("continuer",True,blanc)
    texte_quitter=police.render("quitter",True,blanc)
    screen.blit(texte_continuer,(bouton_continuer.centerx - texte_continuer.get_width()//2,
                               bouton_continuer.centery - texte_continuer.get_height()//2)) 
    screen.blit(texte_quitter,(bouton_quitter.centerx - texte_quitter.get_width()//2,
                                bouton_quitter.centery - texte_quitter.get_height()//2))        
            
def vs_ia_facile():
    while choix_continue:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()       
                if event.type == MOUSEBUTTONDOWN:
                    if gagnant is None and not egalite:    
                        click_utilisateur_jeu()
                    if gagnant is None and not egalite:     
                        ia_facil()
                    if gagnant is not None or egalite:
                        continuer_ou_quitter()
            pygame.display.update()

def vs_ia_difficile():
    while choix_continue:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()       
                if event.type == MOUSEBUTTONDOWN:
                    if gagnant is None and not egalite:    
                        click_utilisateur_jeu()
                    if gagnant is None and not egalite:     
                        ia_p()
                    if gagnant is not None or egalite:
                        continuer_ou_quitter()
            pygame.display.update()
def jcj_py():
    while choix_continue:
            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()       
                if event.type == MOUSEBUTTONDOWN:
                    if gagnant is None and not egalite:    
                        click_utilisateur_jeu()
                    if gagnant is not None or egalite:
                        continuer_ou_quitter()    
            pygame.display.update()

def choix_de_la_difficulté():
    bouton_facile=pygame.Rect(100,150,200,60)
    bouton_normal=pygame.Rect(100,250,200,60)
    mode=None
    run=True
    while run:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if bouton_facile.collidepoint(event.pos):
                    mode="facile"
                    run=False
                elif bouton_normal.collidepoint(event.pos):
                   mode="Normal"
                   run=False
        pygame.draw.rect(screen,(46,204,113),bouton_facile,border_radius=10)
        pygame.draw.rect(screen,(0,162,232),bouton_facile,border_radius=10)
        texte_facile=police.render("Facile",True,blanc)
        texte_normal=police.render("Normal",True,blanc)
        screen.blit(texte_facile,(bouton_facile.centerx - texte_facile.get_width()//2,
                               bouton_facile.centery - texte_facile.get_height()//2)) 
        screen.blit(texte_normal,(bouton_normal.centerx - texte_normal.get_width()//2,
                                bouton_normal.centery - texte_normal.get_height()//2))
        pygame.display.flip()
    return mode

def tout_debut():
    mode=choix_de_mode()
    if mode=="JcJ":   
        commencement_du_jeu()
        jcj_py()
    elif mode=="cIa":
        dificulté=choix_de_la_difficulté()
        if dificulté=="facile":
            commencement_du_jeu()
            vs_ia_facile()
        if dificulté=="Normal":
            commencement_du_jeu()
            vs_ia_difficile()        

tout_debut()