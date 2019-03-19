import Board
import unittest


class FileSort_test(unittest.TestCase):
    def setUp(self):
        self.Board=Board.Board()

    def test_getBoard(self):
        self.assertEqual("000000000","".join(str(x) for x in self.Board.getBoard()))
    
    def test_doMovement_incorrect_player(self):
        with self.assertRaises(ValueError):
            self.Board.doMovement(0,0)
    
    def test_doMovement_incorrect_position_lower(self):
        with self.assertRaises(ValueError):
            self.Board.doMovement(1,-1)

    def test_doMovement_incorrect_position_upper(self):
        with self.assertRaises(ValueError):
            self.Board.doMovement(1,9)

    def test_doMovement_already_taken_position(self):
        with self.assertRaises(ValueError):
            self.Board.doMovement(1,0)
            self.Board.doMovement(1,0)

    def test_doMovement(self):
        self.Board.doMovement(1,0)
        self.Board.printBoard()
        self.assertEqual("100000000","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(2,1)
        self.Board.printBoard()
        self.assertEqual("120000000","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(1,2)
        self.Board.printBoard()
        self.assertEqual("121000000","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(2,3)
        self.Board.printBoard()
        self.assertEqual("121200000","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(1,4)
        self.Board.printBoard()
        self.assertEqual("121210000","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(2,5)
        self.Board.printBoard()
        self.assertEqual("121212000","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(1,6)
        self.Board.printBoard()
        self.assertEqual("121212100","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(2,7)
        self.Board.printBoard()
        self.assertEqual("121212120","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(1,8)
        self.Board.printBoard()

    def test_isBoardFull(self):
        self.Board.doMovement(1,0)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,1)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,2)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,3)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,4)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,5)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,6)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,7)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,8)
        self.assertEqual(True,self.Board.isBoardFull())

    def test_getWinner_no_winner_empty(self):
        self.assertEqual(0,self.Board.getWinner())

    def test_getWinner_no_winner_full(self):
        self.Board.doMovement(1,0)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,1)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,2)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,3)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,5)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,8)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,7)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,4)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,6)
        self.assertEqual(0,self.Board.getWinner())

    def test_getWinner_no_winner_line1(self):
        print("")
        self.Board.doMovement(1,0)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,3)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,2)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,4)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,1)
        self.assertEqual(1,self.Board.getWinner())
        self.Board.printBoard()

    def test_getWinner_no_winner_line2(self):
        print("")
        self.Board.doMovement(1,3)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,6)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,5)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,7)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,4)
        self.assertEqual(1,self.Board.getWinner())
        self.Board.printBoard()

    def test_getWinner_no_winner_line3(self):
        print("")
        self.Board.doMovement(1,6)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,3)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,7)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,4)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,8)
        self.assertEqual(1,self.Board.getWinner())
        self.Board.printBoard()

    def test_getWinner_no_winner_line4(self):
        print("")
        self.Board.doMovement(1,0)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,1)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,3)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,2)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,6)
        self.assertEqual(1,self.Board.getWinner())
        self.Board.printBoard()

    def test_getWinner_no_winner_line5(self):
        print("")
        self.Board.doMovement(1,1)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,0)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,4)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,5)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,7)
        self.assertEqual(1,self.Board.getWinner())
        self.Board.printBoard()

    def test_getWinner_no_winner_line6(self):
        print("")
        self.Board.doMovement(1,2)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,0)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,5)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,4)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,8)
        self.assertEqual(1,self.Board.getWinner())
        self.Board.printBoard()

    def test_getWinner_no_winner_line7(self):
        print("")
        self.Board.doMovement(1,0)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,1)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,4)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,5)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,8)
        self.assertEqual(1,self.Board.getWinner())
        self.Board.printBoard()

    def test_getWinner_no_winner_line8(self):
        print("")
        self.Board.doMovement(1,2)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,1)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,4)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(2,5)
        self.assertEqual(False,self.Board.isBoardFull())
        self.Board.doMovement(1,6)
        self.assertEqual(1,self.Board.getWinner())
        self.Board.printBoard()

if __name__ == '__main__':
    unittest.main()
