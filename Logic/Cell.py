'''
Created on 22/10/2020

Cell that compose the Snake

@author: Carlos Portela
'''

class Cell:

    def __init__(self, index,posX,posY,obj):
        self.index = index
        self.posX = posX
        self.posY = posY
        self.obj  = obj

    def getIndex(self):
        return self.index

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY
    
    def getObject(self):
        return self.obj
    
    def setIndex(self,idx):
        self.index = idx
        
    def setPosX(self,posX):
        self.posX = posX
        
    def setPosY(self,posY):
        self.posY = posY
        
    def setObject(self,obj):
        self.obj = obj