import Bot
import unittest
import Board

class FileSort_test(unittest.TestCase):
    def setUp(self):
        self.player=2
        self.bot=Bot.Bot(self.player)
        self.board=Board.Board()
        self.opponent=[0,2,1]

    def test_isWinBoard_Line1(self):
        self.board.doMovement(self.player,0)
        self.board.doMovement(self.player,1)
        self.board.doMovement(self.player,2)
        self.assertEqual(True,self.bot.isBoardWin(self.board.getBoard()))

    def test_isWinBoard_Line2(self):
        self.board.doMovement(self.player,3)
        self.board.doMovement(self.player,4)
        self.board.doMovement(self.player,5)
        self.assertEqual(True,self.bot.isBoardWin(self.board.getBoard()))

    def test_isWinBoard_Line3(self):
        self.board.doMovement(self.player,6)
        self.board.doMovement(self.player,7)
        self.board.doMovement(self.player,8)
        self.assertEqual(True,self.bot.isBoardWin(self.board.getBoard()))

    def test_isWinBoard_Line4(self):
        self.board.doMovement(self.player,1)
        self.board.doMovement(self.player,4)
        self.board.doMovement(self.player,7)
        self.assertEqual(True,self.bot.isBoardWin(self.board.getBoard()))

    def test_isWinBoard_Line5(self):
        self.board.doMovement(self.player,2)
        self.board.doMovement(self.player,5)
        self.board.doMovement(self.player,8)
        self.assertEqual(True,self.bot.isBoardWin(self.board.getBoard()))

    def test_isWinBoard_Line6(self):
        self.board.doMovement(self.player,0)
        self.board.doMovement(self.player,3)
        self.board.doMovement(self.player,6)
        self.assertEqual(True,self.bot.isBoardWin(self.board.getBoard()))

    def test_isWinBoard_Line7(self):
        self.board.doMovement(self.player,0)
        self.board.doMovement(self.player,4)
        self.board.doMovement(self.player,8)
        self.assertEqual(True,self.bot.isBoardWin(self.board.getBoard()))

    def test_isWinBoard_Line8(self):
        self.board.doMovement(self.player,2)
        self.board.doMovement(self.player,4)
        self.board.doMovement(self.player,6)
        self.assertEqual(True,self.bot.isBoardWin(self.board.getBoard()))

    def test_isMovementWinBlock_position_0(self):
        self.assertEqual(True,self.bot.isMovementWinBlock({'board':[self.player,self.opponent[self.player],self.opponent[self.player],0,0,0,0,0,0],'position':0}))

    def test_isMovementWinBlock_position_1(self):
        self.assertEqual(True,self.bot.isMovementWinBlock({'board':[self.opponent[self.player],self.player,self.opponent[self.player],0,0,0,0,0,0],'position':1}))

    def test_isMovementWinBlock_position_2(self):
        self.assertEqual(True,self.bot.isMovementWinBlock({'board':[self.opponent[self.player],self.opponent[self.player],self.player,0,0,0,0,0,0],'position':2}))
    
    def test_isMovementWinBlock_position_3(self):
        self.assertEqual(True,self.bot.isMovementWinBlock({'board':[0,0,0,self.player,self.opponent[self.player],self.opponent[self.player],0,0,0],'position':3}))

    def test_isMovementWinBlock_position_4(self):
        self.assertEqual(True,self.bot.isMovementWinBlock({'board':[0,0,0,self.opponent[self.player],self.player,self.opponent[self.player],0,0,0],'position':4}))

    def test_isMovementWinBlock_position_5(self):
        self.assertEqual(True,self.bot.isMovementWinBlock({'board':[0,0,0,self.opponent[self.player],self.opponent[self.player],self.player,0,0,0],'position':5}))

    def test_isMovementWinBlock_position_6(self):
        self.assertEqual(True,self.bot.isMovementWinBlock({'board':[0,0,0,0,0,0,self.player,self.opponent[self.player],self.opponent[self.player]],'position':6}))

    def test_isMovementWinBlock_position_7(self):
        self.assertEqual(True,self.bot.isMovementWinBlock({'board':[0,0,0,0,0,0,self.opponent[self.player],self.player,self.opponent[self.player]],'position':7}))

    def test_isMovementWinBlock_position_8(self):
        self.assertEqual(True,self.bot.isMovementWinBlock({'board':[0,0,0,0,0,0,self.opponent[self.player],self.opponent[self.player],self.player],'position':8}))

    def test_evaluatePossibleMovement_block(self):
        self.assertEqual("block",self.bot.evaluatePossibleMovement({'board':[0,0,0,0,0,0,self.opponent[self.player],self.opponent[self.player],self.player],'position':8}))

    def test_evaluatePossibleMovement_win(self):
        self.assertEqual("win",self.bot.evaluatePossibleMovement({'board':[0,0,0,0,0,0,self.player,self.player,self.player],'position':8}))


if __name__ == '__main__':
    unittest.main()
