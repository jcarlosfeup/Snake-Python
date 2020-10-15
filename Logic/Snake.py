'''
Created on 05/08/2020

Snake controlled and used to play the game

@author: Carlos Portela
'''

class Snake:

    def __init__(self,initPosX,initPosY,size=3,speed=3):
        self.size = size
        self.speed = speed
        self.posX =  initPosX
        self.posY =  initPosY
    
    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY
    
    def getSize(self):
        return self.size
    
    def getSpeed(self):
        return self.speed
    
    def setSpeed(self,newSpeed):
        self.speed = newSpeed
        
    def setSize(self,newSize):
        self.size = newSize
    
    def setPosX(self,positionX):
        self.posX = positionX
        
    def setPosY(self,positionY):
        self.posY = positionY
        
    def move(self,direction):
        if direction == "UP":
            self.setPosY(self.getPosY()+(1*self.getSpeed()))
        elif direction == "DOWN":
            self.setPosY(self.getPosY()-(1*self.getSpeed()))
        elif direction == "LEFT":
            self.setPosX(self.getPosX()-(1*self.getSpeed()))
        elif direction == "RIGHT":
            self.setPosX(self.getPosX()+(1*self.getSpeed()))
        
    