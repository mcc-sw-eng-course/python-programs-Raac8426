
import p9
import unittest

 
class TestP9(unittest.TestCase):


	def test_toRoman(self):
		roman=p9.toRoman(537)
		self.assertEqual(roman,"DXXXVII")	

	def test_toRomanZero(self):
		roman=p9.toRoman(0)
		self.assertEqual(roman,"")


	def test_toRomanInvalid(self):
		with self.assertRaises(ValueError):
			roman=p9.toRoman("q")

	def test_toRomanOut(self):
		roman=p9.toRoman(100000000)
		self.assertEqual(roman,"out of scope")



	


if __name__ == '__main__':
    unittest.main()
