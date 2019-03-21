import Board
import random

class Bot(object):
    def __init__(self,player=2):
        self.player=player

    def bestMovement(self,player,board):
        arr=board.getPossibleMovements(player)
        rand=random.randint(0,len(arr)-1)
        return arr[rand]['position']
    
    def isBoardWin(self,possibleBoard):
        if (possibleBoard[0] == possibleBoard[1] and possibleBoard[2] == possibleBoard[0] and possibleBoard[0]==self.player):
            return True
        if (possibleBoard[3] == possibleBoard[4] and possibleBoard[5] == possibleBoard[3] and possibleBoard[3]==self.player):
            return True
        if (possibleBoard[6] == possibleBoard[7] and possibleBoard[8] == possibleBoard[6] and possibleBoard[6]==self.player):
            return True
        if (possibleBoard[0] == possibleBoard[3] and possibleBoard[6] == possibleBoard[0] and possibleBoard[0]==self.player):
            return True
        if (possibleBoard[1] == possibleBoard[4] and possibleBoard[7] == possibleBoard[1] and possibleBoard[1]==self.player):
            return True
        if (possibleBoard[2] == possibleBoard[5] and possibleBoard[8] == possibleBoard[2] and possibleBoard[2]==self.player):
            return True
        if (possibleBoard[0] == possibleBoard[4] and possibleBoard[8] == possibleBoard[0] and possibleBoard[0]==self.player):
            return True
        if (possibleBoard[2] == possibleBoard[4] and possibleBoard[6] == possibleBoard[2] and possibleBoard[2]==self.player):
            return True
        return False                                                                                           
