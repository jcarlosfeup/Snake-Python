'''
Created on 05/08/2020

GUI logic

@author: Carlos Portela
'''
import tkinter
from Logic.Board import Board
from Logic.Snake import Snake

windowWidth = 1000
windowHeight = 800


def createBoardUI(windowWidth,windowHeight):

    verticalMargin = 50
    board = Board(windowWidth,windowHeight)
    
    window = tkinter.Tk()
    #defines window size
    window.geometry(board.getGeometry())
    window.title(board.title)
    
    # prevent window from getting resized
    window.resizable(0,0)
    
    windowFrame = tkinter.Frame(window, width = windowWidth, height = windowHeight-verticalMargin, bg = "brown")
    windowFrame.pack()
    
    # pack is used to show the object in the window
    window.mainloop()
    
    return window


def renderSnake(window):
    pass
    tkinter.Canvas(window, width=200, height=100)

    #snake = Snake(Game.windowWidth/2,Game.windowHeight/2)
    
    
    
    
    