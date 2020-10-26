'''
Created on 05/08/2020

Snake controlled and used to play the game

@author: Carlos Portela
'''

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
        self.Cells.insert(0, newHead)
        self.setCells(self.Cells)
        
    def popTail(self):
        self.Cells.pop()

    '''You hold all snake units in a list - that's already done. There are head and tail which are the first and the last elements of the list. So it is actually a queue.
    On each tick, determine the direction in which you should move. For example, if the direction is left, then next head coordinates will be at (-1,0) relative to current head.
    Insert new unit in the list at the head position with the coordinates determined in step 2.
    Remove the tail unit from the list (and from the screen).'''
    def turn(self,newDir):
        if self.direction == RIGHT and newDir == UP:
            currentHead = self.Cells[0]     #gets current head
            newPosX = 0
            newPosY = -STEP_SIZE
            currentHead.setPosY(newPosY)
            self.replaceHead(currentHead)   #sets new snake head in a different position
        
        print("BEfore POP " + str(len(self.Cells)))
        self.popTail()
        print("After POP " + str(len(self.Cells)))
        
        return (newPosX,newPosY)


    def move(self,key):
        x_offset, y_offset = 0, 0

        if key.keysym == UP:
            x_offset,y_offset = self.turn(UP)
            
        elif key.keysym == DOWN:
            y_offset = +STEP_SIZE
        elif key.keysym == LEFT:
            if self.snakeObj.getDirection() == 'R':
                pass
            else:
                x_offset = -STEP_SIZE
        elif key.keysym == RIGHT:
            x_offset = +STEP_SIZE
            
        return (x_offset,y_offset)
        
            