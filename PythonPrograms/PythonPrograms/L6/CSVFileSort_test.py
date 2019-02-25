import CSVFileSort
import unittest
import os

class CSVFileSort_test(unittest.TestCase):
    def setUp(self):
        self.list=[]
        self.FileSorter=CSVFileSort.CSVFileSort()

    def test_qSort(self):
        self.list.append(5)	
        self.list.append(7)
        self.list.append(3)
        self.list.append(56)
        self.list.append(2)
        self.list.append(5)
        self.list.append(7)
        self.list.append(63)
        self.assertEqual(self.FileSorter.qSort(self.list),[2,3,5,5,7,7,56,63])
    
    def test_mergeSort(self):
        self.list.append(5)	
        self.list.append(7)
        self.list.append(3)
        self.list.append(56)
        self.list.append(2)
        self.list.append(5)
        self.list.append(7)
        self.list.append(63)
        self.assertEqual(self.FileSorter.mergeSort(self.list),[2,3,5,5,7,7,56,63])

    def test_heapSort(self):
        self.list.append(5)	
        self.list.append(7)
        self.list.append(3)
        self.list.append(56)
        self.list.append(2)
        self.list.append(5)
        self.list.append(7)
        self.list.append(63)
        self.FileSorter.heapSort(self.list)
        self.assertEqual(self.list,[2,3,5,5,7,7,56,63])

    def test_set_input_data_exception(self):
        with self.assertRaises(ValueError):
            self.FileSorter.set_input_data("awddq")

    def test_set_input_data_success(self):
        file=open("test.data","x")
        self.FileSorter.set_input_data("test.data")
        self.assertEqual(self.FileSorter.readPath,"test.data")
        file.close()
        os.remove("test.data")


    def test_set_input_data_exception(self):
        file=open("test.data","x")
        with self.assertRaises(ValueError):
            self.FileSorter.set_output_data("test.data")
        file.close()
        os.remove("test.data")

    def test_set_input_data_success(self):
        self.FileSorter.set_output_data("test.data")
        self.assertEqual(self.FileSorter.writePath,"test.data")
        os.remove("test.data")
if __name__ == '__main__':
    unittest.main()
