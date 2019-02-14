
import myPowerList
import unittest
 
class TestmyPowerList(unittest.TestCase):
	def setUp(self):
		self.list=myPowerList.myPowerList()
	def test_insert(self):
		
		self.list.add(5)	
		self.list.add(7)
		self.list.add(3)
		self.assertEqual(self.list.getList(),[5,7,3])
 
	def test_getElement(self):
		self.list.add(5)	
		self.list.add(7)
		self.list.add(3)
		self.assertEqual(self.list.getElementAt(0),5)
	
	def test_remove_element(self):
		self.list.add(5)	
		self.list.add(7)
		self.list.add(3)
		self.list.removeElementAt(1)
		self.assertEqual(self.list.getList(),[5,3])
	
	def test_sort(self):
		self.list.add(5)	
		self.list.add(7)
		self.list.add(3)
		self.list.add(56)
		self.list.add(2)
		self.list.add(5)
		self.list.add(7)
		self.list.add(63)
		self.assertEqual(self.list.sort(),[2,3,5,5,7,7,56,63])
	
	def test_sort(self):
		self.list.add(5)	
		self.list.add(7)
		self.list.add(3)
		self.list.add(56)
		self.list.add(2)
		self.list.add(5)
		self.list.add(7)
		self.list.add(63)
		self.list.sorted()
		self.assertEqual(self.list.getList(),[2,3,5,5,7,7,56,63])
	
	def test_toFile(self):
		self.list.add(5)	
		self.list.add(7)
		self.list.add(3)
		self.list.add(56)
		self.list.add(2)
		self.list.add(5)
		self.list.add(7)
		self.list.add(63)
		self.list.saveToFile("data.json")
		file=open("data.json","r")
		str=file.read()
		self.assertEqual(str,"[5, 7, 3, 56, 2, 5, 7, 63]")
		file.close()
	
	def test_from_file(self):
		file=open("data.json","w")
		str=file.write("[5,7,3,56,2,5]")
		file.close()
		self.list.readFromFile("data.json")
		self.assertEqual(self.list.getList(),[5,7,3,56,2,5])

if __name__ == '__main__':
    unittest.main()
