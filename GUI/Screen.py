'''
Created on 05/08/2020

GUI logic

@author: Carlos Portela
'''

import tkinter
import Logic.Game as Game
from random import Random
from PIL import Image, ImageTk
from Logic.Board import Board


window = tkinter.Tk()

#list of objects composing the snake
fullSnake = []

windowWidth = 1000
windowHeight = 800

verticalMargin = 60
horizontalMargin = 20

frameWidth = windowWidth
frameHeight = windowHeight-verticalMargin

snakeCellW = 20
snakeCellH = 20

scoreMarginVertical = 48
scoreMarginHorizontal = 10

imgApple = ImageTk.PhotoImage(Image.open("../Resources/apple2.png"))
imgEnter = ImageTk.PhotoImage(Image.open("../Resources/enter.png"))

#window general canvas
genCanvas = tkinter.Canvas(window, width=frameWidth, height=frameHeight,bg="green",highlightbackground="black")
genCanvas.pack()


def createBoardUI():
    board = Board(windowWidth,windowHeight)

    #defines window size
    window.geometry(board.getGeometry())
    window.title(board.title)

    # prevent window from getting resized
    window.resizable(0,0)

    windowFrame = tkinter.Frame(window, width = frameWidth, height = frameHeight, bg = "green")
    # pack is used to show the object in the window
    #windowFrame.pack()


def renderSnakeCell(posX1,posY1,posX2,posY2):
    cell = genCanvas.create_rectangle(posX1,posY1,posX2,posY2, fill="red",outline="blue")
    fullSnake.append(cell)


def renderSnake():

    initialPosX = windowWidth/2
    initialPosY = windowHeight/2
    eyeYMargin  = 2

    #creates rectangle for the head
    initialPosX2 = initialPosX+snakeCellW
    initialPosY2 = initialPosY+snakeCellH
    head = genCanvas.create_rectangle(initialPosX,initialPosY,initialPosX2,initialPosY2, fill="red",outline="blue")
    
    #creates snake eyes
    eye1 = genCanvas.create_rectangle(initialPosX+10,initialPosY+eyeYMargin,initialPosX+snakeCellW-3,initialPosY+8, fill="blue")
    eye2 = genCanvas.create_rectangle(initialPosX+10,initialPosY+12,initialPosX+snakeCellW-3,initialPosY+snakeCellH-eyeYMargin, fill="blue")

    #adds snake objects to the list
    fullSnake.append(head)
    fullSnake.append(eye1)
    fullSnake.append(eye2)
    
    for _ in range(3):  #TODO change to snake SIZE
        initialPosX  -= snakeCellW
        initialPosX2 = initialPosX + snakeCellW
        renderSnakeCell(initialPosX,initialPosY,initialPosX2,initialPosY2)


# returns tuple for random position to place food
def randomPosition():
    r1 = Random()
    randPosX = r1.randint(0,frameWidth)
    randPosY = r1.randint(0,frameHeight)
    
    return (randPosX,randPosY)


# renders an apple in a random position
def renderFood(frame):
    posX,posY = randomPosition()
    
    food = tkinter.Canvas(frame, width=snakeCellW, height=snakeCellH,bg="green",highlightthickness=0)
    food.place(x=posX,y=posY)
    #food.image = imgApple
    food.create_image(10,11, image=imgApple)
    

def renderScore():
    score = tkinter.Canvas(window, width=windowWidth/5, height=snakeCellH*2,highlightthickness=0)
    score.place(x=scoreMarginHorizontal,y=windowHeight-scoreMarginVertical)
    score.create_text(scoreMarginHorizontal*5,scoreMarginVertical/2,font="Times 25 bold",text="Score:")

    return score


def renderScoreValue(canvas,points):
    if len(points) == 1:   
        canvas.create_text(scoreMarginHorizontal*11,scoreMarginVertical/2,font="Times 25 bold",text=points)
    elif len(points) == 2:
        canvas.create_text(scoreMarginHorizontal*11+5,scoreMarginVertical/2,font="Times 25 bold",text=points)
    else:
        canvas.create_text(scoreMarginHorizontal*11+10,scoreMarginVertical/2,font="Times 25 bold",text=points)
        

def renderInstructions():
    
    canvOffset = 30
    horzOffset = 65
    
    instr = tkinter.Canvas(window,width=windowWidth/3, height=snakeCellH*2,highlightthickness=0)
    instr.place(x=(windowWidth/3)+canvOffset,y=windowHeight - scoreMarginVertical)
    
    instr.create_text(scoreMarginHorizontal*5,scoreMarginVertical/2,font="Times 25 bold",text="Press ")
    
    #creates picture with key used to start the game
    instr.create_image(scoreMarginHorizontal*5+horzOffset,(scoreMarginVertical/2)-3, image=imgEnter)
    
    #creates remaining statement
    instr.create_text(scoreMarginHorizontal*5+(horzOffset*2.3),scoreMarginVertical/2,font="Times 25 bold",text="to start!")

