'''
Created on 05/08/2020

GUI logic

@author: Carlos Portela
'''
import tkinter
from random import Random
from PIL import Image, ImageTk
from Logic.Board import Board


windowWidth = 1000
windowHeight = 800

verticalMargin = 50
frameWidth = windowWidth
frameHeight = windowHeight-verticalMargin

snakeCellW = 20
snakeCellH = 20

window = tkinter.Tk()

def createBoardUI():

    board = Board(windowWidth,windowHeight)
    
    #defines window size
    window.geometry(board.getGeometry())
    window.title(board.title)

    # prevent window from getting resized
    window.resizable(0,0)
    
    windowFrame = tkinter.Frame(window, width = frameWidth, height = frameHeight, bg = "green")
    # pack is used to show the object in the window
    windowFrame.pack()
        
    return windowFrame



def renderSnakeHead(frame,posX,posY):
    s = tkinter.Canvas(frame, width=snakeCellW, height=snakeCellH,bg="blue")
    s.place(x=posX,y=posY)
    
    # creates snake eyes
    s.create_rectangle(snakeCellW-10,0, snakeCellW-3,snakeCellH-12, fill="red")
    s.create_rectangle(snakeCellW-10,snakeCellH-8, snakeCellW-3,snakeCellH, fill="red")


def renderSnakeCell(frame,posX,posY):
    s = tkinter.Canvas(frame, width=snakeCellW, height=snakeCellH,bg="blue")
    s.place(x=posX,y=posY)
    s.create_rectangle(4,4, snakeCellW-1, snakeCellH-2, fill="red")
    

def renderSnake(frame,snake):
    
    snakePosX = windowWidth/2
    snakePosY = windowHeight/2

    renderSnakeHead(frame,snakePosX,snakePosY)
    
    for _ in range(snake.getSize()):
        snakePosX -= snakeCellW
        renderSnakeCell(frame,snakePosX,snakePosY)

    '''img = Image.open("../Resources/snake2.gif")
    print(img.size)
    image = ImageTk.PhotoImage(img)
    s.image = image
    s.create_image(windowWidth/2,windowHeight/3, image=image)'''
        

# returns tuple for random position to place food
def randomPosition():
    r1 = Random()
    randPosX = r1.randint(0,frameWidth)
    randPosY = r1.randint(0,frameHeight)
    
    return (randPosX,randPosY)


# renders an apple in a random position
def renderFood(frame):
    
    posX,posY = randomPosition()
    
    food = tkinter.Canvas(frame, width=snakeCellW, height=snakeCellH,bg="black")
    food.place(x=posX,y=posY)
    
    
# Just to test
if __name__ == '__main__':
    
    frame = createBoardUI()
    
    renderSnake(frame)
    
    window.mainloop()

