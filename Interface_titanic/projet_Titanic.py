# Créé par fortn, le 31/12/2021 en Python 3.7
from tkinter import *
from random import randint,choice
import string
import tkinter as tk
import time
import tkinter.font as tkFont
import random

#fenêtre
window = Tk()

#variables des cases cochées
oui_homme = IntVar()
oui_femme = IntVar()
oui_1ere_classe = IntVar()
oui_2ere_classe = IntVar()
oui_3ere_classe = IntVar()
oui_moins_de_18= IntVar()
oui_de_18_a_50  = IntVar()
oui_plus_de_50ans = IntVar()


#création de la fenêtre
window.title("Statistiques du Titanic")
window.geometry("700x450")
window.config(background = "#048B9A")
window.iconbitmap("titanic.ico")
window.resizable(width=False,height=False)


#image de fond
image = PhotoImage(file = "fond_papier.gif")

#création de l'image de fond et du Titre
canvas_pour_image = Canvas(window,width=700,height=450, bg='white',bd=0,highlightthickness=0)
canvas_pour_image.create_image(0,0,image = image,anchor='nw')
canvas_pour_image.create_text(20,150,text="Bienvenue dans l'application de statistiques du Titanic",font=("Script",35),anchor='nw')
canvas_pour_image.pack(fill='both',expand=True)

#(fonction en cours)weight_au_harsard_pour_bulles = random.randint(0,200)


#création des bulles ainsi qu leurs déplacements
def bulle():
    for i in range (10):
        #image des bulles
        image_de_la_bulle= PhotoImage(file = "bulle_fond.gif",width=110,height=300)
        image_de_la_petite_bulle= PhotoImage(file = "bulle_fond.gif",width=110,height=100)


        #creation de trois canvas différents pour acceuillir les bulle 1,2,3
        bulle = canvas_pour_image.create_image(0,450,image= image_de_la_bulle,anchor='nw')
        canvas_pour_image.pack(fill='both',expand=True)


        bulle2 = canvas_pour_image.create_image(500,450,image= image_de_la_bulle,anchor='nw')
        canvas_pour_image.pack(fill='both',expand=True)

        #cette bulle utilise une image différente mais est toujours placé à un endroit voulu
        bulle3 = canvas_pour_image.create_image(200,450,image= image_de_la_petite_bulle,anchor='nw')
        canvas_pour_image.pack(fill='both',expand=True)

        #déplacement de la bulle 1
        i =0
        while i<45:
            canvas_pour_image.move(bulle,0,-20)
            time.sleep(0.1)
            canvas_pour_image.update()
            i=i+1
        time.sleep(8)
        i=0
        #déplacement de la bulle 2
        while i<45:
            canvas_pour_image.move(bulle2,0,-20)
            time.sleep(0.1)
            canvas_pour_image.update()
            i=i+1
        time.sleep(8)
        i=0
        #déplacement de la bulle 3
        while i<45:
            canvas_pour_image.move(bulle3,0,-20)
            time.sleep(0.1)
            canvas_pour_image.update()
            i=i+1
        time.sleep(4)


image_bouton = PhotoImage(file="bouton_fond2.gif")



#fonction qui destruit l'accueil et remplace par les statistiques
def CreateNewWindow():
    #destruction de l'image du fond et de l'image+texte
    canvas_pour_image.pack_forget()







    #création d'une nouvelle fenêtre avec une nouvelle taille
    window.title("Statistiques du Titanic")
    window.geometry("1300x600")
    window.config(background = "#048B9A")
    window.iconbitmap("titanic.ico")
    window.resizable(width=True,height=True)

    # caractéritiques du pseudo titre des statistiques
    label_frame_options = Label(window,text="Les critères",font=("Courrier",30),bg='#048B9A',fg='white')

# caracteristiques des titre des themes des options

    label_frame_theme1 = Label(window,text="   - Le sexe des passagers",font=("Courrier",25),bg='#048B9A',fg='white')
    label_frame_theme2 = Label(window,text="   - La classe des passagers",font=("Courrier",25),bg='#048B9A',fg='white')
    label_frame_theme3 = Label(window,text="   - L'age des passagers",font=("Courrier",25),bg='#048B9A',fg='white')

