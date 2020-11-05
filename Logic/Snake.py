'''
Created on 05/08/2020

Snake controlled and used to play the game

@author: Carlos Portela
'''
from copy import copy
from Logic.Cell import Cell

STEP_SIZE = 20

UP = "Up"
DOWN = "Down"
LEFT = "Left"
RIGHT = "Right"

class Snake:

    def __init__(self,initPosX=0,initPosY=0,size=3,speed=2):
        self.size      = size
        self.speed     = speed
        self.posX      = initPosX
        self.posY      = initPosY
        #right direction is the default
        self.direction = RIGHT
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
        
    def removesSnakeEyes(self,screen):
        eyes = []
        for cell in self.Cells:
            if cell.getIndex() == 0:  #its an eye
                screen.genCanvas.delete(cell.getObject())
                eyes.append(cell)
                
        #removes eyes from snake object list
        self.Cells.remove(eyes[0])
        self.Cells.remove(eyes[1])


    def createSnakeEyes(self,screen,direction,head):
        eyeMargin = 2
        eyeXSize = 7
        eyeYSize = 6
        spaceBetween = 2
        
        #creates rectangles representing the eyes
        if direction == UP:
            eye1InitialPosX1 = head.getPosX()+eyeMargin
            eye1InitialPosX2 = eye1InitialPosX1+eyeXSize
            eye1InitialPosY1 = head.getPosY()+eyeMargin
            eye1InitialPosY2 = eye1InitialPosY1+eyeYSize

            eye2InitialPosX1 = eye1InitialPosX1+eyeXSize+spaceBetween
            eye2InitialPosX2 = eye1InitialPosX1+eyeXSize+spaceBetween+eyeXSize
            eye2InitialPosY1 = eye1InitialPosY1
            eye2InitialPosY2 = eye2InitialPosY1+eyeYSize
        elif direction == RIGHT:
            eye1InitialPosX1 = head.getPosX()+eyeXSize+spaceBetween+eyeMargin
            eye1InitialPosX2 = eye1InitialPosX1+eyeYSize
            eye1InitialPosY1 = head.getPosY()+eyeMargin
            eye1InitialPosY2 = eye1InitialPosY1+eyeXSize
            
            eye2InitialPosX1 = eye1InitialPosX1
            eye2InitialPosX2 = eye1InitialPosX2
            eye2InitialPosY1 = eye1InitialPosY2+spaceBetween
            eye2InitialPosY2 = eye2InitialPosY1+eyeXSize
        elif direction == LEFT:
            eye1InitialPosX1 = head.getPosX()+eyeMargin
            eye1InitialPosX2 = eye1InitialPosX1+eyeYSize
            eye1InitialPosY1 = head.getPosY()+eyeMargin
            eye1InitialPosY2 = eye1InitialPosY1+eyeXSize
            
            eye2InitialPosX1 = eye1InitialPosX1
            eye2InitialPosX2 = eye1InitialPosX2
            eye2InitialPosY1 = eye1InitialPosY2+spaceBetween
            eye2InitialPosY2 = eye2InitialPosY1+eyeXSize
        elif direction == DOWN:
            eye1InitialPosX1 = head.getPosX()+eyeMargin
            eye1InitialPosX2 = eye1InitialPosX1+eyeXSize
            eye1InitialPosY1 = head.getPosY()+eyeYSize+spaceBetween+eyeMargin
            eye1InitialPosY2 = eye1InitialPosY1+eyeYSize

            eye2InitialPosX1 = eye1InitialPosX2+spaceBetween
            eye2InitialPosX2 = eye2InitialPosX1+eyeXSize
            eye2InitialPosY1 = eye1InitialPosY1
            eye2InitialPosY2 = eye1InitialPosY2
            
        eye1 = screen.genCanvas.create_rectangle(eye1InitialPosX1,eye1InitialPosY1,
                                                 eye1InitialPosX2,eye1InitialPosY2,
                                                 fill="blue")

        eye2 = screen.genCanvas.create_rectangle(eye2InitialPosX1,eye2InitialPosY1,
                                                 eye2InitialPosX2,eye2InitialPosY2,
                                                 fill="blue")
        
        self.addEyesToCells(Cell(0,eye1InitialPosX1,eye1InitialPosY1,eye1))
        self.addEyesToCells(Cell(0,eye2InitialPosX1,eye1InitialPosY1,eye2))


    def replaceHead(self,newHead):
        #updates cells indexes
        for i in range(len(self.Cells)):
            self.Cells[i].incrementIndex()
        
        newHead.setIndex(1)
        self.Cells.insert(0, newHead)
        
    
    def growSnake(self,canvas):
        currentTail = self.getTail()
        posX = 0
        posY = 0

        if self.direction == UP:
            posX = currentTail.getPosX()
            posY = currentTail.getPosY() + STEP_SIZE
        elif self.direction == DOWN:
            posX = currentTail.getPosX()
            posY = currentTail.getPosY() - STEP_SIZE
        elif self.direction == LEFT:
            posX = currentTail.getPosX() + STEP_SIZE
            posY = currentTail.getPosY()
        elif self.direction == RIGHT:
            posX = currentTail.getPosX() - STEP_SIZE
            posY = currentTail.getPosY()
        
        newObj = canvas.create_rectangle(posX,posY,
                                        posX+STEP_SIZE,posY+STEP_SIZE,
                                        fill="red",outline="blue")
        
        newTail = Cell(currentTail.getIndex()+1,posX,posY,newObj) 
        self.addToCells(newTail)


    def popTail(self):
        return self.Cells.pop()


    def turn(self,newDir,screen):
        newHead = copy(self.getHead())
        
        newObject = screen.genCanvas.create_rectangle(newHead.getPosX(),newHead.getPosY(),
                                                          newHead.getPosX()+screen.SNAKE_CELL_W,newHead.getPosY()+screen.SNAKE_CELL_H,
                                                          fill="red",outline="blue")
        newHead.setObject(newObject)

        if newDir == UP:
            if self.direction != DOWN:
                newHead.setStepY(-STEP_SIZE)
                newHead.setPosY(newHead.getPosY() - STEP_SIZE)
                self.setDirection(UP)
            else:
                newHead.setStepY(+STEP_SIZE)
                newHead.setPosY(newHead.getPosY() + STEP_SIZE)
        
        elif newDir == DOWN:
            if self.direction != UP:
                newHead.setStepY(+STEP_SIZE)
                newHead.setPosY(newHead.getPosY() + STEP_SIZE)
                self.setDirection(DOWN)
            else:
                newHead.setStepY(-STEP_SIZE)
                newHead.setPosY(newHead.getPosY() - STEP_SIZE)
                
        elif newDir == LEFT:
            if self.direction != RIGHT:
                newHead.setStepX(-STEP_SIZE)
                newHead.setPosX(newHead.getPosX() - STEP_SIZE)
                self.setDirection(LEFT)
            else:
                newHead.setStepX(+STEP_SIZE)
                newHead.setPosX(newHead.getPosX() + STEP_SIZE)
        
        elif newDir == RIGHT:
            if self.direction != LEFT:
                newHead.setStepX(+STEP_SIZE)
                newHead.setPosX(newHead.getPosX() + STEP_SIZE)
                self.setDirection(RIGHT)
            else:
                newHead.setStepX(-STEP_SIZE)
                newHead.setPosX(newHead.getPosX() - STEP_SIZE)

        #sets new snake head in the first position
        self.replaceHead(newHead)
        
        #removes previous snake eyes and creates new ones
        self.removesSnakeEyes(screen)
        self.createSnakeEyes(screen,newDir,newHead)

        #removes tail from canvas and queue
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
