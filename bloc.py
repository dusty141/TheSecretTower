#-*-coding:Utf-8 -*
#    TheSecretTower
#    Copyright (C) 2011 Pierre SURPLY
#
#    This file is part of TheSecretTower.
#
#    TheSecretTower is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    TheSecretTower is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with TheSecretTower.  If not, see <http://www.gnu.org/licenses/>.

# Auteur : Pierre Surply

from element import *

import pygame
from pygame.locals import *

from time import *
import random
import copy
# Constantes
import const

# Bloc
class Bloc(Element):

    def __init__(self, picture):
        Element.__init__(self)
        self.vie = 5
        self.last = time()
        self.picture = picture
        self.set_image()
        self.fire = False

    def anim(self):
        if self.picture == 2:
            if time() - self.last > 1: 
                image = copy.copy(const.vide)
                rect = pygame.Rect(0,random.randint(0, 4)*50, 50,50)
                image.blit(const.sprite_lave, (0,0), rect)
                self.changer_image(image)
                self.last = time()

        if self.picture == 13:
            if time()-self.last > 0.1:
                image = copy.copy(const.vide)
                rect = pygame.Rect(0,random.randint(0, 3)*50, 50,50)
                image.blit(const.sprite_torch, (0,0), rect)
                self.changer_image(image)
                self.last = time()
        if self.picture == 23:
            if time() > self.last and self.fire:
                image = copy.copy(const.vide)
                rect = pygame.Rect(0,200, 50,50)
                image.blit(const.sprite_bloc, (0,0), rect)
                self.changer_image(image)
                self.fire = False
            elif time() < self.last and not self.fire:
                image = copy.copy(const.vide)
                rect = pygame.Rect(50,200, 50,50)
                image.blit(const.sprite_bloc, (0,0), rect)
                self.changer_image(image)
                self.fire = True
                
                

    def hit(self, damage):
        self.vie -= damage
        self.set_image()
        if self.vie > 0:
            return False
        else:
            return True

    def set_image(self):
        picture = self.picture
        image = copy.copy(const.vide)
        rect = pygame.Rect(0,0, 50,50)
        if picture == 0:
            rect = pygame.Rect(0,0, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 1:
            rect = pygame.Rect(50,0, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 2:
            rect = pygame.Rect(0,random.randint(0, 3)*50, 50,50)
            image.blit(const.sprite_lave, (0,0), rect)
        elif picture == 3:
            image = pygame.Surface((50,20))
            rect = pygame.Rect(100,0, 50,20)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 4:
            rect = pygame.Rect(150,0, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 5:
            rect = pygame.Rect(200,0, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 6:
            rect = pygame.Rect(0,50, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 7:
            rect = pygame.Rect(50,50, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 8:
            rect = pygame.Rect(100,50, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 9:
            rect = pygame.Rect(150,50, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 10:
            rect = pygame.Rect(200,50, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 11:
            rect = pygame.Rect(0,100, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 12:
            rect = pygame.Rect(0,150, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 13:
            rect = pygame.Rect(0,random.randint(0, 3)*50, 50,50)
            image.blit(const.sprite_torch, (0,0), rect)
        elif picture == 14:
            rect = pygame.Rect(50,100, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 15:
            rect = pygame.Rect(100,100, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 16:
            rect = pygame.Rect(150,100, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 17:
            rect = pygame.Rect(200,100, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 18:
            rect = pygame.Rect(0,150, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 19:
            rect = pygame.Rect(50,150, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 20:
            rect = pygame.Rect(100,150, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 21:
            rect = pygame.Rect(150,150, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 22:
            rect = pygame.Rect(200,150, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        elif picture == 23:
            rect = pygame.Rect(0,200, 50,50)
            image.blit(const.sprite_bloc, (0,0), rect)
        
        # Damage
        if self.vie != 5:
            rect = pygame.Rect(0,int(4-self.vie)*50, 50,50)
            image.blit(const.sprite_degats, (0,0), rect)
        self.changer_image(image)
    
class BlocDisp(Bloc):
    def __init__(self, picture, begin = 0):
        Bloc.__init__(self, picture)
        self.begin = begin
        self.last_change = time()+begin
        self.etat = True

    def disp(self):
        if (time() - self.last_change > 3):
            self.last_change = time()
            if (self.etat == True):
                self.etat = False
            elif (self.etat == False):
                self.etat = True
        
class BlocMouvant(Bloc):
    
    def __init__(self, picture, debut_x, debut_y, dep_x, dep_y):
        Bloc.__init__(self, picture)
        self.debut_x = debut_x
        self.debut_y = debut_y
        self.dep_x = dep_x
        self.dep_y = dep_y
        self.move_el(debut_x, debut_y)
        self.aller = True

    def move(self):
        if self.aller:
            if self.x >= (self.debut_x+self.dep_x) and self.y >= (self.debut_y+self.dep_y):
                self.aller = False
            if self.x < self.dep_x+self.debut_x:
                self.move_el(1,0)
            if self.y < self.dep_y+self.debut_y:
                self.move_el(0,1)
            
        else:
            if self.x <= (self.debut_x) and self.y <= (self.debut_y):
                self.aller = True
            if self.x > self.debut_x:
                self.move_el(-1,0)
            if self.y > self.debut_y:
                self.move_el(0,-1)



class BlocDanger(Bloc):
    
    def __init__(self, picture, atk):
        Bloc.__init__(self, picture)
        self.atk = atk



# etat
#      0 = map--
#      1 = map++
#      2 = map=target
class Porte(Bloc):
    
    def __init__(self, picture, etat, id=0, target=0):
        Bloc.__init__(self, picture)
        self.etat = etat
        self.id = id
        self.target = target

class Terre(Bloc):
    def __init__(self, picture):
        Bloc.__init__(self, picture)


class Stone(Bloc):
    def __init__(self, picture):
        Bloc.__init__(self, picture)

class Wood(Bloc):
    def __init__(self, picture):
        Bloc.__init__(self, picture)

class Echelle(Wood):
    def __init__(self, picture):
        Bloc.__init__(self, picture)

class Atelier(Wood):
    def __init__(self, picture):
        Bloc.__init__(self, picture)



class Forge(Stone):
    def __init__(self, picture):
        Bloc.__init__(self, picture)

class Coal(Stone):
    def __init__(self, picture):
        Bloc.__init__(self, picture)

class Copper(Stone):
    def __init__(self, picture):
        Bloc.__init__(self, picture)

class Iron(Stone):
    def __init__(self, picture):
        Bloc.__init__(self, picture)

class Titanium(Stone):
    def __init__(self, picture):
        Bloc.__init__(self, picture)

class Gold(Stone):
    def __init__(self, picture):
        Bloc.__init__(self, picture)
class Diamond(Stone):
    def __init__(self, picture):
        Bloc.__init__(self, picture)
class Tin(Stone):
    def __init__(self, picture):
        Bloc.__init__(self, picture)
class Uranium(Stone):
    def __init__(self, picture):
        Bloc.__init__(self, picture)

class Deco(Bloc):
    def __init__(self, picture):
        Bloc.__init__(self, picture)

class Torch(Deco):
    def __init__(self, picture):
        Bloc.__init__(self, picture)

class Sign(Deco):
    def __init__(self, picture, txt):
        Bloc.__init__(self, picture)
        self.txt = txt

class Furnace(Stone):
    def __init__(self, picture):
        Bloc.__init__(self, picture)

        
    



