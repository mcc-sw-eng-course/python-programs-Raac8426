import TicTacToe
import unittest


class FileSort_test(unittest.TestCase):
    def setUp(self):
        self.TicTacToe=TicTacToe.TicTacToe()
        
    def test_getPossibleMovements(self):
        possibleMovements=self.TicTacToe.getPossibleMovements(1)
        self.assertEqual("100000000","".join(str(x) for x in possibleMovements[0]))
        self.assertEqual("010000000","".join(str(x) for x in possibleMovements[1]))
        self.assertEqual("001000000","".join(str(x) for x in possibleMovements[2]))
        self.assertEqual("000100000","".join(str(x) for x in possibleMovements[3]))
        self.assertEqual("000010000","".join(str(x) for x in possibleMovements[4]))
        self.assertEqual("000001000","".join(str(x) for x in possibleMovements[5]))
        self.assertEqual("000000100","".join(str(x) for x in possibleMovements[6]))
        self.assertEqual("000000010","".join(str(x) for x in possibleMovements[7]))
        self.assertEqual("000000001","".join(str(x) for x in possibleMovements[8]))

    def test_getPossibleMovements_incorrect_player(self):
        with self.assertRaises(ValueError):
            self.TicTacToe.getPossibleMovements(0)


if __name__ == '__main__':
    unittest.main()
