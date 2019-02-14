def checkNumber(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
def checkListNumber(list):
    for i in list:
        if(not checkNumber(i)):
            return False
    return True
def sampleMean(list):
    if(not checkListNumber(list)):
        raise ValueError('invalid list')
    var=0
    for value in list:
        var=var+value
    return var/len(list)
def standardDeviation(list):
    if(not checkListNumber(list)):
        raise ValueError('invalid list')
    mean=sampleMean(list)
    var=0
    for value in list:
        var=var+pow(abs(mean-value),2)
    return pow(var/len(list),.5)
def median(list):
    if(not checkListNumber(list)):
        raise ValueError('invalid list')
    sorted=list.copy()
    sorted.sort()
    center =int(len(list)/2)
    return sorted[center] if len(list)%2!=0 else (sorted[center]+sorted[center-1])/2
def nQuartile(list,n):
    if(not checkListNumber(list)):
        raise ValueError('invalid list')
    if(n<1 or n>3):
        raise ValueError('invalid quartile')
    if n== 2:
        return median(list)
    size=len(list)
    if(size%2==1):
        return median(list[0:int(size/2)]) if n==1 else median(list[int(size/2)+1:size]) 
    return median(list[0:int(size/2)]) if n==1 else median(list[int(size/2):size]) 
def nPercentile(list,n):
    if(not checkListNumber(list)):
        raise ValueError('invalid list')
    if(n<1 or n>99):
        raise ValueError('invalid percentile')
    if n in[25,50,75]:
        return nQuartile(list,n/25)
    sorted=list.copy()
    sorted.sort()
    size=len(list)
    pos=(n*(size-1))/100
    t=int(pos)
    if pos==t:
        return sorted[t]
    d=pos-t
    return sorted[t]+d*(sorted[t+1]-sorted[t])


