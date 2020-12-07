#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:43:15 2020

@author: jordanbrassac
"""
"""Ce programme a pour but de créer la version graphique du jeu du êndu. 
Il a été réalisé le 7 Décembre 2020 par Jordan Brassac"""
import random as rd
from tkinter  import Tk, PhotoImage, Canvas, Button,Label
from tkinter import *

def mot_au_hasard(data):
    """Dans cette fonction on donne en entréé notre liste de mot et on récupère en sortie un mot tiré au
    hasard dans la liste"""
    global mot1
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
    """Cette fonction reçoit un mot en entrée et renvoie en sortie le même mot mais remplaçant toutes 
    les lettres du mot par des "_" sauf la première."""
    #cette variable doit être global car elle doit être conservée tout au long de la partie
    nom="tp2"
    L=creation_liste(nom)
    mot=mot_au_hasard(L)
    n=len(mot)
    x.set(mot[0]+(n-1)*"_")
    return(mot[0]+(n-1)*"_")
    
    
def verif_lettre():
    global k
    n=Lettre.get()
    k=8
    A=affichage3("tp2")
    A1=list(A)
    L1=list(mot1)
    m=len(list(mot1))-1
       
    if n not in L1 and m!=0 :
        k=k-1
        
        if k>1:  
            resultat.set("Faux ! Il vous reste "+str(k)+" chances")
        elif k==1:#question de grammaire
            resultat.set("Faux ! Il vous reste "+str(k)+" chance")
    elif n in L1 and m>0:#si la lettre du joueur est dans le mot
        p=[indice for indice, valeur in enumerate(L1) if valeur==n]#donne les indices doù se trouvent les lettres correctes dans le mot
        if n not in A1:#on vérifie que la lettre n'a pas déja était trouvé
            m=m-len(p)#on retire une lettre juste autant de fois qu'elle est présente dans le mot à deviner
            for i in p:
                A1[i]=n#on remplace les "_" par les lettres justes trouvées par le joueur
            A2=''.join(A1)
            x.set(A2)
            resultat.set("Vrai !")
        else:
            resultat.set("Lettre déjà trouvé !")
    if m<=0:
        resultat.set("Felicitations, vous avez gagné !")
        
    else:
        resultat.set("Dommage, vous avez perdu.")
    
    

        
        
fenetre=Tk()
fenetre.title("Jeu du pendu")

image1=PhotoImage(file='bonhomme1.gif')
image2=PhotoImage(file='bonhomme2.gif')
image3=PhotoImage(file='bonhomme3.gif')
image4=PhotoImage(file='bonhomme4.gif')
image5=PhotoImage(file='bonhomme5.gif')
image6=PhotoImage(file='bonhomme6.gif')
image7=PhotoImage(file='bonhomme7.gif')
image8=PhotoImage(file='bonhomme8.gif')


canevas=Canvas(fenetre,width=300,height=300)
item=canevas.create_image(150,150,image=image1)
canevas.pack()
x=StringVar()

boutonproposer=Button(fenetre,text='Proposer',command=affichage3)
boutonquitter=Button(fenetre,text='Quitter',command=fenetre.destroy)
boutonproposer.pack(side='left',padx=10,pady=10)
boutonquitter.pack(side='left',padx=10,pady=10)

texteLabel1 = Label(fenetre, textvariable = x,bg='white')
texteLabel1.pack()

mot=StringVar()
resultat=StringVar()
Lettre=StringVar()

champ=Entry(fenetre,textvariable=Lettre)
champ.focus_set()
champ.pack(side='left',padx=10,pady=10)
bout_3=Button(fenetre,text='Entrer',command=verif_lettre)
bout_3.pack(side="left")

texteLabel1 = Label(fenetre, textvariable = resultat,bg='white')
texteLabel1.pack()

texteLabel2 = Label(fenetre, textvariable = x,bg='white')
texteLabel2.pack()

fenetre.mainloop()