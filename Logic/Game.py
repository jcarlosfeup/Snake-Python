'''
Created on 05/08/2020

@author: jcarl
'''
import tkinter
import GUI.Screen as sr
from Logic.Snake import Snake

def renderMovement(canvas,obj,objectClass):
    canvas.move(obj,objectClass.getPosX(),objectClass.getPosY())


def movement(snake):
    canvas = snake.getCanvas()
    canvas.move(snake.getRectangle(),snake.getPosX(),snake.getPosY())
    #canvas.after(1000,callback=movement)


if __name__ == '__main__':
    
    points = 0
    
    sr.createBoardUI()
    
    snake = Snake(sr.windowWidth/2,sr.windowHeight/2)
    snakeCanvas,rectangle = sr.renderSnake(sr.window,snake)
    
    snake.setCanvas(snakeCanvas)
    snake.setRectangle(rectangle)

    sr.renderFood(sr.window)
    scoreCanvas = sr.renderScore()
    sr.renderScoreValue(scoreCanvas,str(points))
        
    # This will bind arrow keys to the tkinter 
    # toplevel which will navigate the image or drawing 

    '''sr.bind("<KeyPress-Left>", lambda e: snake.move(e)) 
    sr.bind("<KeyPress-Right>", lambda e: snake.move(e)) 
    sr.bind("<KeyPress-Up>", lambda e: snake.move(e)) 
    sr.bind("<KeyPress-Down>", lambda e: snake.move(e))'''

    #TODO
    # while not click on ENTER, renders ELSE hides
    sr.renderInstructions()
    
    #print(snake.getPosX())
    #movement(snake)
    
    sr.window.mainloop()
