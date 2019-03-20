from pathlib import Path
import datetime

class Board(object):
    def __init__(self):
        self.board=[0,0,0,0,0,0,0,0,0]

    def getBoard(self):
        return self.board.copy()

    def doMovement(self,player,position):
        if(player not in [1,2]):
            raise ValueError("invalid movement")
        if(position not in range(0,9)):
            raise ValueError("invalid movement")
        if(self.board[position] != 0 ):
            raise ValueError("invalid movement")
        self.board[position]=player

    def isBoardFull(self):
        count=0
        for i in self.board:
            if (i != 0):
                count = count+1
        return count==9

    def getWiner(self):
        if(self.board[0]!=0 and self.board[0]==self.board[1] and self.board[1]==self.board[2]):
            return self.board[0]
        if(self.board[3]!=0 and self.board[3]==self.board[4] and self.board[4]==self.board[5]):
            return self.board[3]
        if(self.board[6]!=0 and self.board[6]==self.board[7] and self.board[7]==self.board[8]):
            return self.board[6]
        if(self.board[0]!=0 and self.board[0]==self.board[3] and self.board[3]==self.board[6]):
            return self.board[0]
        if(self.board[1]!=0 and self.board[1]==self.board[4] and self.board[4]==self.board[7]):
            return self.board[1]
        if(self.board[2]!=0 and self.board[2]==self.board[5] and self.board[5]==self.board[8]):
            return self.board[2]
        if(self.board[0]!=0 and self.board[0]==self.board[4] and self.board[4]==self.board[8]):
            return self.board[0]
        if(self.board[2]!=0 and self.board[2]==self.board[4] and self.board[4]==self.board[6]):
            return self.board[2]
        return 0

    def getPossibleMovements(self,player):
        if(player not in [1,2]):
            raise ValueError("invalid player")
        possibleMovements=[]
        for i in range(0,9):
            if(self.getBoard()[i]==0):
                temporal=self.getBoard()
                temporal[i]=player
                possibleMovements.append({'board':temporal,'position':i})
        return possibleMovements