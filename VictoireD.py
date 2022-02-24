from tkinter import*#importer tkinter
import os#importer os pour pouvoir ouvir d'autre fenetre
import pygame #on importe pygame

def quitter():# on fet une fonction quitter
    cmd = "accueil.py"# ouvrir le fichier accueil.py
    Fenetre.destroy()#ferme la fenetre
    pygame.quit()#on fini le pygame
    os.system(cmd)#pour quon puisse ouvrir la fenetre
    
Fenetre=Tk()#on crée la fenetre tkinter
Fenetre.geometry("640x480")#on la redimensionne
Fenetre.title("Bien joué!" )#on lui donne un titre
fond = PhotoImage(file="IMG\joueurd.png")# on definier fond avec l'image accueil
pygame.init()#on demare pygame
son = pygame.mixer.Sound("gagner.mp3")#on definie la musique sur son
son.play()#on lance la musique
son.set_volume(0.05)# on met le volume à 0.05  
Lab=Label(Fenetre,image=fond)#on met le fond
Lab.pack()#one le pause en pack
Bq = Button(Fenetre,command=quitter,text="Retour à l'accueil",width=20,height=2,font="calibri",fg="black",bg="#048B91",cursor="hand2")#on crée un bouton quitter qui appelle quitter
Bq.place(x=235,y=400)#je le place avec les cordoné
Fenetre.mainloop()#on fini le tkinter
pygame.quit()#on fini le pygame
