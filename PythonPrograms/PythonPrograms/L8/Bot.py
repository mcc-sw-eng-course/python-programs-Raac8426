import Board
import random

class Bot(object):
    def __init__(self,player=2):
        self.player=player

    def bestMovement(self,player,board):
        arr=board.getPossibleMovements(player)
        rand=random.randint(0,len(arr)-1)
        return arr[rand]['position']
    
