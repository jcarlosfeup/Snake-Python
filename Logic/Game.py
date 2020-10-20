'''
Created on 05/08/2020

@author: jcarl
'''

import GUI.Screen as sr
from Logic.Snake import Snake


if __name__ == '__main__':

    points = 0
    
    sr.createBoardUI()

    #renders objects
    sr.renderFood(sr.window)
    sr.renderSnake()
    
    scoreCanvas = sr.renderScore()
    sr.renderScoreValue(scoreCanvas,str(points))

    def movement(event):
        x_offset, y_offset = 0, 0
        if event.keysym == "Up":
            y_offset = -10
            #snake.setPosY(snake.getPosY()+(1*snake.getSpeed()))  # substituir pelo metodo da classe
        elif event.keysym == "Down":
            #snake.setPosY(snake.getPosY()-(1*snake.getSpeed()))
            y_offset = +10
        elif event.keysym == "Left":
            #snake.setPosX(snake.getPosX()-(1*snake.getSpeed()))
            x_offset = -10
        elif event.keysym == "Right":
            #snake.setPosX(snake.getPosX()+(1*snake.getSpeed()))
            x_offset = +10

        for obj in sr.fullSnake:
            sr.genCanvas.move(obj,x_offset,y_offset)

        #print(snake.getPosX())
        #print(snake.getPosY())

    # while not click on ENTER, renders ELSE hides
    sr.renderInstructions()

    sr.window.bind("<Key>", movement)

    sr.window.mainloop()
