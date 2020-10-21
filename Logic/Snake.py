'''
Created on 05/08/2020

Snake controlled and used to play the game

@author: Carlos Portela
'''

class Snake:

    def __init__(self,initPosX=0,initPosY=0,size=3,speed=3):
        self.size      = size
        self.speed     = speed
        self.posX      = initPosX
        self.posY      = initPosY
        self.direction = "R"    #start direction is right
        self.Cells = []

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY
    
    def getSize(self):
        return self.size
    
    def getSpeed(self):
        return self.speed
    
    def getCanvas(self):
        return self.canvas

    def getRectangle(self):
        return self.rectangle
    
    def getDirection(self):
        return self.direction
    
    def getCells(self):
        return self.Cells
    
    def setSpeed(self,newSpeed):
        self.speed = newSpeed
        
    def setSize(self,newSize):
        self.size = newSize
    
    def setPosX(self,positionX):
        self.posX = positionX
        
    def setPosY(self,positionY):
        self.posY = positionY
        
    def setDirection(self,newDir):
        self.direction = newDir

    def setCells(self,newCells):
        self.Cells = newCells
        
    def addToCells(self,newCell):
        self.Cells.append(newCell)

    def move(self,direction):
        if direction == "U":   #up
            for cell in self.Cells:  #TODO
                pass
                
            self.setPosY(self.getPosY()+(1*self.getSpeed()))

        
    