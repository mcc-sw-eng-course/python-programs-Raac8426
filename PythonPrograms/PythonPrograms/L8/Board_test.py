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
        self.assertEqual("100000000","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(2,1)
        self.assertEqual("120000000","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(1,2)
        self.assertEqual("121000000","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(2,3)
        self.assertEqual("121200000","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(1,4)
        self.assertEqual("121210000","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(2,5)
        self.assertEqual("121212000","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(1,6)
        self.assertEqual("121212100","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(2,7)
        self.assertEqual("121212120","".join(str(x) for x in self.Board.getBoard()))
        self.Board.doMovement(1,8)

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

    def test_getWiner_no_Winer_empty(self):
        self.assertEqual(0,self.Board.getWiner())

    def test_getWiner_no_Winer_full(self):
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
        self.assertEqual(0,self.Board.getWiner())

    def test_getWiner_no_Winer_line1(self):
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
        self.assertEqual(1,self.Board.getWiner())

    def test_getWiner_no_Winer_line2(self):
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
        self.assertEqual(1,self.Board.getWiner())

    def test_getWiner_no_Winer_line3(self):
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
        self.assertEqual(1,self.Board.getWiner())

    def test_getWiner_no_Winer_line4(self):
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

    def test_getWiner_no_Winer_line5(self):
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
        self.assertEqual(1,self.Board.getWiner())

    def test_getWiner_no_Winer_line6(self):
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
        self.assertEqual(1,self.Board.getWiner())

    def test_getWiner_no_Winer_line7(self):
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
        self.assertEqual(1,self.Board.getWiner())

    def test_getWiner_no_Winer_line8(self):
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
        self.assertEqual(1,self.Board.getWiner())

    def test_getPossibleMovements(self):
        possibleMovements=self.Board.getPossibleMovements(2)
        self.assertEqual("200000000","".join(str(x) for x in possibleMovements[0]['board']))
        self.assertEqual("020000000","".join(str(x) for x in possibleMovements[1]['board']))
        self.assertEqual("002000000","".join(str(x) for x in possibleMovements[2]['board']))
        self.assertEqual("000200000","".join(str(x) for x in possibleMovements[3]['board']))
        self.assertEqual("000020000","".join(str(x) for x in possibleMovements[4]['board']))
        self.assertEqual("000002000","".join(str(x) for x in possibleMovements[5]['board']))
        self.assertEqual("000000200","".join(str(x) for x in possibleMovements[6]['board']))
        self.assertEqual("000000020","".join(str(x) for x in possibleMovements[7]['board']))
        self.assertEqual("000000002","".join(str(x) for x in possibleMovements[8]['board']))
        self.assertEqual(0,possibleMovements[0]['position'])
        self.assertEqual(1,possibleMovements[1]['position'])
        self.assertEqual(2,possibleMovements[2]['position'])
        self.assertEqual(3,possibleMovements[3]['position'])
        self.assertEqual(4,possibleMovements[4]['position'])
        self.assertEqual(5,possibleMovements[5]['position'])
        self.assertEqual(6,possibleMovements[6]['position'])
        self.assertEqual(7,possibleMovements[7]['position'])
        self.assertEqual(8,possibleMovements[8]['position'])

    def test_getPossibleMovements_incorrect_player(self):
        with self.assertRaises(ValueError):
            self.Board.getPossibleMovements(3)
if __name__ == '__main__':
    unittest.main()
