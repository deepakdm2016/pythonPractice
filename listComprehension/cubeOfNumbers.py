#li=range(1,11)

'''
for i in li:
    print(i**3)
'''

lst=[]
lst=[x**3 for x in range (1,11)]
for i in lst:
    print(i)

evlst=[]
evlst=[x for x in range (2,21,2)]
for i in evlst:
    print(i)


evlst=[]
evlst=[x for x in range (1,21) if x%2==0]
for i in evlst:
    print(i)
    
