#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:43:15 2020

@author: jordanbrassac
"""
"""Ce programme a pour but de créer la version graphique du jeu du êndu. 
Il a été réalisé le 7 Décembre 2020 par Jordan Brassac"""
import random as rd
from tkinter  import Tk, PhotoImage, Canvas, Button,Label, StringVar,Entry


def mot_au_hasard(data):
    """Dans cette fonction on donne en entréé notre liste de mot et on récupère en sortie un mot tiré au
    hasard dans la liste"""
    mot1=rd.choice(data)
    return mot1
    
def creation_liste(nom):
    """Cette fonction permet de recuperer nos mots dans notre fichier txt et de les mettre dans une liste.
     On a donc en entrée le nom du fichier contenant les mots, à écrire entre guillemets lorsque l'on 
     appelle la fonction et en sortie on a la liste précédemment évoquée."""
    L=[]
    fichier=open(nom+".txt","r",encoding='utf-8-sig')
    for ligne in fichier:
        data=ligne.split("\n") #permet de supprimer les \n qui représentent les retour à ligne
        data=str(data[0])#on recupère notre chaine de caractère contenant not mot
        data2=data.split(",") #on sépare les mots par une virgule
        L=L+data2
    fichier.close()
    for i in L:#On supprime tous les éléments vides possiblement crées à cause de la supression des \n
        if i=='':
            L.remove('')
    return L

def affichage3():
    """Cette fonction permet de renvoyer le mot à deviner mais en remplaçant les lettres du mot par des "_" sauf la première."""
    #cette variable doit être global car elle doit être conservée tout au long de la partie
    global mot, A, A1, k, m, score
    nom="tp2"#fichier contenant les mots à deviner
    L=creation_liste(nom)
    mot=mot_au_hasard(L)#tirage du mot à deviner
    n=len(mot)
    A=mot[0]+(n-1)*"_"#création de l'affichage souhaitée
    x.set(A)#affichage  de A sur la fenêtre
    A1=list(A)
    k=7#initialisation de notre compteur de chances
    m=len(list(mot))-1#initialisation de notre compteur de lettres justes
    score=len(list(mot))*1000#initialisation du score du joueur
    
    
score=0#initisalition score
record=0#initisalition score
def verif_lettre():
    global k, A1, A2, m, d, score, e
    n=Lettre.get()#on récupère la lettre proposée par le joueur
    L1=list(mot)
    Lettre.set("")
    if n not in L1 and m!=0 :#si la lettre est dans le mot et que ce n'était pas la dernière à trouver
        k=k-1#actualisation de notre compteur chance
        if k==1:  
            resultat.set("Faux ! Il vous reste "+str(k)+" chance")#affichage des chances qu'il restent au joueur 
            item=canevas.create_image(150,150,image=image7)#affichage de l'image correspondante aux chances qu'il restent au joueur
            score=int(score-(score/9)*(8-k))
        elif k==2:
            resultat.set("Faux ! Il vous reste "+str(k)+" chances")#affichage des chances qu'il restent au joueur
            item=canevas.create_image(150,150,image=image6)#affichage de l'image correspondante aux chances qu'il restent au joueur
            score=int(score-(score/9)*(8-k))
        elif k==3:#question de grammaire
            resultat.set("Faux ! Il vous reste "+str(k)+" chances")#affichage des chances qu'il restent au joueur
            item=canevas.create_image(150,150,image=image5)#affichage de l'image correspondante aux chances qu'il restent au joueur
            score=int(score-(score/9)*(8-k))
        elif k==4:#question de grammaire
            resultat.set("Faux ! Il vous reste "+str(k)+" chances")#affichage des chances qu'il restent au joueur
            item=canevas.create_image(150,150,image=image4)#affichage de l'image correspondante aux chances qu'il restent au joueur
            score=int(score-(score/9)*(8-k))
        elif k==5:#question de grammaire
            resultat.set("Faux ! Il vous reste "+str(k)+" chances")#affichage des chances qu'il restent au joueur
            item=canevas.create_image(150,150,image=image3)#affichage de l'image correspondante aux chances qu'il restent au joueur
            score=int(score-(score/9)*(8-k))
        elif k==6:#question de grammaire
            resultat.set("Faux ! Il vous reste "+str(k)+" chances")#affichage des chances qu'il restent au joueur
            item=canevas.create_image(150,150,image=image2)#affichage de l'image correspondante aux chances qu'il restent au joueur   
            score=int(score-(score/9)*(8-k))
    elif n in L1 and m>0:#si la lettre du joueur est dans le mot
        p=[indice for indice, valeur in enumerate(L1) if valeur==n]#donne les indices doù se trouvent les lettres correctes dans le mot
        if n not in A1:#on vérifie que la lettre n'a pas déja était trouvé
            m=m-len(p)#on retire une lettre juste autant de fois qu'elle est présente dans le mot à deviner
            for i in p:
                A1[i]=n#on remplace les "_" par les lettres justes trouvées par le joueur
            A2=''.join(A1)
            x.set(A2)#actualisation de l'affichage des lettres à trouver  
            resultat.set("Vrai !")#affichage si la lettre proposée par le joueur est dans le mot
        else:
            resultat.set("Lettre déjà trouvé !")#affichage si la lettre proposée par le joueur est dans le mot mais qu'elle a déjà était découverte
    if m<=0:
        resultat.set("Felicitations, vous avez gagné !")#affichage quand le joueur gagne la partie
        d=False#permet de dire que la partie est finie
        e=True#permet de dire qu'une partie a déjà était joué
        if score> record:
            info.set("Nouveau Record !!! Vous avez fait "+str(score)+" points")
            record1.set("Record actuel: "+str(score))
        else:
            info.set("Vous avez fait "+str(score)+" points")
    elif k==0:
        resultat.set("Dommage, vous avez perdu.")#affichage quand le joueur perd la partie
        score =0
        d=False#permet de dire que la partie est finie
        e=True#permet de dire qu'une partie a déjà était joué
        item=canevas.create_image(150,150,image=image8)#affichage de l'image correspondante à la défaite du joueur

c=False #variable qui vérifie si le mot à deviner est affiché  
d=False #variable qui vérifie si le jeu est fini
e=False #variable qui verifie que l'on puisse relancer une partie seulement si on en a déjà lancé une juste avant

def pendu():
    """Cette fonction permet d'effectuer une partie de pendu lorsque l'utilisateur clique sur proposer."""
    global c,d,e 
    info.set("")#verification que la variable info soit vide
    if c==False:#verification que le mot à trouver (avec les lettres cachées) a déjà était montré au joueur
        affichage3()
        c=True
        d=True
    elif d==True:#verification que la partie continue
        verif_lettre()
    elif e==True:#verification si le joueur a déjà jouer une partie juste avant
        x.set("")
        info.set("Partie terminé, cliquez sur rejouer, si vous voulez recommencer une faire partie !")
    
def rejouer():
     """Cette fonction permet de relancer une partie de pendu lorsque l'utilisateur clique sur rejouer, si une partie a déjà 
     été jouer juste avant."""
     global c,d,e
     resultat.set("")
     c=False #réinitialisations des variables
     d=False #réinitialisations des variables
     if e==True:#si l'utilisateur a déjà jouer une partie juste avant
         info.set("")
         item=canevas.create_image(150,150,image=image1)#on remet la première image
         pendu()#on relance le jeu
     else:
         info.set("veuillez d'abord jouer une partie avant d'en relancer une")
            
def indice():   
    """Cette fonction renvoie un indice lorsque le joueur est bloqué."""
    if d==True:#verifie qu'une partie est en cours
        ind=rd.choice(list(mot))#tir une lettre du mot à deviner au hasard
        if ind not in A1 :#verifie que l'indice n'a pas déjà était trouvé
            Lettre.set(ind)
            pendu()
    elif c==False and d==False:
        info.set("Vous devez d'abord lancer une partie avant de demander un indice.")
    else:
        indice()
    
#création fenetre        
fenetre=Tk()
fenetre.title("Jeu du pendu")

#chargement image
image1=PhotoImage(file='bonhomme1.gif')
image2=PhotoImage(file='bonhomme2.gif')
image3=PhotoImage(file='bonhomme3.gif')
image4=PhotoImage(file='bonhomme4.gif')
image5=PhotoImage(file='bonhomme5.gif')
image6=PhotoImage(file='bonhomme6.gif')
image7=PhotoImage(file='bonhomme7.gif')
image8=PhotoImage(file='bonhomme8.gif')




#affichage image
canevas=Canvas(fenetre,width=300,height=300)
item=canevas.create_image(150,150,image=image1)



#création bouton
boutonrejouer=Button(fenetre,text='Rejouer',command=rejouer)
boutonquitter=Button(fenetre,text='Quitter',command=fenetre.destroy)
boutonproposer=Button(fenetre,text='Proposer',command=pendu)
boutonindice=Button(fenetre,text='Indice',command=indice)

#variable contenant du texte qui devra s'afficher sur la fenêtre pendant le programme
x=StringVar()
mot=StringVar()
resultat=StringVar()
Lettre=StringVar()
info=StringVar()
record1=StringVar()

#création du champ de saisie
champ=Entry(fenetre,textvariable=Lettre)
champ.focus_set()


#création des zones d'affichage de texte
texteLabel1 = Label(fenetre, textvariable = x,bg='white', padx=10 , pady=10 )
texteLabel2 = Label(fenetre, textvariable = resultat,bg='white', padx=10 , pady=10)
texteLabel3 = Label(fenetre, textvariable = info,bg='white', padx=10 , pady=10)
texteLabel4 = Label(fenetre, textvariable = record1,bg='white', padx=10 , pady=10)

#mise en place des élèments sur la fenêtre
champ.grid(row=1, column=2)
boutonrejouer.grid(row=2, column=1)
boutonquitter.grid(row=3, column=1)
boutonproposer.grid(row=1, column=1)
boutonindice.grid(row=1,column=3)
texteLabel1.grid(row=4, sticky='NE')
texteLabel2.grid(row=5)
texteLabel3.grid(row=6)
texteLabel4.grid(row=7)
canevas.grid(column=4, row=7)

fenetre.mainloop()