#caractéristiques des options du theme 1
    case_theme1_option1 = Checkbutton(window,text ='Homme',bg='#048B9A',fg='black',font=("Courrier",15),activeforeground='white',activebackground='#048B9A',variable=oui_homme)
    case_theme1_option2 = Checkbutton(window,text ='Femme',bg='#048B9A',fg='black',font=("Courrier",15),activeforeground='white',activebackground='#048B9A',variable=oui_femme)

#caractéristiques des options du theme 2

    case_theme2_option1 = Checkbutton(window,text ='1ère Classe',bg='#048B9A',fg='black',font=("Courrier",15),activeforeground='white',activebackground='#048B9A',variable=oui_1ere_classe)
    case_theme2_option2 = Checkbutton(window,text ='2ème Classe',bg='#048B9A',fg='black',font=("Courrier",15),activeforeground='white',activebackground='#048B9A',variable=oui_2ere_classe)
    case_theme2_option3 = Checkbutton(window,text ='3ème Classe',bg='#048B9A',fg='black',font=("Courrier",15),activeforeground='white',activebackground='#048B9A',variable=oui_3ere_classe)

#caractéristiques des options du theme 3
    case_theme3_option1 = Checkbutton(window,text ='- de 18 ans',bg='#048B9A',fg='black',font=("Courrier",15),activeforeground='white',activebackground='#048B9A',variable=oui_moins_de_18)
    case_theme3_option2 = Checkbutton(window,text =' 18 à 50 ans',bg='#048B9A',fg='black',font=("Courrier",15),activeforeground='white',activebackground='#048B9A',variable=oui_de_18_a_50)
    case_theme3_option3 = Checkbutton(window,text =' plus de 50 ans',bg='#048B9A',fg='black',font=("Courrier",15),activeforeground='white',activebackground='#048B9A',variable=oui_plus_de_50ans)

#caractéristiques du bouton "rechercher"

    button_rechercher = Button(window,text='rechercher',bg='#048B9A',fg='white',font=("Courrier",20),activeforeground='white',activebackground='#048B9A')



    label_frame_options.grid(row=4,column=0,sticky=W)

#placements des titres du theme 1 des options
    label_frame_theme1.grid(row=5,column=0,sticky=W)

#placements des options du theme 1
    case_theme1_option1.grid(row=6,column=0,sticky=W)
    case_theme1_option2.grid(row=7,column=0,sticky=W)

#placements des titres du theme 2 des options
    label_frame_theme2.grid(row=8,column=0,sticky=W)

#placements des options du theme 2
    case_theme2_option1.grid(row=9,column=0,sticky=W)
    case_theme2_option2.grid(row=10,column=0,sticky=W)
    case_theme2_option3.grid(row=11,column=0,sticky=W)

#placements des titres du theme 3 des options
    label_frame_theme3.grid(row=12,column=0,sticky=W)

#placements des options du theme 3
    case_theme3_option1.grid(row=13,column=0,sticky=W)
    case_theme3_option2.grid(row=14,column=0,sticky=W)
    case_theme3_option3.grid(row=15,column=0,sticky=W)

#placement du bouton "rechercher"
    button_rechercher.grid(row=17,column=0,sticky=W)


"""
image = PhotoImage(file = "souligner_chic.png")
canvas = Canvas(window,width=600,height=300, bg='#048B9A', bd = 0)
canvas.create_image(200/2,200/2,image = image)
canvas.grid(row=1,column=0,sticky=N)
"""

"""
label_window.grid(row=0,column=0)


canvas.grid(row=0,column=0)

"""

#boutton "commencer l'aventure" ansi que son placement dans la fenêtre
button1 = Button(window,image= image_bouton,borderwidth=0,highlightthickness=0,command=CreateNewWindow)
my_button1_window = canvas_pour_image.create_window(255,450/2,anchor = "nw",window=button1)




#création du menu en haut

menu_bar = Menu(window)

menu_fill = Menu(menu_bar,tearoff=0)
menu_fill.add_command(label="Choix des statistiques",command=CreateNewWindow)
menu_fill.add_command(label="Quitter",command=window.quit)
menu_bar.add_cascade(label="Fonction",menu=menu_fill)

window.config(menu=menu_bar)


#automatisation de la mise en route des bulles
bulle()
#affichage global(obligatoire)
window.mainloop()