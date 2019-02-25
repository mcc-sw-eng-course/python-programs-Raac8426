from pathlib import Path

class CSVFileSort(object):
    def __init__(self):
        self.readPath=""
        self.writePath=""
    def qSort(self,list):
        if(len(list)>1):
            upper, lower,same=[],[],[]
            pivot=list[int(len(list)/2)]

            for item in list:
                if(item>pivot):
                    upper.append(item)
                elif(item<pivot):
                    lower.append(item)
                else: 
                    same.append(item)
            return self.qSort(lower)+same+self.qSort(upper)
        return list

    def mergeSort(self,list): 
        if len(list) >1: 
            mid = len(list)//2
            L = self.mergeSort(list[:mid]) 
            R = self.mergeSort(list[mid:])   
            i = j = 0
            toReturn=[]

            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    toReturn.append( L[i] )
                    i+=1
                else: 
                    toReturn.append( R[j]) 
                    j+=1
            while i < len(L): 
                toReturn.append(L[i]) 
                i+=1       
            while j < len(R): 
                toReturn.append(R[j]) 
                j+=1
            return toReturn
        return list

    def heapSort(self, aList ):
        length = len( aList ) - 1
        leastParent = length // 2
        for i in range ( leastParent, -1, -1 ):
            self.moveDown( aList, i, length )

        for i in range ( length, 0, -1 ):
            if aList[0] > aList[i]:
                self.swap( aList, 0, i )
                self.moveDown( aList, 0, i - 1 )
     
    def moveDown(self, aList, first, last ):
        largest = 2 * first + 1
        while largest <= last:
            if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
                largest += 1
            if aList[largest] > aList[first]:
                self.swap( aList, largest, first )
                first = largest;
                largest = 2 * first + 1
            else:
                return
 
    def swap(self, A, x, y ):
      A[x],A[y] = A[y],A[x]

    def set_input_data(self,file_path_name):
        file = Path(file_path_name)
        if not file.is_file():
            raise ValueError("file not found")
        try:
            file=open(file_path_name,"r")
            self.readPath=file_path_name
            file.close()
        except:
            raise ValueError("could not open file")

    def set_output_data(self,file_path_name):        file = Path(file_path_name)
        if file.is_file():            raise ValueError("file already exists")        try:
            file=open(file_path_name,"x")
            file.close()
            self.writePath=file_path_name
        except:
            raise ValueError("could not create file")
