def checkInt(val):
    try:
        number=int(val)
        return True
    except ValueError:
        return False
def toRoman(var):
    if(not checkInt(var)):
        raise ValueError("invalid number")
    retVal=""
    Map1=["I","II","III","IV","V","VI","VII","VIII","IX"]
    Map10=["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    Map100=["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    Map1000=["M","MM","MMM","(I)(V)","(V)","(V)(I)","(V)(I)(I)","(V)(I)(I)(I)","(I)(X)"]
    Map10000=["(X)","(X)(X)","(X)(X)(X)","(X)(L)","(L)","(L)(X)","(L)(X)(X)","(L)(X)(X)(X)","(X)(C)"]
    Map100000=["(C)","(C)(C)","(C)(C)(C)","(C)(D)","(D)","(D)(C)","(D)(C)(C)","(D)(C)(C)(C)","(C)(M)"]
    Map1000000=["(M)"]
    dictionary=dict()
    dictionary[1]=Map1
    dictionary[10]=Map10
    dictionary[100]=Map100
    dictionary[1000]=Map1000
    dictionary[10000]=Map10000
    dictionary[100000]=Map100000
    dictionary[1000000]=Map1000000
    intVar=int(var)
    if intVar==0:
        return "";
    current=10000000
    if intVar>current/10:
        return "out of scope"
    while (True):
        res=intVar%current
        div=int((intVar/current))
        if div>0:
            retVal=retVal+dictionary[current][div-1]
        if(res==0):
            return retVal
        intVar=res
        current=current/10
