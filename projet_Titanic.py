# -*- coding: utf-8 -*-
from tkinter import *
from random import randint,choice
import string
import tkinter as tk
import time
import tkinter.font as tkFont
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


#fonction pour quitter la page
def Quitter():
    sys.exit()

#(fonction en cours)weight_au_harsard_pour_bulles = random.randint(0,200)
ok_pour_bulle=True

#création des bulles ainsi qu leurs déplacements
def bulle():
    while ok_pour_bulle==True:
        for i in range (1):
            #image des bulles
            image_de_la_bulle= PhotoImage(file = "bulle_fond.gif",\
                              width=110,height=300)
            image_de_la_petite_bulle= PhotoImage\
                    (file = "bulle_fond.gif",width=110,height=100)



            #creation de trois canvas différents pour acceuillir les bulle 1,2,3
            bulle = canvas_pour_image.create_image\
                    (0,450,image= image_de_la_bulle,anchor='nw')
            canvas_pour_image.pack(fill='both',expand=True)


            bulle2 = canvas_pour_image.create_image\
                    (500,450,image= image_de_la_bulle,anchor='nw')
            canvas_pour_image.pack(fill='both',expand=True)

            #cette bulle utilise une image différente mais est toujours placé à un endroit voulu
            bulle3 = canvas_pour_image.create_image\
                    (150,450,image= image_de_la_petite_bulle,anchor='nw')
            canvas_pour_image.pack(fill='both',expand=True)

            #déplacement de la bulle 1
            i =0
            while i<45:
                canvas_pour_image.move(bulle,0,-20)
                time.sleep(0.1)
                canvas_pour_image.update()
                i=i+1
            canvas_pour_image.after(4000)
            i=0
            #déplacement de la bulle 2
            while i<45:
                canvas_pour_image.move(bulle2,0,-20)
                time.sleep(0.1)
                canvas_pour_image.update()
                i=i+1
            canvas_pour_image.after(4000)
            i=0
            #déplacement de la bulle 3
            while i<45:
                canvas_pour_image.move(bulle3,0,-20)
                time.sleep(0.1)
                canvas_pour_image.update()
                i=i+1
            canvas_pour_image.after(4000)
        break


#fonction qui crée un dataframe contenant que les lignes désirées et qui compte les lignes à la fin   
def filtres():   
    data = pd.read_excel('titanic3.xls')
    data = data.drop(['name', 'sibsp', 'parch', 'ticket',\
                    'fare', 'cabin', 'embarked', 'boat', 'body', 'home.dest'],axis=1)
    data.dropna()
    lignes_début = len(data.axes[0])
    if sex.get() == 1:
        data = data[data['sex'] == 'male']
    if sex.get() == 2:
        data = data[data['sex'] == 'female']
    if classe.get() == 1:
        data = data[data['pclass'] == 1]
    if classe.get() == 2:
        data = data[data['pclass'] == 2]
    if classe.get() == 3:
        data = data[data['pclass'] == 3]
    if age.get() == 1:
        data = data[data['age'] < 18]
    if age.get() == 2:
        data = data[data['age'] > 18]
    if état.get() == 1:
        data = data[data['survived'] == 1]
    if état.get() == 2:
        data = data[data['survived'] == 0]
    total_lignes = len(data.axes[0]) 
    lignes_fin = lignes_début - total_lignes
    return total_lignes,lignes_fin

#fonction qui affiche le graphique
def afficher_graphique():
    x = filtres()
    plt.pie(x, labels = ['Population visée', 'Reste population'],
    colors = ['red', '#40E0D0'],
    explode = [0.3, 0],
    autopct = lambda x: str(round(x, 2)) + '%',
    pctdistance = 0.7, labeldistance = 1.4,
    shadow = True)
    plt.show()




#fonction qui destruit l'accueil et remplace par les statistiques
def CreateNewWindow():
# variables des cases cochées
    sex.set(0)
    classe.set(0)
    age.set(0)
    état.set(0)
    
#destruction de l'ancienne image de fond, du texte et du bouton
    canvas_pour_image.delete(ALL)

#création d'une nouvelle fenêtre avec une nouvelle taille
    window.title("Statistiques du Titanic")
    window.geometry("900x563")
    window.config(background = "#048B9A")
    window.iconbitmap("titanic.ico")
    window.resizable(width=False,height=False)
    
    canvas_pour_image.create_image(0,0,image = image_fond2,anchor='nw')
    canvas_pour_image.create_text(300,25,text="Les Criteres",\
                                 font=("Roman",50, "bold"),anchor='nw')
    canvas_pour_image.create_text(30,125,text="Le sexe des passagers :",\
                                 font=("Roman",25, "bold"),anchor='nw')
    canvas_pour_image.create_text(560,125,text="La classe des passagers :",\
                                 font=("Roman",25, "bold"),anchor='nw')
    canvas_pour_image.create_text(30,300,text="Age des passagers :",\
                                 font=("Roman",25, "bold"),anchor='nw')
    canvas_pour_image.create_text(560,300,text="Survivant :",\
                                 font=("Roman",25, "bold"),anchor='nw')



