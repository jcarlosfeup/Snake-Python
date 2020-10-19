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
fullSnake = []

windowWidth = 1000
windowHeight = 800

verticalMargin = 50
horizontalMargin = 20

frameWidth = windowWidth
frameHeight = windowHeight-verticalMargin

snakeCellW = 20
snakeCellH = 20

scoreMarginVertical = 48
scoreMarginHorizontal = 10

imgApple = ImageTk.PhotoImage(Image.open("../Resources/apple2.png"))
imgEnter = ImageTk.PhotoImage(Image.open("../Resources/enter.png"))


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


def renderSnakeHead(frame,posX,posY):
    s = tkinter.Canvas(frame, width=snakeCellW, height=snakeCellH,bg="blue",highlightbackground="black")
    s.place(x=posX,y=posY)
    #s.pack()
    
    # creates snake eyes
    eye1 = s.create_rectangle(snakeCellW-10,0, snakeCellW-3,snakeCellH-12, fill="red")
    eye2 = s.create_rectangle(snakeCellW-10,snakeCellH-8, snakeCellW-3,snakeCellH, fill="red")

    fullSnake.append((s,eye1))
    fullSnake.append((s,eye2))


def renderSnakeCell(frame,posX,posY):
    s = tkinter.Canvas(frame, width=snakeCellW, height=snakeCellH,bg="blue",highlightbackground="black")
    s.place(x=posX,y=posY)
    #s.pack()
    rect = s.create_rectangle(4,4, snakeCellW-1, snakeCellH-2, fill="red")
    
    Game.snake.setCanvas(s)

    fullSnake.append((s,rect))
    

def renderSnake(frame):
    snakePosX = windowWidth/2
    snakePosY = windowHeight/2

    renderSnakeHead(frame,snakePosX,snakePosY)

    for _ in range(Game.snake.getSize()):
        snakePosX -= snakeCellW
        renderSnakeCell(frame,snakePosX,snakePosY)


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

