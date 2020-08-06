'''
Created on 05/08/2020

Contains the attributes of the game board

@author: Carlos Portela
'''

class Board:

    def __init__(self,width,height):
        self.boardWidth = width
        self.boardHeight = height
        self.title = "Snake"
    
    def getGeometry(self):
        return str(self.boardWidth) + "x" + str(self.boardHeight)
    
    
    
    