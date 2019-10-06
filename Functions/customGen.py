def customGen(x,y):
    while x<y:
        yield x
        x+=1
        
result=customGen(12, 25)

for i in result:
    print(i)