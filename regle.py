from tkinter import* #importer tkinter
import os #importer os pour pouvoir ouvir d'autre fenetre
import pygame #on importe pygame
    
def quitter():# on fet une fonction quitter
    Fenetre.destroy()#ferme la fenetre
    pygame.quit()#on fini le pygame
pygame.init()#on demare pygame
son = pygame.mixer.Sound("voix.mp3")#on definie la musique sur son
son.play()#on lance la musique
son.set_volume(0.05)# on met le volume à 0.05


Fenetre=Tk()#on crée la fenetre tkinter
Fenetre.geometry("640x480")#on la redimensionne
Fenetre.title("Volley Pong Regles" )#on lui donne un titre
fond = PhotoImage(file="IMG/regles.png")# on definier fond avec l'image accueil    
Lab=Label(Fenetre,image=fond)#on met le fond
Lab.pack()#on le pack
Bq = Button(Fenetre,command=quitter,text="Quitter",width=20,height=2,font="calibri",fg="black",bg="#048B91",cursor="hand2")#on crée un bouton quitter qui appelle quitter
Bq.place(x=235,y=400)#je le place avec les cordoné
Fenetre.mainloop()#on fini le tkinter
pygame.quit()#on fini le pygame

