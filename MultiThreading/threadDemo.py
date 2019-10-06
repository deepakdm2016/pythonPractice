from threading import *

def displayNumber():
    print(current_thread().getName())
    for i in range(2,10):
        print(i)


print(current_thread().getName())
t=Thread(target=displayNumber)
t.start()
    