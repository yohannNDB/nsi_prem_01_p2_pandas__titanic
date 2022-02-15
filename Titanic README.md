__Projet 2 NSI première__
                                                          
                                                        
Participants: Amir Kemache, Louis Milliers, Yohann Pouillieute, Maxence Guibal
                                                       
                                                       
__Information sur le naufrage du titanic__
![photo du titanic](http://c.files.bbci.co.uk/1C60/production/_118046270_gettyimages-877330410.jpg)

Le naufrage du Titanic est l'un des naufrages les plus tristement célèbres de l'histoire. 
Le Titanic est long de 269 mètres, large de 28 mètres et haut de 53 mètres, de la quille aux cheminées. Son tonnage brut est d'environ 46 000 tjb , soit 1 000 de plus que l'Olympic(ship-sister du titanic). Il nécessite environ 885 membres d'équipage, et peut transporter 2 471 passagers répartis en trois classes. 

Le 15 avril 1912, lors de son voyage inaugural, le RMS Titanic, largement considéré comme "insubmersible", a coulé après avoir heurté un iceberg. Malheureusement, il n'y avait pas assez de canots de sauvetage pour tout le monde à bord, ce qui a entraîné la mort de 1502 des 2224 passagers et membres d'équipage. Bien qu'il y ait eu une part de chance dans la survie, il semble que certains groupes de personnes aient eu plus de chances de survivre que d'autres.  

*Pour plus d'information sur le titanic voici quelques liens:*
* [wikipedia du titanic](https://en.wikipedia.org/wiki/Passengers_of_the_RMS_Titanic)
* [autre site en englais](http://mashable.com/2016/04/14/titanic-survivors)


__Modules utilisés__
             
* tkinter
* xlrd
* pandas
* matplotlib
* numpy



__Interface graphique:__ (louis, yohann)


* Création d'une fenêtre avec un titre un bouton "démarrer l'experience"
* un background avec des animations,puis un onglet déroulant offrant 2 possibilités:"nouvelle stat" et "quitter"
* quand "nouvelle stat" est choisie la fenêtre affiche des choix sur les informations contenues dans le graphique grâce à des boutons.


__Affichage et création des graphique:__ (maxence,amir)
         
* utilisation de pandas pour créer des graphiques
* utilisation de camembert:
```
def afficher(): 
    print (filtres()) 
    print (total_variables()) 
    fig = Figure(figsize = (8, 8)) 
    x = [filtres(), len(data.axes[0])] 
    plt.pie(x, labels = ['homme', 'femme'], 
    colors = ['red', '#40E0D0'],  
    explode = [0, 0], 
    autopct = lambda x: str(round(x, 2)) + '%',  
    pctdistance = 0.7, labeldistance = 1.4,  
    shadow = True)  
    #print(oui_1ere_classe.get()) 
    plt.show()    
```








