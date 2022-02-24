from tkinter import*#on import tkinter 
import os #importer os pour pouvoir ouvir d'autre fenetre
import pygame #on importe pygame

def change_de_fenetre():#on met une fonction pour changer de fenetre
    cmd = "jeu_pong.py"# ouvrir le fichier jeu_pong.py
    Fenetre.destroy()#ferme la fenetre
    pygame.quit()#on fini le pygame
    os.system(cmd)#pour quon puisse ouvrir la fenetr
    
def quitter():# on fet une fonction quitter
    Fenetre.destroy()#ferme la fenetre
def regles():#on fait la fonction regles
    cmd = "regle.py"#lance la fenetre regles
    os.system(cmd)#pour quon puisse ouvrir la fenetr

Fenetre=Tk()#on crée la fenetre tkinter
Fenetre.geometry("640x480")#on la redimensionne
Fenetre.title("Volley Pong" )#on lui donne un titre

fond = PhotoImage(file="IMG/accueil.png")# on definier fond avec l'image accueil
pygame.init()#on demare pygame
son = pygame.mixer.Sound("musique.mp3")#on definie la musique sur son
son.play()#on lance la musique
son.set_volume(0.025)# on met le volume à 0.025


    
Lab=Label(Fenetre,image=fond)#on met le fond
Lab.pack()#one le pause en pack
Bj=Button(Fenetre,command=change_de_fenetre,text="Jouer",width=20,height=2,font="calibri",fg="black",bg="#048B91",cursor="hand2")#on crée un bouton jouer qui appelle change_de_fenetre
Bj.place(x=235,y=200)    #je le place avec les cordoné
R=Button(Fenetre,command=regles,text="Règles",width=20,height=2,font="calibri",fg="black",bg="#048B91",cursor="hand2")#on crée un bouton regles qui appelle la fonction regle
R.place(x=235,y=300)#je le place avec les cordoné
Bq = Button(Fenetre,command=quitter,text="Quitter",width=20,height=2,font="calibri",fg="black",bg="#048B91",cursor="hand2")#on crée un bouton quitter qui appelle quitter
Bq.place(x=235,y=400)#je le place avec les cordoné

Fenetre.mainloop()#on fini le tkinter
pygame.quit()#on fini le pygame