#caractéristiques des options du theme 1
    case_theme1_option1 = Radiobutton(window,text ='Homme',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=sex,value=1)
    case_theme1_option2 = Radiobutton(window,text ='Femme',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=sex,value=2)

#caractéristiques des options du theme 2
    case_theme2_option1 = Radiobutton(window,text ='1ère Classe',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=classe,value=1)
    case_theme2_option2 = Radiobutton(window,text ='2e Classe',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=classe,value=2)
    case_theme2_option3 = Radiobutton(window,text ='3e Classe',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=classe,value=3)

#caractéristiques des options du theme 3
    case_theme3_option1 = Radiobutton(window,text ='Mineur',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=age,value=1)
    case_theme3_option2 = Radiobutton(window,text ='Majeur',bg='#FADF8F',\
                        fg='black',font=("Roman",15),activeforeground='white',\
                        activebackground='#048B9A',variable=age,value=2)

#caractéristiques des options du theme 4
    case_theme4_option1 = Radiobutton(window,text ='Oui',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=1)
    case_theme4_option2 = Radiobutton(window,text ='Non',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=2)
        
#caractéristiques du bouton "rechercher"
    button_rechercher = Button(window,text='rechercher',bg='#FDD663',fg='black',\
                        font=("Roman",20),activeforeground='white',\
                        activebackground='#048B9A',command=afficher_graphique)

#placements des options du theme 1
    case_theme1_option1.place(x=50,y=180)
    case_theme1_option2.place(x=50,y=220)

#placements des options du theme 2
    case_theme2_option1.place(x=580,y=180)
    case_theme2_option2.place(x=580,y=220)
    case_theme2_option3.place(x=580,y=260)

#placements des options du theme 3
    case_theme3_option1.place(x=50,y=360)
    case_theme3_option2.place(x=50,y=400)

#placements des options du theme 4
    case_theme4_option1.place(x=580,y=360)
    case_theme4_option2.place(x=580,y=400)

#placement du bouton "rechercher"
    button_rechercher.place(x=380,y=480)

# création du menu en haut
    menu_bar = Menu(window)
    menu_fill = Menu(menu_bar, tearoff=0)
    menu_fill.add_command(label="Choix des statistiques", command=CreateNewWindow)
    menu_fill.add_command(label="Quitter", command=Quitter)
    menu_bar.add_cascade(label="Fonction", menu=menu_fill)
    window.config(menu=menu_bar)



#fenêtre
window = Tk()

# variables des cases cochées
sex = IntVar(master= window, value= 0)
classe = IntVar(master= window, value= 0)
age = IntVar(master= window, value= 0)
état = IntVar(master= window, value= 0)

#création de la fenêtre
window.title("Statistiques du Titanic")
window.geometry("710x444")
window.config(background = "#048B9A")
window.iconbitmap("titanic.ico")
window.resizable(width=False,height=False)

#image de fond
image_fond = PhotoImage(file = "fond_papier.gif")
image_fond2 = PhotoImage(file = "fond2.gif")

#image du bouton
image_bouton = PhotoImage(file="bouton_fond2.gif")

#création de l'image de fond et du Titre
canvas_pour_image = Canvas(window,width=1300,height=813, bg='white',bd=0,highlightthickness=0)
canvas_pour_image.create_image(0,0,image = image_fond,anchor='nw')
canvas_pour_image.create_text(20,150,text="Bienvenue dans l'applicationde statistiques du Titanic",\
                             font=("Script",35),anchor='nw')
canvas_pour_image.place(x=0,y=0)

menu_bar = Menu(window)
menu_fill = Menu(menu_bar, tearoff=0)
menu_fill.add_command(label="Quitter", command=Quitter)
menu_bar.add_cascade(label="Fonction", menu=menu_fill)
window.config(menu=menu_bar)

#boutton "commencer l'aventure" ansi que son placement dans la fenêtre
button1 = Button(window,image= image_bouton,borderwidth=0,\
                                highlightthickness=0,command=CreateNewWindow)
my_button1_window = canvas_pour_image.create_window\
                    (255,450/2,anchor = "nw",window=button1)


#automatisation de la mise en route des bulles
bulle()
#affichage global(obligatoire)
window.mainloop()
