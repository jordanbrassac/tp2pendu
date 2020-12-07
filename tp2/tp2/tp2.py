#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 17:48:16 2020

@author: jordanbrassac
"""


"""Voici le lien github pour avoir accès à tout mes fichiers https://github.com/jordanbrassac/tp2pendu#tp2pendu"""

"""Ce programme a pour but de créer le jeu du pendu sans version graphique. 
Il a été réalisé le 30 Novembre 2020 par Jordan Brassac"""
import random as rd
from tkinter  import Tk, PhotoImage, Canvas, Button,Label
from tkinter import *


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

def mot_au_hasard(data):
    """Dans cette fonction on donne en entréé notre liste de mot et on récupère en sortie un mot tiré au
    hasard dans la liste"""
    return(rd.choice(data))

def affichage(nom):
    """Cette fonction reçoit un mot en entrée et renvoie en sortie le même mot mais remplaçant toutes 
    les lettres du mot par des "_" sauf la première."""
    global mot#cette variable doit être global car elle doit être conservée tout au long de la partie
    L=creation_liste(nom)
    mot=mot_au_hasard(L)
    n=len(mot)
    return(mot[0]+(n-1)*"_")
    
def affichage2(nom,indice):
    """Cette fonction a le même but que la précédente sauf qu'ici on rajoute une deuxième variable
    d'entrée qui permet de choisir si la première lettre du mot est visible ou non"""
    global mot#cette variable doit être global car elle doit être conservée tout au long de la partie
    L=creation_liste(nom)
    mot=mot_au_hasard(L)
    n=len(mot)
    if indice in ["Oui","oui"]:    
        return(mot[0]+(n-1)*"_")
    else :
        return(n*"_")

def lancer_partie(nom):
    """Ce programme permet d'effectuer une partie de pendue à partir des fonctions précédentes.
    On met en entrée le nom du fichier contenant nos mots à deviner, puis ce programme nous le fait deviner.
    On a le droit à 8 chances. Le programme remplace les trous par les "_" par les bonnes lettres lorsque
    le joueur en trouve et nous renvoie le nombre de chances restantes lorsqu'on commet une erreur.""" 
    
    A=affichage(nom)
    print(A)
    L1=list(mot)
    A1=list(A)
    k=8#nombre d'erreur possible
    m=len(A1)-1#nombre de lettre à trouver lorsque l'on nous donne la première lettre du mot à deviner
    print("C'est parti, vous avez 8 chances pour devinez ce mot.")
    while k>0: 
        if m<=0:#si toutes les lettres du mots sont trouvés on sort de la boucle while
            break
        n=input("Choisissez une lettre :")
        if n not in L1 and m!=0:#si la lettre du joueur n'est pas dans le mot
            k=k-1#le nombre d'erreur possible diminue
            if k>1:  
                print("Faux ! Il vous reste ",k," chances")
            elif k==1:#question de grammaire
                print("Faux ! Il vous reste ",k," chance")
        elif n in L1 and m>0:#si la lettre du joueur est dans le mot 
            p=[indice for indice, valeur in enumerate(L1) if valeur==n]#donne les indices doù se trouvent les lettres correctes dans le mot
            if n not in A1:#on vérifie que la lettre n'a pas déja était trouvé
                m=m-len(p)#on retire une lettre juste autant de fois qu'elle est présente dans le mot à deviner
                for i in p:
                    A1[i]=n#on remplace les "_" par les lettres justes trouvées par le joueur
                A2=''.join(A1)
                print(A2)
                print("Vrai !")
            else:
                print("Lettre déjà trouvé !")
    if m<=0:
        print("Felicitations, vous avez gagné !")
    else:
        print("Dommage, vous avez perdu.")
        
record=0

    
def lancer_partie2(nom):
    """Cette fonctionne comme celle juste au dessus sauf qu'ici, on peut choisir si l'on souhaite que
    la première lettre du mot nous soit donnée ou non. De plus, il y a un système de calcul de score
    et de record."""
    global record
    k1=False
    indice=input("Souhaitez-vous connaitre la première lettre du mot ? ")
    while k1==False:#tant que le joueur n'a pas précisé s'il souhaitait un indice la partie ne se lance pas
        if indice in ["oui","Oui","Non","non"]:
            k1=True
        elif k1==False:
            indice=input("Avant de commencer la partie vous devez indiquer si vous souhaitezavoir un indice. Souhaitez-vous connaitre la première lettre du mot ? ")
    A=affichage2(nom,indice)
    print(A)
    L1=list(mot)
    A1=list(A)
    k=8#nombre d'erreur possible
    m=len(A1)-1#nombre de lettre à trouver lorsque l'on nous donne la première lettre du mot à deviner
    if indice in ["Oui","oui"]:
        score=100*m
    elif indice in ["Non","non"]:
        m=m+1
        score=150*(m+1)#lorsque l'on joue sans indice on a plus de points au debut de la partie
    print("C'est parti, vous avez 8 chances pour devinez ce mot.")
    while k>0: 
        if m<=0:#si toutes les lettres du mots sont trouvés on sort de la boucle while
            break
        n=input("Choisissez une lettre :")
        if n not in L1 and m!=0 :#si la lettre du joueur n'est pas dans le mot
            k=k-1#le nombre d'erreur possible diminue
            score=score-int((score/(k+1))*(9))#notre score diminue à chaque erreur
            if k>1:  
                print("Faux ! Il vous reste ",k," chances")
            elif k==1:#question de grammaire
                print("Faux ! Il vous reste ",k," chance")
        elif n in L1 and m>0:#si la lettre du joueur est dans le mot
            p=[indice for indice, valeur in enumerate(L1) if valeur==n]#donne les indices doù se trouvent les lettres correctes dans le mot
            if n not in A1:#on vérifie que la lettre n'a pas déja était trouvé
                m=m-len(p)#on retire une lettre juste autant de fois qu'elle est présente dans le mot à deviner
                for i in p:
                    A1[i]=n#on remplace les "_" par les lettres justes trouvées par le joueur
                A2=''.join(A1)
                print(A2)
                print("Vrai !")
            else:
                print("Lettre déjà trouvé !")
    if m<=0:
        print("Felicitations, vous avez gagné !")
        if record==0:
            record=score
            print("Nouveau record ! Vous avez fait un score de",score," points")
       
        if score>record:#verifie si le score du joueur est un nouveau record ou non
            record=score
            print("Nouveau record ! Vous avez fait un score de",score," points")
        else:
            print("Vous avez fait un score de",score," points")
    else:
        score=0
        print("Dommage, vous avez perdu.")
    r=input("Voulez vous rejouer ?")#demande au joueur s'il veut relancer une partie
    k2=False
    while k2==False:#tant que le joueur n'a pas précisé s'il souhaitait rejouer
        if r in ["oui","Oui","Non","non"]:
            k2=True
        elif k2==False:
                r=input("Voulez vous rejouer ?")
    if r in ["Oui","oui"]:
        lancer_partie2(nom)
    elif r in ["Non","non"]:
        print("Partie terminé, merci d'avoir jouer !")
 

       

    
    

