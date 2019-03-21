import Bot
import unittest
import Board

class FileSort_test(unittest.TestCase):
    def setUp(self):
        self.player=2
        self.bot=Bot.Bot(self.player)
        self.board=Board.Board()

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

if __name__ == '__main__':
    unittest.main()
