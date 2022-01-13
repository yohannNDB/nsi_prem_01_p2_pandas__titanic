# Créé par fortn, le 31/12/2021 en Python 3.7
from tkinter import *
from random import randint,choice
import string


window = Tk()
"""
image_fond =image = PhotoImage(file = "fond brule.png")

window.title("Statistiques du Titanic")
window.geometry("1300x800")
window.config(background = image_fond)
window.iconbitmap("titanic.ico")
"""
label_window = Label(window,text="Bienvenue sur l'application de statistique du Titanic",font=("Courrier",40),bg='#048B9A',fg='white')








label_frame_options = Label(window,text="Les critères",font=("Courrier",30),bg='#048B9A',fg='white')

# caracteristiques des titre des themes des options
label_frame_theme1 = Label(window,text="   - Le sexe des passagers",font=("Courrier",25),bg='#048B9A',fg='white')
label_frame_theme2 = Label(window,text="   - La classe des passagers",font=("Courrier",25),bg='#048B9A',fg='white')
label_frame_theme3 = Label(window,text="   - L'age des passagers",font=("Courrier",25),bg='#048B9A',fg='white')

#caractéristiques des options du theme 1
case_theme1_option1 = Checkbutton(window,text ='Homme',bg='#048B9A',fg='white',font=("Courrier",15),activeforeground='white',activebackground='#048B9A')
case_theme1_option2 = Checkbutton(window,text ='Femme',bg='#048B9A',fg='white',font=("Courrier",15),activeforeground='white',activebackground='#048B9A')

#caractéristiques des options du theme 2

case_theme2_option1 = Checkbutton(window,text ='1ère Classe',bg='#048B9A',fg='white',font=("Courrier",15),activeforeground='white',activebackground='#048B9A')
case_theme2_option2 = Checkbutton(window,text ='2ème Classe',bg='#048B9A',fg='white',font=("Courrier",15),activeforeground='white',activebackground='#048B9A')
case_theme2_option3 = Checkbutton(window,text ='3ème Classe',bg='#048B9A',fg='white',font=("Courrier",15),activeforeground='white',activebackground='#048B9A')

#caractéristiques des options du theme 3
case_theme3_option1 = Checkbutton(window,text ='- de 18 ans',bg='#048B9A',fg='white',font=("Courrier",15),activeforeground='white',activebackground='#048B9A')
case_theme3_option2 = Checkbutton(window,text =' 18 à 50 ans',bg='#048B9A',fg='white',font=("Courrier",15),activeforeground='white',activebackground='#048B9A')
case_theme3_option3 = Checkbutton(window,text =' plus de 50 ans',bg='#048B9A',fg='white',font=("Courrier",15),activeforeground='white',activebackground='#048B9A')

#caractéristiques du bouton "rechercher"

button_rechercher = Button(window,text='rechercher',bg='#048B9A',fg='white',font=("Courrier",15),activeforeground='white',activebackground='#048B9A')



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

image = PhotoImage(file = "souligner_chic.png")
canvas = Canvas(window,width=600,height=300, bg='#048B9A', bd = 0)
canvas.create_image(200/2,200/2,image = image)
canvas.grid(row=1,column=0,sticky=N)


label_window.grid(row=0,column=0)








window.mainloop()