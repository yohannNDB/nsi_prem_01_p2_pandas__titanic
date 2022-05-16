# -*- coding: utf-8 -*-
"""

"""

from os import listdir
from os.path import isfile, join
import random
import time
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from jdlv_data import *
from jdlv_model import *
from jdlv_outils import *

def clean_grid (grid):
    for i in range (default_grid_size):
        for j in range (default_grid_size):
            grid.cases [i][j]['s'] = death_status
            grid.cases [i][j]['c'] = death_color
    return grid

def make_1(grid, i, j, color):
    try:
        grid = clean_grid (grid)
        cases = grid.cases
        for x in range (10):
            for y in range(4):
                color = 'white'
                if x == 0 or x == 1:
                    color  = 'red'
                if y == 2 or y == 3:
                    color = 'red'
                cases [i+x] [j+y] ['s'] = life_status
                cases [i+x] [j+y] ['c'] = color




    except:
        pass
    return grid

def make_2(grid, i, j, color):
    try:
        grid = clean_grid (grid)
        cases = grid.cases
        for x in range (10):
            for y in range(6):
                color = 'white'
                if x == 1 or x == 2 or x== 5 or x == 6 or x == 9 or x == 10:
                    color  = 'red'
                if  x == 7 or x == 8:
                    if y<2:
                        color = 'red'
                if x == 1 or x == 2 or x == 3 or x == 4 :
                    if y>4:
                        color = 'red'
                cases [i+x] [j+y] ['s'] = life_status
                cases [i+x] [j+y] ['c'] = color
    except:
        pass
    return grid

def make_3(grid, i, j, color):
    try:
        grid = clean_grid (grid)
        cases = grid.cases
        for x in range (10):
            for y in range(6):
                color = 'white'
                if x == 0 or x == 1 or x == 8 or x == 9:
                    color = 'red'
                if x==4 or x== 5:
                    if 1<y<6:
                        color = 'red'
                if y ==  4 or y == 5:
                    color = 'red'
                cases [i+x] [j+y] ['s'] = life_status
                cases [i+x] [j+y] ['c'] = color
    except:
        pass
    return grid


def apply_game_of_life_rules (grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            nbre_alive_voisins = count_alive_voisins (voisins)
            if nbre_alive_voisins == 3:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 2 or nbre_alive_voisins >= 5:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid



def apply_rules (grid, compteur):
    next_grid = grid
    if 1<compteur<20 :
            next_grid = make_3(grid,4,default_grid_size//2-3,'black')
    if 20<compteur<30:
            next_grid = apply_game_of_life_rules (grid)


    if 29<compteur<50:
            next_grid = make_2(grid,4,default_grid_size//2-3,'black')
    if 60<compteur<70:
            next_grid = apply_game_of_life_rules (grid)



    if 70<compteur<80:
            next_grid = make_1(grid,4,default_grid_size//2-2,'black')
    else:
            new_grid = apply_game_of_life_rules(grid)
    return next_grid



