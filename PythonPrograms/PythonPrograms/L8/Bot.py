import Board
import random

class Bot(object):
    def __init__(self,player=2):
        self.player=player

    def bestMovement(self,player,board):
        arr=board.getPossibleMovements(player)
        for possibleMovement in arr:
            possibleMovement['eval']= self.evaluatePossibleMovement(possibleMovement)
        win=list(filter(lambda x: x['eval'] == "win",arr))
        if(win != []):
            #print (win)
            return win[0]['position']
        block=list(filter(lambda x: x['eval'] == "block",arr))
        if(block != []):
            #print(block)
            return block[0]['position']
        rand=random.randint(0,len(arr)-1)
        return arr[rand]['position']

    def evaluatePossibleMovement(self,possibleMovement):
        if(self.isBoardWin(possibleMovement['board'])):
            return "win"
        if(self.isMovementWinBlock(possibleMovement)):
            return "block"
        return "normal"
    
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

    def isMovementWinBlock(self,possibleMovement):
        mapResult=[0,5,4]
        mapPositionLine=[
            [0,3,6],[0,4],[0,5,7],
            [1,3],[1,4,6,7],[1,5],
            [2,3],[2,4],[2,5,6]
        ]
        mapLineCells=[
            [0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]
        ]
        for line in mapPositionLine[possibleMovement['position']] :
            sum=0
            for cell in mapLineCells[line]:
                sum=sum+possibleMovement['board'][cell]
            if(sum==mapResult[self.player]):
                return True
        return False