x=123

def locGlobDemo():
    x=13
    print(x,globals()['x'])
    
print(x)
locGlobDemo()