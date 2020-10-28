'''
Created on 05/08/2020

Snake controlled and used to play the game

@author: Carlos Portela
'''
from copy import copy

STEP_SIZE = 20

UP = "Up"
DOWN = "Down"
LEFT = "Left"
RIGHT = "Right"

class Snake:

    def __init__(self,initPosX=0,initPosY=0,size=3,speed=3):
        self.size      = size
        self.speed     = speed
        self.posX      = initPosX
        self.posY      = initPosY
        self.direction = RIGHT    #right direction is the default
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
        
    def replaceHead(self,newHead):
        
        #updates cells indexes
        for i in range(len(self.Cells)):
            self.Cells[i].incrementIndex()
        
        self.Cells.insert(0, newHead)
        self.setCells(self.Cells)
        
    def popTail(self):
        return self.Cells.pop()

    def turn(self,newDir,screen):
        newHead = copy(self.Cells[0])     #gets current head and makes a new copy
        
        newObject = screen.genCanvas.create_rectangle(newHead.getPosX(),newHead.getPosY(),
                                                          newHead.getPosX()+screen.SNAKE_CELL_W,newHead.getPosY()+screen.SNAKE_CELL_H,
                                                          fill="red",outline="blue")
        newHead.setObject(newObject)

        if (self.direction in (UP,RIGHT,LEFT) and newDir == UP):
            print(newHead.getPosX())
            print(newHead.getPosY())
            newHead.setStepY(-STEP_SIZE)
            newHead.setPosY(newHead.getPosY() - STEP_SIZE)
        
        elif(self.direction in (DOWN,RIGHT,LEFT) and newDir == DOWN):
            newHead.setStepY(+STEP_SIZE)
            newHead.setPosY(newHead.getPosY() + STEP_SIZE)

        elif(self.direction in (LEFT,UP,DOWN) and newDir == LEFT):
            newHead.setStepX(-STEP_SIZE)
            newHead.setPosX(newHead.getPosX() - STEP_SIZE)
        
        elif(self.direction in (RIGHT,UP,DOWN) and newDir == RIGHT):
            newHead.setStepX(+STEP_SIZE)
            newHead.setPosX(newHead.getPosX() + STEP_SIZE)

        self.replaceHead(newHead)   #sets new snake head in the first position

        #removes tail from canvas and queue
        tail = self.popTail()
        screen.genCanvas.delete(tail.getObject())


    def move(self,key,screen):
        if key.keysym == UP:
            if self.getDirection() != DOWN:
                self.turn(UP,screen)
                self.setDirection(UP)
            
        elif key.keysym == DOWN:
            if self.getDirection() != UP:
                self.turn(DOWN,screen)
                self.setDirection(DOWN)
        
        elif key.keysym == LEFT:
            if self.getDirection() != RIGHT:
                self.turn(LEFT,screen)
                self.setDirection(LEFT)

        elif key.keysym == RIGHT:
            if self.getDirection() != LEFT:
                self.turn(RIGHT,screen)
                self.setDirection(RIGHT)
            