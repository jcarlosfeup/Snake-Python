'''
Created on 05/08/2020

GUI logic

@author: Carlos Portela
'''
import tkinter
from PIL import Image, ImageTk
from Logic.Board import Board
from Logic.Snake import Snake

windowWidth = 1000
windowHeight = 800

snakeCellW = 250
snakeCellH = 250

window = tkinter.Tk()

def createBoardUI():

    verticalMargin = 50
    board = Board(windowWidth,windowHeight)
    
    #defines window size
    window.geometry(board.getGeometry())
    window.title(board.title)
    
    # prevent window from getting resized
    window.resizable(0,0)
    
    windowFrame = tkinter.Frame(window, width = windowWidth, height = windowHeight-verticalMargin, bg = "brown")
    # pack is used to show the object in the window
    windowFrame.pack()
        
    return windowFrame


def renderSnake(frame):
    s = tkinter.Canvas(frame, width=snakeCellW, height=snakeCellH)
    s.place(x=windowWidth/2, y=windowHeight/2)
    
    img = Image.open("../Resources/snake2.gif")
    print(img.size)
    image = ImageTk.PhotoImage(img)
    s.image = image
    s.create_image(windowWidth/2,windowHeight/3, image=image)

    #s.create_rectangle(0, 0, snakeCellW, snakeCellH, fill="green")

    snake = Snake(windowWidth/2,windowHeight/2)
    
    

# Just to test
if __name__ == '__main__':
    
    frame = createBoardUI()
    
    renderSnake(frame)
    
    window.mainloop()

    
    
    