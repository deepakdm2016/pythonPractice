from threading import *
from time import *

def evenNumbers():
    e=[i for i in range(1,101) if i%2==0]
    print(e)
    
def oddNumbers():
    e=[i for i in range(1,101) if i%2!=0]
    print(e)
    
t1=Thread(target=evenNumbers)
t2=Thread(target=oddNumbers)

t1.start()
t2.start()
for i in range(1,101):
    print(i)