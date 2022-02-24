import pygame #importe pyame
from pygame.locals import * #importe pyame
from pygame.time import*
import os



def change_de_fenetre():#on met une fonction pour changer de fenetre
    cmd = "accueil.py"# ouvrir le fichier jeu_pong.py
    pygame.quit()
    os.system(cmd)#pour quon puisse ouvrir la fenetr
def detect_collision(ballerect,barrerect):
    '''
    fonction qui détecte si la balle entre en contacte avec un des bords de la barre
     et renvoie 'Est' si le côté touché est le droit, 'Ouest' si le côté touché est le gauche
    'Nord' si le côté touché est celui du dessus et 'Sud' si c'est celui du dessous
    '''
    if barrerect.top<=ballerect.top and barrerect.bottom>=ballerect.bottom and barrerect.left<=ballerect.right and barrerect.right>=ballerect.right :#on retire la largeur de la barre a gauche
        return'Ouest'
    if barrerect.top<=ballerect.top and barrerect.bottom>=ballerect.bottom and barrerect.right>=ballerect.left and barrerect.left<=ballerect.left:
        return 'Est'
    if  barrerect.top<=ballerect.bottom and barrerect.right>=ballerect.right and barrerect.bottom >=ballerect.top and barrerect.left <= ballerect.left :
        return 'Nord'
    if  barrerect.bottom<=ballerect.top and barrerect.right>=ballerect.right and barrerect.top>=ballerect.bottom :
        return 'Sud'
    else :return False
def compteur_score(joueur):
    global score_g,score_d #on importe le score
    if joueur==1:         # on verifie quel joueur a marqué
        score_g=score_g+1 # et on ajoute les point
    if joueur==2:         #
        score_d=score_d+1 #


# Main
pygame.init()
#Création de la fenetre
taille=largeur, hauteur = 640, 480#on choisi la taille
fenetre = pygame.display.set_mode(taille)#la fenetre se fait par rapport à la taille

#Titre
pygame.display.set_caption("Volley Pong") #donner un titre à la fenêtre



#Chargement et collage de la balle et de la barre
fond=pygame.image.load("IMG/fond.png").convert()# on définie le fond
balle = pygame.image.load("IMG/ball.png").convert_alpha()#on met le fichier ball.png pour balle convert alpha pour le vide dans limage
ballerect = balle.get_rect() #on crée le get_rect
barre_gauche = pygame.image.load("IMG/barre.png").convert_alpha()#on met le fichier barre.png pour barre_gauche convert alpha pour le vide dans limage
barre_droite = pygame.image.load("IMG/barre2.png").convert_alpha()#on met le fichier barre2.png pour barre_droite convert alpha pour le vide dans limage
barrerect_gauche = barre_gauche.get_rect()  #on crée le get_rect
barrerect_gauche= barrerect_gauche.move((0,210))# on décale la barre de droite a droite
barrerect_droite = barre_droite.get_rect()  #on crée le get_rect
barrerect_droite= barrerect_droite.move((625,210))# on décale la barre de droite a droite

#musique
son = pygame.mixer.Sound("musique.mp3")#on definie la musique sur son
son.play()#on lance la musique
son.set_volume(0.025)# on met le volume à 0.025

#Création des variables
font = pygame.font.Font(None, 80)#on definie font
vitesse = [1.5,1.5]#on met la vitesse à 1,1
noir = 0, 0, 0#on féinie le noir
GREY=200,200,200#on définie le grey
continuer=1
score_g=0#on met les scores à 0
score_d=0#on met les scores à 0


