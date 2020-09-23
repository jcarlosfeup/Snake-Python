'''
Created on 05/08/2020

@author: jcarl
'''
from GUI.Screen import createBoardUI, renderSnake

if __name__ == '__main__':
    
    window = createBoardUI()
    
    renderSnake(window)
    
    
    window.mainloop()
