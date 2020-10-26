'''
Created on 05/08/2020

GUI logic

@author: Carlos Portela
'''

import tkinter
from random import Random
from PIL import Image, ImageTk
from Logic.Board import Board
from Logic.Snake import Snake
from Logic.Cell import Cell

class Screen:
    
    def __init__(self,window):
        self.window = window
        self.snakeObj = Snake()
        
        self.initConstants()
        self.createBoardUI()
        self.createCanvas()
        self.createImages()
        self.renderSnake()
        self.renderFood()
        self.initObjects()


    def initConstants(self):
        self.WINDOW_WIDTH = 1000
        self.WINDOW_HEIGHT = 800

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
        
        self.SCORE_MARGIN_VERTICAL = 48
        self.SCORE_MARGIN_HORIZONTAL = 10
        
    def initObjects(self):
        self.snakeObj.setPosX(self.SNAKE_INITIAL_POSX2)
        self.snakeObj.setPosY(self.SNAKE_INITIAL_POSY2)


    def createBoardUI(self):
        board = Board(self.WINDOW_WIDTH,self.WINDOW_HEIGHT)

        #defines window size
        self.window.geometry(board.getGeometry())
        self.window.title(board.title)
    
        # prevent window from getting resized
        self.window.resizable(0,0)


    def createCanvas(self):
        #window general canvas
        self.genCanvas = tkinter.Canvas(window, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT,bg="green",highlightbackground="black")
        self.genCanvas.pack()


    def createImages(self):
        apple = Image.open("../Resources/apple.png")
        apple = apple.resize((self.FOOD_H, self.FOOD_W), Image.ANTIALIAS)

        self.IMG_APPLE = ImageTk.PhotoImage(apple)
        self.IMG_ENTER = ImageTk.PhotoImage(Image.open("../Resources/enter.png"))


    def renderSnake(self):

        def renderSnakeCell(indice,posX1,posY1,posX2,posY2):
            cell = self.genCanvas.create_rectangle(posX1,posY1,posX2,posY2, fill="red",outline="blue")
            self.snakeObj.addToCells(Cell(indice,posX1,posY1,cell))

        initialPosX = (self.WINDOW_WIDTH)/2
        initialPosY = (self.WINDOW_HEIGHT)/2
        eyeYMargin  = 2

        #creates rectangle for the head
        head = self.genCanvas.create_rectangle(initialPosX,initialPosY,
                                               self.SNAKE_INITIAL_POSX2,
                                               self.SNAKE_INITIAL_POSY2,
                                               fill="red",outline="blue")
        eyeInitialPosX = initialPosX+10
        eye1InitialPosY = initialPosY+eyeYMargin
        eye2InitialPosY = initialPosY+12

        eye1 = self.genCanvas.create_rectangle(eyeInitialPosX,eye1InitialPosY,
                                               initialPosX+self.SNAKE_CELL_W-3,initialPosY+8,
                                               fill="blue")
        eye2 = self.genCanvas.create_rectangle(eyeInitialPosX,eye2InitialPosY,
                                               initialPosX+self.SNAKE_CELL_W-3,initialPosY+self.SNAKE_CELL_H-eyeYMargin,
                                               fill="blue")

        #adds objects/poligons to the snake object
        self.snakeObj.addToCells(Cell(1,initialPosX,initialPosY,head))
        self.snakeObj.addToCells(Cell(1,eyeInitialPosX,eye1InitialPosY,eye1))
        self.snakeObj.addToCells(Cell(1,eyeInitialPosX,eye2InitialPosY,eye2))

        for i in range(self.snakeObj.getSize()):
            initialPosX  -= self.SNAKE_CELL_W
            initialPosX2 = initialPosX + self.SNAKE_CELL_W
            renderSnakeCell(i+2,initialPosX,initialPosY,initialPosX2,self.SNAKE_INITIAL_POSY2) #1 for the snake head + 1 for loop begins at 0


    # returns tuple for random position to place food
    def randomPosition(self):
        r1 = Random()
        randPosX = -1
        randPosY = -1

        while (randPosX % 10) > 0:
            randPosX = r1.randint(0,self.CANVAS_WIDTH)

        while (randPosY % 10) > 0:
            randPosY = r1.randint(0,self.CANVAS_HEIGHT)
        
        return (randPosX,randPosY)


    # renders an apple in a random position
    def renderFood(self):
        posX,posY = self.randomPosition()
        self.genCanvas.create_image(posX,posY,image=self.IMG_APPLE)


    def renderScore(self):
        score = tkinter.Canvas(window, width=self.WINDOW_WIDTH/5, height=self.SNAKE_CELL_H*2,highlightthickness=0)
        score.place(x=self.SCORE_MARGIN_HORIZONTAL,y=self.WINDOW_HEIGHT-self.SCORE_MARGIN_VERTICAL)
        score.create_text(self.SCORE_MARGIN_HORIZONTAL*5,self.SCORE_MARGIN_VERTICAL/2,font="Times 25 bold",text="Score:")

        return score


    def renderScoreValue(self,canvas,points):
        if len(points) == 1:   
            canvas.create_text(self.SCORE_MARGIN_HORIZONTAL*11,self.SCORE_MARGIN_VERTICAL/2,font="Times 25 bold",text=points)
        elif len(points) == 2:
            canvas.create_text(self.SCORE_MARGIN_HORIZONTAL*11+5,self.SCORE_MARGIN_VERTICAL/2,font="Times 25 bold",text=points)
        else:
            canvas.create_text(self.SCORE_MARGIN_HORIZONTAL*11+10,self.SCORE_MARGIN_VERTICAL/2,font="Times 25 bold",text=points)
        

    def renderInstructions(self):
        
        canvOffset = 30
        horzOffset = 65
        
        instr = tkinter.Canvas(window,width=self.WINDOW_WIDTH/3, height=self.SNAKE_CELL_H*2,highlightthickness=0)
        instr.place(x=(self.WINDOW_WIDTH/3)+canvOffset,y=self.WINDOW_HEIGHT - self.SCORE_MARGIN_VERTICAL)
        
        instr.create_text(self.SCORE_MARGIN_HORIZONTAL*5,self.SCORE_MARGIN_VERTICAL/2,font="Times 25 bold",text="Press ")
        
        #creates picture with key used to start the game
        instr.create_image(self.SCORE_MARGIN_HORIZONTAL*5+horzOffset,(self.SCORE_MARGIN_VERTICAL/2)-3, image=self.IMG_ENTER)
        
        #creates remaining statement
        instr.create_text(self.SCORE_MARGIN_HORIZONTAL*5+(horzOffset*2.3),self.SCORE_MARGIN_VERTICAL/2,font="Times 25 bold",text="to start!")


    '''You hold all snake units in a list - that's already done. There are head and tail which are the first and the last elements of the list. So it is actually a queue.
    On each tick, determine the direction in which you should move. For example, if the direction is left, then next head coordinates will be at (-1,0) relative to current head.
    Insert new unit in the list at the head position with the coordinates determined in step 2.
    Remove the tail unit from the list (and from the screen).'''
    def movement(self,event):
        x_offset,y_offset = self.snakeObj.move(event)

        for cell in self.snakeObj.getCells():

            #calculates offset based on last position
            self.genCanvas.move(cell.obj,x_offset,y_offset)


if __name__ == '__main__':

    window = tkinter.Tk()
    sr = Screen(window)

    points = 0

    scoreCanvas = sr.renderScore()
    sr.renderScoreValue(scoreCanvas,str(points))
    
    # while not click on ENTER, renders ELSE hides
    sr.renderInstructions()
    
    #binds keyboard keys to a procedure
    window.bind("<Key>", sr.movement)
    
    window.mainloop()

