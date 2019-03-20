import Board
import Bot
class TicTacToe(object):
    def __init__(self,):
        self.board=Board.Board()
        self.sequence=[0,2,1]
        self.playerHumans=[False,True,False]
        self.map= [' ','X','O']

    def play(self,startsPlayer1=True,player1Human=True,player2Human=False):
        self.board=Board.Board()
        currentPlayer= 1 if startsPlayer1 else 2
        self.playerHumans[1]=player1Human
        self.playerHumans[2]=player2Human
        while(self.board.getWiner()==0 and not self.board.isBoardFull()):
            self.printBoard()
            self.playerTurn(currentPlayer)
            currentPlayer=self.sequence[currentPlayer]
        winer=self.board.getWiner()
        winer=self.map[winer]
        print("winner "+ winer if winer!=" " else "tie")
        self.printBoard()

    def playerTurn(self,player):
        position=    self.humanTurn(player) if self.playerHumans[player] else  self.botTurn(player)
        self.board.doMovement(player,position)
        
    def botTurn(self,player):
        bot= Bot.Bot()
        return bot.bestMovement(player,self.board)

    def humanTurn(self,player):
        position=input("player " + str(player)+ " enter your mark position 0-8")
        return int(position)
 

    def printBoard(self):
        board=self.board.getBoard()
        print(self.map[board[0]]+"|"+self.map[board[1]]+"|"+self.map[board[2]])
        print("-----")
        print(self.map[board[3]]+"|"+self.map[board[4]]+"|"+self.map[board[5]])
        print("-----")
        print(self.map[board[6]]+"|"+self.map[board[7]]+"|"+self.map[board[8]])

TicTacToe1 = TicTacToe()
TicTacToe1.play(True,True,True)
