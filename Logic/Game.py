'''
Created on 05/08/2020

@author: jcarl
'''

import GUI.Screen as Screen
from Logic.Snake import Snake

if __name__ == '__main__':
    
    points = 0
    
    window = Screen.createBoardUI()
    
    snake = Snake(Screen.windowWidth/2,Screen.windowHeight/2)

    Screen.renderSnake(window,snake)
    
    Screen.renderFood(window)
    
    canvas = Screen.renderScore()
    Screen.renderScoreValue(canvas,str(points))
    
    #TODO
    # while not click on ENTER, renders ELSE hides
    Screen.renderInstructions()
    
    window.mainloop()
