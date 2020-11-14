'''
Created on 05/08/2020

Snake controlled and used to play the game

@author: Carlos Portela
'''
from copy import copy
from Logic.Cell import Cell

UP = "Up"
DOWN = "Down"
LEFT = "Left"
RIGHT = "Right"
RED_COLOR = "red"
GREEN_COLOR = "green"
BLUE_COLOR = "blue"
BLACK_COLOR = "black"
STEP_SIZE = 20
EYE_MARGIN = 2

class Snake:

    def __init__(self,initPosX=0,initPosY=0,size=4,speed=9):
        self.size      = size
        self.speed     = speed
        self.posX      = initPosX
        self.posY      = initPosY
        self.direction = RIGHT
        self.eyesDirection = RIGHT
        self.Cells = []

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

    def getHead(self):
        for cell in self.Cells:
            if cell.getIndex() == 1:
                return cell

    def getTail(self):
        return self.Cells[-1]

    def getPosX(self):
        return self.getHead().getPosX()

    def getPosY(self):
        return self.getHead().getPosY()
    
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
        
    def addEyesToCells(self,newCell):
        self.Cells.insert(0,newCell)
        
    def cellCollision(self,cell1,cell2):
        return (cell1.getPosX() == cell2.getPosX()) and (cell1.getPosY() == cell2.getPosY())
        
    def snakeBodyCollision(self):
        head = self.getHead()
        for cell in self.Cells:
            if cell.getIndex() > 1:
                if self.cellCollision(head,cell):
                    return True
        return False


    def removesSnakeEyes(self,screen):
        eyes = []
        for cell in self.Cells:
            if cell.getIndex() == 0:
                screen.genCanvas.delete(cell.getObject())
                eyes.append(cell)

        self.Cells.remove(eyes[0])
        self.Cells.remove(eyes[1])


    def createSnakeEyes(self,screen,direction,head):
        eyeXSize  = 7
        eyeYSize  = 6

        if direction == UP:
            eye1InitialPosX1 = head.getPosX()+EYE_MARGIN
            eye1InitialPosX2 = eye1InitialPosX1+eyeXSize
            eye1InitialPosY1 = head.getPosY()+EYE_MARGIN
            eye1InitialPosY2 = eye1InitialPosY1+eyeYSize

            eye2InitialPosX1 = eye1InitialPosX1+eyeXSize+EYE_MARGIN
            eye2InitialPosX2 = eye1InitialPosX1+eyeXSize+EYE_MARGIN+eyeXSize
            eye2InitialPosY1 = eye1InitialPosY1
            eye2InitialPosY2 = eye2InitialPosY1+eyeYSize
        elif direction == RIGHT:
            eye1InitialPosX1 = head.getPosX()+eyeXSize+EYE_MARGIN+EYE_MARGIN
            eye1InitialPosX2 = eye1InitialPosX1+eyeYSize
            eye1InitialPosY1 = head.getPosY()+EYE_MARGIN
            eye1InitialPosY2 = eye1InitialPosY1+eyeXSize
            
            eye2InitialPosX1 = eye1InitialPosX1
            eye2InitialPosX2 = eye1InitialPosX2
            eye2InitialPosY1 = eye1InitialPosY2+EYE_MARGIN
            eye2InitialPosY2 = eye2InitialPosY1+eyeXSize
        elif direction == LEFT:
            eye1InitialPosX1 = head.getPosX()+EYE_MARGIN
            eye1InitialPosX2 = eye1InitialPosX1+eyeYSize
            eye1InitialPosY1 = head.getPosY()+EYE_MARGIN
            eye1InitialPosY2 = eye1InitialPosY1+eyeXSize
            
            eye2InitialPosX1 = eye1InitialPosX1
            eye2InitialPosX2 = eye1InitialPosX2
            eye2InitialPosY1 = eye1InitialPosY2+EYE_MARGIN
            eye2InitialPosY2 = eye2InitialPosY1+eyeXSize
        elif direction == DOWN:
            eye1InitialPosX1 = head.getPosX()+EYE_MARGIN
            eye1InitialPosX2 = eye1InitialPosX1+eyeXSize
            eye1InitialPosY1 = head.getPosY()+eyeYSize+EYE_MARGIN+EYE_MARGIN
            eye1InitialPosY2 = eye1InitialPosY1+eyeYSize

            eye2InitialPosX1 = eye1InitialPosX2+EYE_MARGIN
            eye2InitialPosX2 = eye2InitialPosX1+eyeXSize
            eye2InitialPosY1 = eye1InitialPosY1
            eye2InitialPosY2 = eye1InitialPosY2
            
        eye1 = screen.createRectangleOnCanvas(eye1InitialPosX1,eye1InitialPosY1,eye1InitialPosX2,eye1InitialPosY2,eyes=True)
        eye2 = screen.createRectangleOnCanvas(eye2InitialPosX1,eye2InitialPosY1,eye2InitialPosX2,eye2InitialPosY2,eyes=True)

        self.addEyesToCells(Cell(0,eye1InitialPosX1,eye1InitialPosY1,eye1))
        self.addEyesToCells(Cell(0,eye2InitialPosX1,eye1InitialPosY1,eye2))


    def replaceHead(self,newHead):
        for i in range(len(self.Cells)):
            self.Cells[i].incrementIndex()

        newHead.setIndex(1)
        self.Cells.insert(0,newHead)
        
    
    def growSnake(self,screen):
        currentTail = self.getTail()
        posX,posY = 0,0

        if self.direction == UP:
            posX = currentTail.getPosX()
            posY = currentTail.getPosY() - STEP_SIZE
        elif self.direction == DOWN:
            posX = currentTail.getPosX()
            posY = currentTail.getPosY() + STEP_SIZE
        elif self.direction == LEFT:
            posX = currentTail.getPosX() - STEP_SIZE
            posY = currentTail.getPosY()
        elif self.direction == RIGHT:
            posX = currentTail.getPosX() + STEP_SIZE
            posY = currentTail.getPosY()

        newObj = screen.createRectangleOnCanvas(posX,posY,posX+STEP_SIZE,posY+STEP_SIZE)
        newTail = Cell(currentTail.getIndex()+1,posX,posY,newObj)
        self.addToCells(newTail)


    def popTail(self):
        return self.Cells.pop()
    
    
    def performStep(self,newDir,newHead):
        if newDir == UP:
            if self.direction != DOWN:
                newHead.setStepY(-STEP_SIZE)
                newHead.setPosY(newHead.getPosY() - STEP_SIZE)
                self.setDirection(UP)
            else:
                newHead.setStepY(+STEP_SIZE)
                newHead.setPosY(newHead.getPosY() + STEP_SIZE)
                self.eyesDirection = DOWN
        
        elif newDir == DOWN:
            if self.direction != UP:
                newHead.setStepY(+STEP_SIZE)
                newHead.setPosY(newHead.getPosY() + STEP_SIZE)
                self.setDirection(DOWN)
            else:
                newHead.setStepY(-STEP_SIZE)
                newHead.setPosY(newHead.getPosY() - STEP_SIZE)
                self.eyesDirection = UP
                
        elif newDir == LEFT:
            if self.direction != RIGHT:
                newHead.setStepX(-STEP_SIZE)
                newHead.setPosX(newHead.getPosX() - STEP_SIZE)
                self.setDirection(LEFT)
            else:
                newHead.setStepX(+STEP_SIZE)
                newHead.setPosX(newHead.getPosX() + STEP_SIZE)
                self.eyesDirection = RIGHT
        
        elif newDir == RIGHT:
            if self.direction != LEFT:
                newHead.setStepX(+STEP_SIZE)
                newHead.setPosX(newHead.getPosX() + STEP_SIZE)
                self.setDirection(RIGHT)
            else:
                newHead.setStepX(-STEP_SIZE)
                newHead.setPosX(newHead.getPosX() - STEP_SIZE)
                self.eyesDirection = LEFT
        
        return newHead


    def turn(self,newDir,screen):
        newHead = copy(self.getHead())
        self.eyesDirection = newDir

        newObject = screen.createRectangleOnCanvas(newHead.getPosX(),newHead.getPosY(),
                                                   newHead.getPosX()+STEP_SIZE,newHead.getPosY()+STEP_SIZE)
        newHead.setObject(newObject)
        newHead = self.performStep(newDir,newHead)

        self.replaceHead(newHead)
        self.removesSnakeEyes(screen)
        self.createSnakeEyes(screen,self.eyesDirection,newHead)

        tail = self.popTail()
        screen.genCanvas.delete(tail.getObject())


    def move(self,command,screen):
        if command == UP:
            self.turn(UP,screen)
        elif command == DOWN:
            self.turn(DOWN,screen)
        elif command == LEFT:
            self.turn(LEFT,screen)
        elif command == RIGHT:
            self.turn(RIGHT,screen)
