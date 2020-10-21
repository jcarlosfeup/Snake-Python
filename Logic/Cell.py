'''
Created on 22/10/2020

Cell that compose the Snake

@author: Carlos Portela
'''

class Cell:

    def __init__(self, index,posX,posY):
        self.index = index
        self.posX = posX
        self.posY = posY

    def getIndex(self):
        return self.index

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY
    
    def setIndex(self,idx):
        self.index = idx
        
    def setPosX(self,posX):
        self.posX = posX
        
    def setPosY(self,posY):
        self.posY = posY