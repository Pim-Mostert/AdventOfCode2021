def NumberOfIncrements(x):
    xL0 = x[1:]
    xL1 = x[:-1]
    
    inc = [a > b for (a,b) in zip(xL0, xL1)]
    
    return inc.count(True)
    
def NumberOfSmoothedIncrements(x):
    x0 = x[:-2]
    x1 = x[1:-1]
    x2 = x[2:]
    
    s = [sum(x) for x in zip(x0, x1, x2)]

    return NumberOfIncrements(s)
        