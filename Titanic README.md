# Projet 2 NSI première
                                                          
                                                        
Participants: Amir Kemache, Louis Milliers, Yohann Pouillieute, Maxence Guibal
## Notre projet:
A partir de la base de statistique du naufrage du titanic nous créons des graphiques comparant plusieurs filtres. Notre projet comporte 267 lignes de code.
                                                       
## __Informations sur le naufrage du titanic:__
![photo du titanic](http://c.files.bbci.co.uk/1C60/production/_118046270_gettyimages-877330410.jpg)

Le naufrage du Titanic est l'un des naufrages les plus tristement célèbres de l'histoire. 
Le Titanic est long de 269 mètres, large de 28 mètres et haut de 53 mètres, de la quille aux cheminées. Son tonnage brut est d'environ 46 000 tjb , soit 1 000 de plus que l'Olympic(ship-sister du titanic). Il nécessite environ 885 membres d'équipage, et peut transporter 2 471 passagers répartis en trois classes. 

Le 15 avril 1912, lors de son voyage inaugural, le RMS Titanic, largement considéré comme "insubmersible", a coulé après avoir heurté un iceberg. Malheureusement, il n'y avait pas assez de canots de sauvetage pour tout le monde à bord, ce qui a entraîné la mort de 1502 des 2224 passagers et membres d'équipage. Bien qu'il y ait eu une part de chance dans la survie, il semble que certains groupes de personnes aient eu plus de chances de survivre que d'autres.  

*Pour plus d'informations sur le titanic voici quelques liens:*
* [wikipedia du titanic](https://fr.wikipedia.org/wiki/Passagers_du_Titanic)
* [autre site en anglais](http://mashable.com/2016/04/14/titanic-survivors)


## __Modules utilisés:__
             
* tkinter
* xlrd
* pandas
* matplotlib
* numpy

## __Fichiers nécessaires:__
Pour faire fonctionner notre projet, il faut télécharger certaines images contenu dans:
* interface graphique
    * bouton_fond2.gif
    * bulle_fond.gif
    * fond2.gif
    * fond_papier.gif
    * titanic.ico
 * base de donnée: titanic3.xls


## __Interface graphique:__ (louis, yohann)


* Création d'une fenêtre avec un titre un bouton "commencer l'aventure" qui lance la fonction CreateNewWindow

![bouton commencer l'aventure](https://user-images.githubusercontent.com/91455596/154450920-27c0b2ac-292f-404f-bb2d-578d523042ad.PNG)
 
* un background avec des animations,puis un onglet déroulant offrant 2 possibilités:"nouvelle stat" et "quitter"

* quand "nouvelle stat" est choisie la fenêtre affiche des choix sur les informations contenues dans le graphique grâce à des boutons.
```
#caractéristiques des options du theme 4
case_theme4_option1 = Radiobutton(window,text ='Oui',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=1)
    case_theme4_option2 = Radiobutton(window,text ='Non',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=2)

    
 ```

## __Affichage et création des graphique:__ (maxence,amir)
         
* utilisation de pandas pour lire le fichier excel et pour faire un tri dans les données qui nous intéressent
* utilisation de camembert:
```
def afficher_graphique():
    x = filtres()
    plt.pie(x, labels = ['Population visée', 'Reste population'],
    colors = ['red', '#40E0D0'],
    explode = [0.3, 0],
    autopct = lambda x: str(round(x, 2)) + '%',
    pctdistance = 0.7, labeldistance = 1.4,
    shadow = True)
    plt.show()

```
*Les différents bug possible*
* animation des bulles peut faire crash la window(il suffit de relancer le programme en général ca marche, sinon raccourcir la boucle d'apparition des bulles)
* boutons mettent du temps a s'afficher (attendre l'apparition ne pas spam-click)





