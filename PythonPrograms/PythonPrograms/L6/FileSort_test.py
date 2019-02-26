import FileSort
import unittest
import os
import random
from pathlib import Path
import math

class FileSort_test(unittest.TestCase):
    def setUp(self):
        self.list=[]
        self.FileSorter=FileSort.FileSort()
        self.file="test123456789abc.data"
        self.elements=100000
        file = Path(self.file)
        if file.is_file():
            os.remove(self.file)

    def test_qSort(self):
        self.list.append(5)	
        self.list.append(7)
        self.list.append(3)
        self.list.append(56)
        self.list.append(2)
        self.list.append(5)
        self.list.append(7)
        self.list.append(63)
        self.assertEqual(self.FileSorter.quickSort(self.list),[2,3,5,5,7,7,56,63])
    
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
        
        self.assertEqual(self.FileSorter.heapSort(self.list),[2,3,5,5,7,7,56,63])

    def test_set_input_data_exception(self):
        with self.assertRaises(ValueError):
            self.FileSorter.set_input_data("awddq")

    def test_set_input_data_success(self):
        file=open(self.file,"x")
        self.FileSorter.set_input_data(self.file)
        self.assertEqual(self.FileSorter.readPath,self.file)
        file.close()
        os.remove(self.file)


    def test_set_input_data_exception(self):
        file=open(self.file,"x")
        with self.assertRaises(ValueError):
            self.FileSorter.set_output_data(self.file)
        file.close()
        os.remove(self.file)

    def test_set_input_data_success(self):
        self.FileSorter.set_output_data(self.file)
        self.assertEqual(self.FileSorter.writePath,self.file)
        os.remove(self.file)

    def test_writeListToFile(self):
        self.FileSorter.set_output_data(self.file)
        for i in range(0,self.elements):
            self.list.append(random.randint(-999999999,999999999))
        self.FileSorter.list=self.list
        self.FileSorter.writeListToFile() 
        file=open(self.file,"r")
        lines=file.readlines()
        equal=True
        for i in range(0,self.elements):
            equal=equal and self.list[i]==int(lines[i].replace("\n",""))
        file.close()
        os.remove(self.file)
        self.assertEqual(True,equal)

    def test_writeListToFile_error(self):
        with self.assertRaises(RuntimeError):
            self.FileSorter.list=[1,2,3,4]
            self.FileSorter.writeListToFile()

    def test_readListFromFile_error(self):
        with self.assertRaises(RuntimeError):
            self.FileSorter.readListFromFile()

    def test_readListFromFile(self):
        file=open(self.file,"w")
        for i in range(0,self.elements):
            number=random.randint(-999999999,999999999)
            self.list.append(number)
            file.write(str(number)+"\n")
        file.close()
        self.FileSorter.set_input_data(self.file)
        self.FileSorter.readListFromFile()
        os.remove(self.file)
        self.assertEqual(self.list,self.FileSorter.list)

    def test_execute_sort_except_source(self):
        with self.assertRaises(RuntimeError):
            self.FileSorter.execute_sort("")
    
    def test_execute_sort_except_destination(self):
        with self.assertRaises(RuntimeError):
            file=open(self.file,"x")
            file.close()
            self.FileSorter.set_input_data(self.file)
            self.FileSorter.execute_sort("")
            os.remove(seld.file)

    def test_execute_quick_sort(self):
        self.FileSorter.set_output_data(self.file+"o")
        file=open(self.file,"w")
        for i in range(0,self.elements):
            number=random.randint(-999999999,999999999)
            self.list.append(number)
            file.write(str(number)+"\n")
        file.close()
        self.FileSorter.set_input_data(self.file)
        self.FileSorter.execute_quick_sort()
        file=open(self.file+"o","r")
        lines=file.readlines()
        sorted=True
        current=-math.inf
        for line in lines:
            number=float(lines[i].replace("\n",""))
            sorted=sorted and current<=number
            current=number
        file.close()
        os.remove(self.file)
        os.remove(self.file+"o")
        self.assertEqual(True,sorted)

    def test_execute_merge_sort(self):
        self.FileSorter.set_output_data(self.file+"o")
        file=open(self.file,"w")
        for i in range(0,self.elements):
            number=random.randint(-999999999,999999999)
            self.list.append(number)
            file.write(str(number)+"\n")
        file.close()
        self.FileSorter.set_input_data(self.file)
        self.FileSorter.execute_merge_sort()
        file=open(self.file+"o","r")
        lines=file.readlines()
        sorted=True
        current=-math.inf
        for line in lines:
            number=float(lines[i].replace("\n",""))
            sorted=sorted and current<=number
            current=number
        file.close()
        os.remove(self.file)
        os.remove(self.file+"o")
        self.assertEqual(True,sorted)

    def test_execute_heap_sort(self):
        self.FileSorter.set_output_data(self.file+"o")
        file=open(self.file,"w")
        for i in range(0,self.elements):
            number=random.randint(-999999999,999999999)
            self.list.append(number)
            file.write(str(number)+"\n")
        file.close()
        self.FileSorter.set_input_data(self.file)
        self.FileSorter.execute_heap_sort()
        file=open(self.file+"o","r")
        lines=file.readlines()
        sorted=True
        current=-math.inf
        for line in lines:
            number=float(lines[i].replace("\n",""))
            sorted=sorted and current<=number
            current=number
        file.close()
        os.remove(self.file)
        os.remove(self.file+"o")
        self.assertEqual(True,sorted)

    def test_get_performance_data_except(self):
        with self.assertRaises(RuntimeError):
            self.FileSorter.get_performance_data()

    def test_get_performance_data(self):
        self.FileSorter.set_output_data(self.file+"o")
        file=open(self.file,"w")
        for i in range(0,self.elements):
            number=random.randint(-999999999,999999999)
            self.list.append(number)
            file.write(str(number)+"\n")
        file.close()
        self.FileSorter.set_input_data(self.file)
        self.FileSorter.execute_quick_sort()
        pData=self.FileSorter.get_performance_data()
        os.remove(self.file)
        os.remove(self.file+"o")
        self.assertEqual(pData["sortedElememts"],self.elements)



if __name__ == '__main__':
    unittest.main()
