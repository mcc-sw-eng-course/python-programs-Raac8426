import json
class myPowerList(object):
    def __init__(self):
        self.list=[]
    def add(self,var):
        self.list.append(var)
    def getElementAt(self,index):
        return self.list[index]
    def getList(self):
        return self.list.copy()
    def removeElementAt(self,index):
        del self.list[index]
    def __qSort(self,list):
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
            return self.__qSort(lower)+same+self.__qSort(upper)
        return list
    def sort(self):
        return self.__qSort(self.list)
    def sorted(self):
        self.list=self.__qSort(self.list)
    def saveToFile(self,path):
        file=open(path,"w")
        file.write(json.dumps(self.list))
        file.close()
    def readFromFile(self,path):
        file=open(path,"r")
        string=file.read()
        self.list=json.loads(string)
        file.close()
