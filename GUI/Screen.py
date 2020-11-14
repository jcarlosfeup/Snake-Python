'''
Created on 05/08/2020

GUI logic

@author: Carlos Portela
'''

import tkinter
import pygame
import Logic.Snake as SnakeConst
from random import Random
from PIL import Image, ImageTk
from Logic.Snake import Snake, BLACK_COLOR
from Logic.Cell import Cell

class Screen:

    def __init__(self,window):
        self.window = window
        self.snakeObj = Snake()
        self.foodObj = Cell()
        self.points = 0
        self.moving = False
        self.playing = True
        self.scoreObj = None
        self.instrObj = None
        
        self.initConstants()
        self.defineWindowSpecs()
        self.createCanvas()
        self.createImages()
        self.renderSnake()
        self.renderFood()
        self.initObjects()
        self.commands = {"Up": False,"Down": False, "Right": False, "Left": False}


    def initConstants(self):
        self.WINDOW_WIDTH  = 1000
        self.WINDOW_HEIGHT = 800
        self.WINDOW_TITLE  = "Snake"

        self.VERTICAL_MARGIN = 60
        self.HORIZONTAL_MARGIN = 20

        self.CANVAS_WIDTH = self.WINDOW_WIDTH
        self.CANVAS_HEIGHT = self.WINDOW_HEIGHT-self.VERTICAL_MARGIN

        self.SNAKE_CELL_W = 20
        self.SNAKE_CELL_H = 20

        self.SNAKE_INITIAL_POSX2 = (self.WINDOW_WIDTH)/2 + self.SNAKE_CELL_W
        self.SNAKE_INITIAL_POSY2 = (self.WINDOW_HEIGHT)/2 + self.SNAKE_CELL_H

        self.FOOD_W = self.SNAKE_CELL_W
        self.FOOD_H = self.SNAKE_CELL_H
        self.FOOD_SCORE = 10
        
        self.SCORE_MARGIN_VERTICAL = self.VERTICAL_MARGIN
        self.SCORE_MARGIN_HORIZONTAL = 11
        
        self.NORMAL_TEXT = "NORMAL"
        self.END_TEXT = "END"
        
        RESOURCES_FOLDER = "../Resources/"
        self.COLLISION_SOUND = RESOURCES_FOLDER + "snakeCollision.wav"
        self.MOVE_SOUND = RESOURCES_FOLDER + "snakeMovement.wav"
        self.EAT_SOUND  = RESOURCES_FOLDER + "snakeEat.wav"
        self.APPLE_DIR  = RESOURCES_FOLDER + "apple.png"
        self.KEYS_DIR   = RESOURCES_FOLDER + "keys.png"
        self.RETURN_DIR = RESOURCES_FOLDER + "return.png"
        
        self.FONT_TEXT = "Times 25 bold"


    def initObjects(self):
        self.snakeObj.setPosX(self.SNAKE_INITIAL_POSX2)
        self.snakeObj.setPosY(self.SNAKE_INITIAL_POSY2)


    def defineWindowSpecs(self):
        self.window.geometry(str(self.WINDOW_WIDTH) + "x" + str(self.WINDOW_HEIGHT))
        self.window.title(self.WINDOW_TITLE)
        self.window.resizable(0,0)


    def createCanvas(self):
        self.genCanvas = tkinter.Canvas(window, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT,bg=SnakeConst.GREEN_COLOR,highlightbackground=SnakeConst.BLACK_COLOR)
        self.genCanvas.pack()

        self.bottomCanvas = tkinter.Canvas(window, width=self.CANVAS_WIDTH, height=self.VERTICAL_MARGIN,highlightbackground=BLACK_COLOR)
        self.bottomCanvas.pack()


    def createImages(self):
        apple = Image.open(self.APPLE_DIR)
        apple = apple.resize((self.FOOD_H, self.FOOD_W), Image.ANTIALIAS)

        self.IMG_APPLE  = ImageTk.PhotoImage(apple)
        self.IMG_KEYS   = ImageTk.PhotoImage(Image.open(self.KEYS_DIR))
        self.IMG_RETURN = ImageTk.PhotoImage(Image.open(self.RETURN_DIR))


    def clearsSnake(self):
        for cell in self.snakeObj.getCells():
            self.genCanvas.delete(cell.getObject())
        self.snakeObj.setCells([])
        
    
    def createRectangleOnCanvas(self,posX1,posY1,posX2,posY2,eyes=False):
        if eyes:
            return self.genCanvas.create_rectangle(posX1,posY1,posX2,posY2,fill=SnakeConst.BLUE_COLOR)
        else:
            return self.genCanvas.create_rectangle(posX1,posY1,posX2,posY2,fill=SnakeConst.RED_COLOR,outline=SnakeConst.BLUE_COLOR)


    def renderSnake(self):
        def renderSnakeCell(index,posX1,posY1,posX2,posY2,eyes=False):
            cell = self.createRectangleOnCanvas(posX1,posY1,posX2,posY2,eyes)
            self.snakeObj.addToCells(Cell(index,posX1,posY1,cell))

        initialPosX = (self.WINDOW_WIDTH)/2 
        initialPosY = (self.WINDOW_HEIGHT)/2
        
        #head cell
        renderSnakeCell(1,initialPosX,initialPosY,self.SNAKE_INITIAL_POSX2,self.SNAKE_INITIAL_POSY2)

        eyeInitialPosX  = initialPosX+10
        eye1InitialPosY = initialPosY+SnakeConst.EYE_MARGIN 
        eye2InitialPosY = initialPosY+12

        renderSnakeCell(0,eyeInitialPosX,eye1InitialPosY,initialPosX+self.SNAKE_CELL_W-3,initialPosY+8,eyes=True)
        renderSnakeCell(0,eyeInitialPosX,eye2InitialPosY,initialPosX+self.SNAKE_CELL_W-3,initialPosY+self.SNAKE_CELL_H-SnakeConst.EYE_MARGIN,eyes=True)

        for i in range(self.snakeObj.getSize()):
            initialPosX  -= self.SNAKE_CELL_W
            initialPosX2 = initialPosX + self.SNAKE_CELL_W
            #1 for the snake head + 1 for loop begins at 0
            renderSnakeCell(i+2,initialPosX,initialPosY,initialPosX2,self.SNAKE_INITIAL_POSY2) 


    def randomPosition(self):
        r1 = Random()
        randPosX,randPosY = -1, -1

        while (randPosX % 20) > 0:
            randPosX = r1.randint(0,self.CANVAS_WIDTH)

        while (randPosY % 20) > 0:
            randPosY = r1.randint(0,(self.CANVAS_HEIGHT-self.SNAKE_CELL_H))
        
        return (randPosX,randPosY)


    def renderFood(self):
        posX,posY = self.randomPosition()
        self.foodObj.setPosX(posX)
        self.foodObj.setPosY(posY)
        foodImg = self.genCanvas.create_image(posX,posY,image=self.IMG_APPLE,anchor=tkinter.NW)
        self.foodObj.setObject(foodImg)


    def renderScore(self):
        self.bottomCanvas.create_text(self.SCORE_MARGIN_HORIZONTAL*5,self.SCORE_MARGIN_VERTICAL/2,font=self.FONT_TEXT,text="Score:")


    def renderScoreValue(self,points):
        self.bottomCanvas.delete(self.scoreObj)
        
        if len(points) == 1:
            self.scoreObj = self.bottomCanvas.create_text(self.SCORE_MARGIN_HORIZONTAL*11,self.SCORE_MARGIN_VERTICAL/2,font=self.FONT_TEXT,text=points)
        elif len(points) == 2:
            self.scoreObj = self.bottomCanvas.create_text(self.SCORE_MARGIN_HORIZONTAL*11+5,self.SCORE_MARGIN_VERTICAL/2,font=self.FONT_TEXT,text=points)
        else:
            self.scoreObj = self.bottomCanvas.create_text(self.SCORE_MARGIN_HORIZONTAL*11+10,self.SCORE_MARGIN_VERTICAL/2,font=self.FONT_TEXT,text=points)


    def renderInstructions(self,mode):
        if mode == self.NORMAL_TEXT:
            textBegin = "Press "
            textEnd = "to start"
            imgOffset = 65
            horzOffset = 145
            color = SnakeConst.BLACK_COLOR
            img = self.IMG_KEYS
        else:
            textBegin = "You lost! Press "
            textEnd = "to start again"
            imgOffset = 130
            horzOffset = 250
            color = SnakeConst.RED_COLOR
            img = self.IMG_RETURN

        instrObjList = []
        instr1 = self.bottomCanvas.create_text(self.WINDOW_WIDTH/2-(self.SCORE_MARGIN_HORIZONTAL*8),self.SCORE_MARGIN_VERTICAL/2,font=self.FONT_TEXT,text=textBegin,fill=color)
        instr2 = self.bottomCanvas.create_image(self.WINDOW_WIDTH/2-(self.SCORE_MARGIN_HORIZONTAL*8)+imgOffset,(self.SCORE_MARGIN_VERTICAL/2)-3, image=img)
        instr3 = self.bottomCanvas.create_text(self.WINDOW_WIDTH/2-(self.SCORE_MARGIN_HORIZONTAL*8)+horzOffset,self.SCORE_MARGIN_VERTICAL/2,font=self.FONT_TEXT,text=textEnd,fill=color)
        
        instrObjList.append(instr1)
        instrObjList.append(instr2)
        instrObjList.append(instr3)
        self.instrObj = instrObjList


    def clearsInstructions(self,objList):
        for obj in objList:
            self.bottomCanvas.delete(obj)
        self.instrObj = []

    
    def resetAllCommands(self):
        for k in self.commands:
            self.commands[k] = False


    def resetOtherCommands(self,command):
        for k in self.commands:
            if k != command:
                self.commands[k] = False


    def key_pressed(self,event):
        self.commands[event.keysym] = True
        self.resetOtherCommands(event.keysym)

    
    def eatFood(self):
        self.genCanvas.delete(self.foodObj.getObject())

        self.points = self.points + self.FOOD_SCORE
        self.renderScoreValue(str(self.points))

        self.snakeObj.growSnake(self)
        
        self.renderFood()
    
    def collidesFood(self):
        return (self.snakeObj.getPosX() == self.foodObj.getPosX()) and (self.snakeObj.getPosY() == self.foodObj.getPosY())


    def snakeCollision(self):
        if self.snakeObj.getDirection() == SnakeConst.RIGHT:
            return (self.snakeObj.getPosX()+self.SNAKE_CELL_W <= -1) or (self.snakeObj.getPosX()+self.SNAKE_CELL_W >= self.CANVAS_WIDTH+1) or (self.snakeObj.getPosY() <= -1) or (self.snakeObj.getPosY() >= self.CANVAS_HEIGHT+1)
        elif self.snakeObj.getDirection() == SnakeConst.DOWN:
            return (self.snakeObj.getPosX() <= -1) or (self.snakeObj.getPosX() >= self.CANVAS_WIDTH+1) or (self.snakeObj.getPosY()+self.SNAKE_CELL_H <= -1) or (self.snakeObj.getPosY()+self.SNAKE_CELL_H >= self.CANVAS_HEIGHT+1)
        else:
            return (self.snakeObj.getPosX() <= -1) or (self.snakeObj.getPosX() >= self.CANVAS_WIDTH+1) or (self.snakeObj.getPosY() <= -1) or (self.snakeObj.getPosY() >= self.CANVAS_HEIGHT+1)


    def loadSoundChannels(self):
        self.loopChannel  = pygame.mixer.Channel(0)
        self.spontChannel = pygame.mixer.Channel(1)       

        
    def play(self):
        if self.playing:
            if self.commands[SnakeConst.UP]:
                self.snakeObj.move(SnakeConst.UP,self)
                self.moving = True
            elif self.commands[SnakeConst.DOWN]:
                self.snakeObj.move(SnakeConst.DOWN,self)
                self.moving = True
            elif self.commands[SnakeConst.RIGHT]:
                self.snakeObj.move(SnakeConst.RIGHT,self)
                self.moving = True
            elif self.commands[SnakeConst.LEFT]:
                self.snakeObj.move(SnakeConst.LEFT,self)
                self.moving = True

            if self.moving:
                self.clearsInstructions(self.instrObj)
                self.loopChannel.play(pygame.mixer.Sound(self.MOVE_SOUND),loops = -1)

            for cell in self.snakeObj.getCells():
                self.genCanvas.move(cell.obj,cell.getStepX(),cell.getStepY())
                cell.resetSteps()
                
            if self.snakeCollision() or self.snakeObj.snakeBodyCollision():
                self.spontChannel.play(pygame.mixer.Sound(self.COLLISION_SOUND))
                self.loopChannel.pause()
                self.moving = False
                self.renderInstructions(self.END_TEXT)
                self.playing = False
            
            if self.collidesFood():
                self.spontChannel.play(pygame.mixer.Sound(self.EAT_SOUND))
                self.eatFood()

            # speed in millisecconds
            self.window.after(1000-self.snakeObj.getSpeed()*100, self.play)


    def playAgain(self,event):
        if event.keysym == "Return":
            self.points = 0
            self.renderScoreValue(str(self.points))
            self.clearsInstructions(self.instrObj)
            self.clearsSnake()
            self.resetAllCommands()
            self.renderSnake()
            self.snakeObj.setDirection(SnakeConst.RIGHT)
            self.renderInstructions(self.NORMAL_TEXT)
            self.playing = True
            self.play()


if __name__ == '__main__':
    window = tkinter.Tk()
    pygame.init()
    
    sr = Screen(window)
    sr.renderScore()
    sr.renderScoreValue(str(sr.points))
    sr.renderInstructions(sr.NORMAL_TEXT)
    sr.loadSoundChannels()
    
    window.bind("<KeyPress>", sr.key_pressed)
    window.bind("<Return>", sr.playAgain)
    
    sr.play()

    window.mainloop()

