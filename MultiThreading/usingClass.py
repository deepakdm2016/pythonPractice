from threading import *
from time import sleep

class myThread:
    def displayNumbers(self):
        print(current_thread().getName())
        sleep(2)
        for i in range(2,10):
            print(i)

obj=myThread()

t=Thread(target=obj.displayNumbers)
t.start()

t1=Thread(target=obj.displayNumbers)
t1.start()

t2=Thread(target=obj.displayNumbers)
t2.start()
