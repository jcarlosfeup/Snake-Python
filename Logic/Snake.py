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
    
    def setSpeed(self,newSpeed):
        self.speed = newSpeed
        
    def setSize(self,newSize):
        self.size = newSize
    
    def setPosX(self,positionX):
        self.posX = positionX
        
    def setPosY(self,positionY):
        self.posY = positionY
        
    def setCanvas(self,canvas):
        self.canvas = canvas
        
    def setRectangle(self,rectangle):
        self.rectangle = rectangle
        
    def setDirection(self,newDir):
        self.direction = newDir

    def move(self,direction):
        if direction == "UP":
            self.setPosY(self.getPosY()+(1*self.getSpeed()))
        elif direction == "DOWN":
            self.setPosY(self.getPosY()-(1*self.getSpeed()))
        elif direction == "LEFT":
            self.setPosX(self.getPosX()-(1*self.getSpeed()))
        elif direction == "RIGHT":
            self.setPosX(self.getPosX()+(1*self.getSpeed()))
        
    