#Rafraîchissement de l'écran
pygame.display.flip()
pygame.key.set_repeat(400, 30) #pour pouvoir laisser les fleches enfoncées
ballerect=ballerect.move((320,240)) #placer la balle au centre au départ
while continuer:

    #Création de la boucle de déplacement de la balle
    pygame.time.Clock().tick(100) #pour ralentir la boucle de jeu
    ballerect = ballerect.move(vitesse)

    if ballerect.left < 0 : # changement de direction de la balle si atteint les bords gauche ou droit
        vitesse[0] = -vitesse[0]
        compteur_score
        compteur_score(2)
    if ballerect.right > largeur: # changement de direction de la balle si atteint les bords gauche ou droit
        vitesse[0] = -vitesse[0]
        compteur_score(1)

    if ballerect.top < 0 or ballerect.bottom > hauteur: # changement de direction de la balle si atteint les bords bas ou haut
        vitesse[1] = -vitesse[1]
    if score_g == 7:  #si le score du joueur de gauche =7
        cmd = "VictoireG.py"# ouvrir le fichier jeu_pong.py
        pygame.quit()#fin du pygame
        os.system(cmd)#pour quon puisse ouvrir la fenetr

    if score_d == 7:# si le score du joueur de droite =7
        cmd = "VictoireD.py"# ouvrir le fichier jeu_pong.py
        pygame.quit()#fin du pygame
        os.system(cmd)#pour quon puisse ouvrir la fenetr


    #Gestion de la fermeture :
    for event in pygame.event.get():   #On parcourt la liste de tous les événements reçus
        
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle
    #quitter avec echap
        if event.type == KEYDOWN:#Si "touche echap"
            if event.key ==  K_ESCAPE:
                change_de_fenetre()# appelle la fonction change_fenetre qui quit et ouvre l'accueil



            
    # mouvement de la barre de gauche:
        if event.type == KEYDOWN:
            if event.key == K_q:             #Si "touche q"
                barrerect_gauche = barrerect_gauche.move(0,30) #On descend la barre de gauche de 30 pixels
            if event.key == K_a:             #Si "touche a"
                barrerect_gauche = barrerect_gauche.move(0,-30) #On monte la barre de gauche de 30 pixels
            if event.key == K_p:             #Si "touche p"
                barrerect_droite = barrerect_droite.move(0,-30) #On monte la barre de gauche de 30 pixel
            if event.key == K_m:             #Si "touche m"
                barrerect_droite = barrerect_droite.move(0,30) #On descend la barre de gauche de 30 pixels

    if ballerect.colliderect(barrerect_gauche) :#si la balle touche la barre de gauche
        vitesse[0]=-vitesse[0] #pars dans le sens oppose

    if ballerect.colliderect(barrerect_droite) :#si la balle touche la barre de droite
        vitesse[0]=-vitesse[0]#pars dans le sens oppose
    #aughementation de la vitesse petit a petit
    temps = pygame.time.get_ticks()
    if temps >= 10000 and temps <= 10020: #au bout de 10 secondes
        vitesse[0] = vitesse[0]*1.2 #augmente les deux indices de directions ce qui fait accélérer la balle
        vitesse[1] = vitesse[1]*1.2
    if temps >= 20000 and temps <= 20020: #au bout de 20 secondes
        vitesse[0] = vitesse[0]*1.2#augmente les deux indices de directions ce qui fait accélérer la balle
        vitesse[1] = vitesse[1]*1.2
    if temps >= 30000 and temps <= 30020: #au bout de 30 secondes
        vitesse[0] = vitesse[0]*1.2#augmente les deux indices de directions ce qui fait accélérer la balle
        vitesse[1] = vitesse[1]*1.2


    #on empeche les barres de sortir du cadre
    if barrerect_gauche.top<0 :                        
        barrerect_gauche=barrerect_gauche.move(0,10)
    if barrerect_gauche.bottom>hauteur:                
        barrerect_gauche=barrerect_gauche.move(0,-10)
    if barrerect_droite.top<0 :                        
        barrerect_droite=barrerect_droite.move(0,10)
    if barrerect_droite.bottom>hauteur:                
        barrerect_droite=barrerect_droite.move(0,-10)

    #Création de la ligne de séparation centrale
    fenetre.blit(fond,(0,0))
    fenetre.blit(balle, ballerect)  #Dessin de la balle
    fenetre.blit(barre_gauche, barrerect_gauche) #Dessin de la barre gauche
    fenetre.blit(barre_droite, barrerect_droite) #Dessin de la barre droite

    #affichage du score
    text = font.render(str(score_g), 1, (0, 0, 0))#le premier score a gauche
    textpos = text.get_rect()#on crée le get_rect
    fenetre.blit(text,(160,10))# on le décale de 160 de la gauche et de 10 en haut

    text2 = font.render(str(score_d), 1, (0, 0, 0))#le deuxieme score a droite
    text2pos = text.get_rect()#on crée le get_rect
    fenetre.blit(text2,(440,10))# on le décale de 440 de la gauche et de 10 en haut# on le décale de 160 de la gauche et de 10 en haut

    #Rafraîchissement de l'écran
    pygame.display.flip()

pygame.quit()#fin du pygame

