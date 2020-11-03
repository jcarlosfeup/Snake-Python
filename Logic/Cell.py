'''
Created on 22/10/2020

Cell that compose the Snake

@author: Carlos Portela
'''

class Cell:

    def __init__(self, index=0,posX=0,posY=0,obj=None):
        self.index = index
        self.posX = posX
        self.posY = posY
        self.stepX = 0
        self.stepY = 0
        self.obj  = obj

    def getIndex(self):
        return self.index

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY
    
    def getStepX(self):
        return self.stepX
    
    def getStepY(self):
        return self.stepY
    
    def getObject(self):
        return self.obj
    
    def setIndex(self,idx):
        self.index = idx
        
    def setPosX(self,posX):
        self.posX = posX
        
    def setPosY(self,posY):
        self.posY = posY
        
    def setStepX(self,x):
        self.stepX = x

    def setStepY(self,y):
        self.stepY = y
        
    def setObject(self,obj):
        self.obj = obj
        
    def incrementIndex(self):
        if self.index != 0:
            self.index = self.index + 1

    def resetSteps(self):
        self.stepX = 0
        self.stepY = 0